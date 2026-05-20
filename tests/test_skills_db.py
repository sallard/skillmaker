import pytest
from pathlib import Path
from skillmaker.skills_db import SkillSummary, parse_skill_file, read_all_skills

SAMPLE_INDEX_TS = """
export const slug = 'cold-email-v2'
export const title = 'Cold Email Mastery'
export const applies_to = ['sales', 'gmail']
export const mode: 'for_generating' | 'for_understanding' | 'mixed' = 'for_generating'
export const covers = ['cold email', 'subject lines', 'permission CTA']
export const use_when = 'Use when the user wants to draft a cold email.'
export const body = `# Cold Email Mastery

## Rules
- Subject lines: 2-4 words.
- Body: 60-90 words.
`
"""


def test_parse_slug():
    assert parse_skill_file(SAMPLE_INDEX_TS).slug == "cold-email-v2"


def test_parse_title():
    assert parse_skill_file(SAMPLE_INDEX_TS).title == "Cold Email Mastery"


def test_parse_applies_to():
    assert parse_skill_file(SAMPLE_INDEX_TS).applies_to == ["sales", "gmail"]


def test_parse_covers():
    assert "cold email" in parse_skill_file(SAMPLE_INDEX_TS).covers


def test_parse_body_excerpt_contains_heading():
    assert "Cold Email Mastery" in parse_skill_file(SAMPLE_INDEX_TS).body_excerpt


def test_read_all_skills_finds_one(tmp_path):
    skill_dir = tmp_path / "cold-email-v2"
    skill_dir.mkdir()
    (skill_dir / "index.ts").write_text(SAMPLE_INDEX_TS)
    skills = read_all_skills(tmp_path)
    assert len(skills) == 1
    assert skills[0].slug == "cold-email-v2"


def test_read_all_skills_empty_dir(tmp_path):
    assert read_all_skills(tmp_path) == []


def test_read_all_skills_ignores_non_index_files(tmp_path):
    skill_dir = tmp_path / "cold-email-v2"
    skill_dir.mkdir()
    (skill_dir / "index.ts").write_text(SAMPLE_INDEX_TS)
    (skill_dir / "other.ts").write_text("// not a skill")
    assert len(read_all_skills(tmp_path)) == 1
