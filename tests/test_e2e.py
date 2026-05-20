import httpx
import pytest
import respx
from pathlib import Path
from unittest.mock import MagicMock, patch
from typer.testing import CliRunner
from skillmaker.cli import app

runner = CliRunner()

_FIRECRAWL_RESPONSE = {
    "success": True,
    "data": {"markdown": "# Cold Email Openers\n\nUse pattern interrupts. Cite specific metrics."}
}

_ANALYSIS_TOOL_RESULT = {
    "adds_value": True,
    "reason": "Introduces pattern interrupt technique not in existing library.",
    "relevant_skills": [],
    "action": "create_new_skill",
    "key_insights": ["Pattern interrupts outperform compliments", "Cite specific metrics"],
}

_GENERATE_TOOL_RESULT = {
    "skill_slug": "cold-email-openers",
    "index_ts": (
        "export const slug = 'cold-email-openers'\n"
        "export const title = 'Cold Email Openers'\n"
        "export const applies_to = ['sales']\n"
        "export const mode: 'for_generating' | 'for_understanding' | 'mixed' = 'for_generating'\n"
        "export const covers = ['opener', 'pattern interrupt', 'metrics']\n"
        "export const use_when = 'Use when drafting cold email opening lines.'\n"
        "export const body = `# Cold Email Openers\n\n## Rules\n"
        "- Open with a specific metric or observation.\n"
        "- Use pattern interrupt, not flattery.\n\n"
        "## Anti-patterns\n"
        "- Starting with 'I hope this finds you well'.\n"
        "- Leading with your own company name.\n`\n"
    ),
    "refs": [],
    "handoff_note": "Add import and SKILLS.push() to kb/index.ts after tests pass."
}


def _mock_anthropic_client(tool_result: dict):
    mock_client = MagicMock()
    mock_message = MagicMock()
    mock_block = MagicMock()
    mock_block.type = "tool_use"
    mock_block.input = tool_result
    mock_message.content = [mock_block]
    mock_client.messages.create.return_value = mock_message
    return mock_client


@respx.mock
def test_blog_url_full_pipeline_no_write(tmp_path):
    respx.post("https://api.firecrawl.dev/v1/scrape").mock(
        return_value=httpx.Response(200, json=_FIRECRAWL_RESPONSE)
    )
    with patch("skillmaker.analyzer.anthropic.Anthropic",
               return_value=_mock_anthropic_client(_ANALYSIS_TOOL_RESULT)), \
         patch("skillmaker.generator.anthropic.Anthropic",
               return_value=_mock_anthropic_client(_GENERATE_TOOL_RESULT)):
        result = runner.invoke(app, [
            "process", "https://example.com/blog/cold-email-openers",
            "--skills-dir", str(tmp_path),
        ])
    assert result.exit_code == 0
    assert "cold-email-openers" in result.output
    assert "PASTEABLE BUNDLE" in result.output
    assert "=== HANDOFF ===" in result.output
    assert not (tmp_path / "cold-email-openers").exists()


@respx.mock
def test_blog_url_full_pipeline_with_write(tmp_path):
    respx.post("https://api.firecrawl.dev/v1/scrape").mock(
        return_value=httpx.Response(200, json=_FIRECRAWL_RESPONSE)
    )
    with patch("skillmaker.analyzer.anthropic.Anthropic",
               return_value=_mock_anthropic_client(_ANALYSIS_TOOL_RESULT)), \
         patch("skillmaker.generator.anthropic.Anthropic",
               return_value=_mock_anthropic_client(_GENERATE_TOOL_RESULT)):
        result = runner.invoke(app, [
            "process", "https://example.com/blog/cold-email-openers",
            "--skills-dir", str(tmp_path),
            "--write",
        ])
    assert result.exit_code == 0
    index = tmp_path / "cold-email-openers" / "index.ts"
    assert index.exists()
    assert "cold-email-openers" in index.read_text()


@respx.mock
def test_blog_url_no_value_stops_cleanly(tmp_path):
    respx.post("https://api.firecrawl.dev/v1/scrape").mock(
        return_value=httpx.Response(200, json=_FIRECRAWL_RESPONSE)
    )
    no_value_result = {
        "adds_value": False,
        "reason": "Already covered by existing cold-email skill.",
        "relevant_skills": ["cold-email-v2"],
        "action": "no_action",
        "key_insights": [],
    }
    with patch("skillmaker.analyzer.anthropic.Anthropic",
               return_value=_mock_anthropic_client(no_value_result)):
        result = runner.invoke(app, [
            "process", "https://example.com/blog/generic-email-tips",
            "--skills-dir", str(tmp_path),
        ])
    assert result.exit_code == 0
    assert "does not add value" in result.output.lower()
    assert not (tmp_path / "cold-email-openers").exists()
