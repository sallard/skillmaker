import pytest
from unittest.mock import MagicMock, patch
from skillmaker.generator import GeneratedSkill, GeneratedRef, generate_skill
from skillmaker.analyzer import AnalysisResult
from skillmaker.skills_db import SkillSummary
from pathlib import Path

SAMPLE_ANALYSIS = AnalysisResult(
    adds_value=True,
    reason="Introduces pattern interrupt technique.",
    relevant_skills=[],
    action="create_new_skill",
    key_insights=["Use specific metrics in openers", "Pattern interrupts outperform compliments"],
)

_MOCK_TOOL_RESULT = {
    "skill_slug": "cold-email-openers",
    "index_ts": (
        "export const slug = 'cold-email-openers'\n"
        "export const title = 'Cold Email Openers'\n"
        "export const applies_to = ['sales']\n"
        "export const mode: 'for_generating' | 'for_understanding' | 'mixed' = 'for_generating'\n"
        "export const covers = ['opener', 'pattern interrupt']\n"
        "export const use_when = 'Use when drafting cold email opening lines.'\n"
        "export const body = `# Cold Email Openers\n\n## Rules\n- Open with a specific observation.\n`"
    ),
    "refs": [
        {
            "slug": "opener-patterns",
            "content": (
                "export const slug = 'opener-patterns'\n"
                "export const title = 'Opener Patterns'\n"
                "export const triggers = { keywords: ['opener', 'first line', 'hook'] }\n"
                "export const body = `# Opener Patterns\n- Pattern interrupt: cite one metric.\n`"
            )
        }
    ],
    "handoff_note": "Add import and SKILLS.push() after tests pass."
}


def _mock_client(tool_input: dict):
    mock_client = MagicMock()
    mock_message = MagicMock()
    mock_block = MagicMock()
    mock_block.type = "tool_use"
    mock_block.input = tool_input
    mock_message.content = [mock_block]
    mock_client.messages.create.return_value = mock_message
    return mock_client


def test_returns_generated_skill():
    with patch("skillmaker.generator.anthropic.Anthropic", return_value=_mock_client(_MOCK_TOOL_RESULT)):
        result = generate_skill("Content about pattern interrupts.", SAMPLE_ANALYSIS, [])
    assert isinstance(result, GeneratedSkill)
    assert result.slug == "cold-email-openers"


def test_index_ts_contains_slug():
    with patch("skillmaker.generator.anthropic.Anthropic", return_value=_mock_client(_MOCK_TOOL_RESULT)):
        result = generate_skill("Content.", SAMPLE_ANALYSIS, [])
    assert "cold-email-openers" in result.index_ts


def test_refs_populated():
    with patch("skillmaker.generator.anthropic.Anthropic", return_value=_mock_client(_MOCK_TOOL_RESULT)):
        result = generate_skill("Content.", SAMPLE_ANALYSIS, [])
    assert len(result.refs) == 1
    assert result.refs[0].slug == "opener-patterns"
    assert isinstance(result.refs[0], GeneratedRef)
