import pytest
from typer.testing import CliRunner
from unittest.mock import patch
from skillmaker.cli import app
from skillmaker.analyzer import AnalysisResult
from skillmaker.generator import GeneratedSkill

runner = CliRunner()

_NO_VALUE = AnalysisResult(
    adds_value=False,
    reason="Already covered by cold-email-v2.",
    relevant_skills=["cold-email-v2"],
    action="no_action",
    key_insights=[],
)

_ADDS_VALUE = AnalysisResult(
    adds_value=True,
    reason="New pattern interrupt technique.",
    relevant_skills=[],
    action="create_new_skill",
    key_insights=["Use specific metrics"],
)

_MOCK_SKILL = GeneratedSkill(
    slug="test-skill",
    index_ts="export const slug = 'test-skill'",
    refs=[],
    handoff_note="Test handoff.",
)


def test_process_raw_text_no_value(tmp_path):
    with patch("skillmaker.cli.read_all_skills", return_value=[]), \
         patch("skillmaker.cli.analyze_content", return_value=_NO_VALUE):
        result = runner.invoke(app, ["process", "Some generic text", "--skills-dir", str(tmp_path)])
    assert result.exit_code == 0
    assert "does not add value" in result.output.lower()


def test_process_adds_value_shows_bundle(tmp_path):
    with patch("skillmaker.cli.read_all_skills", return_value=[]), \
         patch("skillmaker.cli.analyze_content", return_value=_ADDS_VALUE), \
         patch("skillmaker.cli.generate_skill", return_value=_MOCK_SKILL):
        result = runner.invoke(app, ["process", "Pattern interrupt content", "--skills-dir", str(tmp_path)])
    assert result.exit_code == 0
    assert "test-skill" in result.output
    assert "PASTEABLE BUNDLE" in result.output


def test_process_with_write_creates_files(tmp_path):
    with patch("skillmaker.cli.read_all_skills", return_value=[]), \
         patch("skillmaker.cli.analyze_content", return_value=_ADDS_VALUE), \
         patch("skillmaker.cli.generate_skill", return_value=_MOCK_SKILL):
        result = runner.invoke(app, [
            "process", "Pattern interrupt content",
            "--skills-dir", str(tmp_path),
            "--write",
        ])
    assert result.exit_code == 0
    assert (tmp_path / "test-skill" / "index.ts").exists()


def test_process_no_write_does_not_create_files(tmp_path):
    with patch("skillmaker.cli.read_all_skills", return_value=[]), \
         patch("skillmaker.cli.analyze_content", return_value=_ADDS_VALUE), \
         patch("skillmaker.cli.generate_skill", return_value=_MOCK_SKILL):
        result = runner.invoke(app, ["process", "content", "--skills-dir", str(tmp_path)])
    assert not (tmp_path / "test-skill").exists()
