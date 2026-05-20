import pytest
from unittest.mock import MagicMock, patch
from skillmaker.analyzer import AnalysisResult, analyze_content
from skillmaker.skills_db import SkillSummary
from pathlib import Path

SAMPLE_SKILLS = [
    SkillSummary(
        slug="cold-email-v2",
        title="Cold Email Mastery",
        applies_to=["sales"],
        covers=["cold email", "subject lines"],
        body_excerpt="## Rules\n- Subject lines: 2-4 words.",
        path=Path("skills/cold-email-v2/index.ts"),
    )
]

_ADDS_VALUE_RESPONSE = {
    "adds_value": True,
    "reason": "Introduces pattern interrupt technique not covered in existing skills.",
    "relevant_skills": ["cold-email-v2"],
    "action": "update_existing",
    "key_insights": ["Use pattern interrupts", "Cite specific metrics"],
}

_NO_VALUE_RESPONSE = {
    "adds_value": False,
    "reason": "Repeats existing cold email rules without new angles.",
    "relevant_skills": ["cold-email-v2"],
    "action": "no_action",
    "key_insights": [],
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


def test_returns_adds_value_true():
    with patch("skillmaker.analyzer.anthropic.Anthropic", return_value=_mock_client(_ADDS_VALUE_RESPONSE)):
        result = analyze_content("Content about pattern interrupts.", SAMPLE_SKILLS)
    assert result.adds_value is True
    assert result.action == "update_existing"
    assert "cold-email-v2" in result.relevant_skills


def test_returns_adds_value_false():
    with patch("skillmaker.analyzer.anthropic.Anthropic", return_value=_mock_client(_NO_VALUE_RESPONSE)):
        result = analyze_content("Generic cold email tips.", SAMPLE_SKILLS)
    assert result.adds_value is False
    assert result.action == "no_action"


def test_returns_analysis_result_dataclass():
    with patch("skillmaker.analyzer.anthropic.Anthropic", return_value=_mock_client(_ADDS_VALUE_RESPONSE)):
        result = analyze_content("Some content.", SAMPLE_SKILLS)
    assert isinstance(result, AnalysisResult)
    assert isinstance(result.key_insights, list)
