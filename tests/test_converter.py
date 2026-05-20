import pytest
from pathlib import Path
from skillmaker.converter import convert_skill_md, _sanitize_for_ts, _infer_applies_to

SKILL_MD = """\
---
name: linkedin-content-strategy
description: Plan LinkedIn content strategy, content calendars, and sales pipeline.
---

# LinkedIn Content Strategy

Strategic content planning for founders using LinkedIn as pipeline infrastructure.

## Rules
- Post 3-4x per week.
- Alternate TOF, MOF, BOF posts.
"""

REF_ICP_MD = """\
# ICP Definition

- Role: CMO, VP Marketing
- Industry: Luxury fashion
"""


def _make_skill_dir(tmp_path: Path) -> Path:
    skill_dir = tmp_path / "linkedin-content-strategy"
    skill_dir.mkdir()
    (skill_dir / "SKILL.md").write_text(SKILL_MD)
    refs_dir = skill_dir / "references"
    refs_dir.mkdir()
    (refs_dir / "icp-and-pillars.md").write_text(REF_ICP_MD)
    return skill_dir


def test_convert_slug(tmp_path):
    skill = convert_skill_md(_make_skill_dir(tmp_path))
    assert skill.slug == "linkedin-content-strategy"


def test_convert_index_ts_has_slug(tmp_path):
    skill = convert_skill_md(_make_skill_dir(tmp_path))
    assert "export const slug = 'linkedin-content-strategy'" in skill.index_ts


def test_convert_index_ts_has_title(tmp_path):
    skill = convert_skill_md(_make_skill_dir(tmp_path))
    assert "export const title = 'Linkedin Content Strategy'" in skill.index_ts


def test_convert_index_ts_has_applies_to_linkedin(tmp_path):
    skill = convert_skill_md(_make_skill_dir(tmp_path))
    assert "linkedin_writing" in skill.index_ts


def test_convert_index_ts_has_mode(tmp_path):
    skill = convert_skill_md(_make_skill_dir(tmp_path))
    assert "export const mode:" in skill.index_ts


def test_convert_index_ts_has_use_when(tmp_path):
    skill = convert_skill_md(_make_skill_dir(tmp_path))
    assert "export const use_when" in skill.index_ts


def test_convert_index_ts_body_contains_content(tmp_path):
    skill = convert_skill_md(_make_skill_dir(tmp_path))
    assert "LinkedIn Content Strategy" in skill.index_ts


def test_convert_generates_one_ref(tmp_path):
    skill = convert_skill_md(_make_skill_dir(tmp_path))
    assert len(skill.refs) == 1
    assert skill.refs[0].slug == "icp-and-pillars"


def test_convert_ref_has_triggers(tmp_path):
    skill = convert_skill_md(_make_skill_dir(tmp_path))
    assert "triggers" in skill.refs[0].content
    assert "keywords" in skill.refs[0].content


def test_convert_ref_body_contains_content(tmp_path):
    skill = convert_skill_md(_make_skill_dir(tmp_path))
    assert "CMO" in skill.refs[0].content


def test_convert_no_refs_when_no_references_dir(tmp_path):
    skill_dir = tmp_path / "simple-skill"
    skill_dir.mkdir()
    (skill_dir / "SKILL.md").write_text(SKILL_MD)
    skill = convert_skill_md(skill_dir)
    assert skill.refs == []


def test_sanitize_replaces_em_dash():
    assert "—" not in _sanitize_for_ts("foo — bar")
    assert ", " in _sanitize_for_ts("foo — bar")


def test_sanitize_replaces_backtick():
    assert "`" not in _sanitize_for_ts("use `code` here")


def test_infer_applies_to_linkedin():
    assert "linkedin_writing" in _infer_applies_to("LinkedIn content strategy")


def test_infer_applies_to_sales():
    assert "sales" in _infer_applies_to("cold outreach and sales pipeline")


def test_infer_applies_to_defaults_to_sales():
    assert _infer_applies_to("something completely unrelated") == ["sales"]
