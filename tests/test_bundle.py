import pytest
from pathlib import Path
from skillmaker.bundle import format_bundle, write_local_files
from skillmaker.generator import GeneratedSkill, GeneratedRef

_SKILL_WITH_REFS = GeneratedSkill(
    slug="cold-email-openers",
    index_ts="export const slug = 'cold-email-openers'\nexport const body = `# Openers`",
    refs=[
        GeneratedRef(
            slug="opener-patterns",
            content="export const slug = 'opener-patterns'\nexport const body = `# Patterns`"
        )
    ],
    handoff_note="Add import after tests pass."
)

_SKILL_NO_REFS = GeneratedSkill(
    slug="simple-skill",
    index_ts="export const slug = 'simple-skill'",
    refs=[],
)


def test_bundle_contains_index_header():
    bundle = format_bundle(_SKILL_WITH_REFS)
    assert "=== supabase/functions/_shared/chat/kb/skills/cold-email-openers/index.ts ===" in bundle


def test_bundle_contains_index_content():
    bundle = format_bundle(_SKILL_WITH_REFS)
    assert "export const slug = 'cold-email-openers'" in bundle


def test_bundle_contains_ref_header():
    bundle = format_bundle(_SKILL_WITH_REFS)
    assert "=== supabase/functions/_shared/chat/kb/skills/cold-email-openers/refs/opener-patterns.ts ===" in bundle


def test_bundle_contains_handoff_section():
    bundle = format_bundle(_SKILL_WITH_REFS)
    assert "=== HANDOFF ===" in bundle
    assert "Add import after tests pass." in bundle


def test_bundle_contains_import_line():
    bundle = format_bundle(_SKILL_WITH_REFS)
    assert "import * as coldEmailOpeners" in bundle
    assert "SKILLS.push(coldEmailOpeners" in bundle


def test_bundle_no_refs_section_when_empty():
    bundle = format_bundle(_SKILL_NO_REFS)
    assert "refs/" not in bundle


def test_write_local_creates_index(tmp_path):
    write_local_files(_SKILL_WITH_REFS, tmp_path)
    index = tmp_path / "cold-email-openers" / "index.ts"
    assert index.exists()
    assert "cold-email-openers" in index.read_text()


def test_write_local_creates_ref(tmp_path):
    write_local_files(_SKILL_WITH_REFS, tmp_path)
    ref = tmp_path / "cold-email-openers" / "refs" / "opener-patterns.ts"
    assert ref.exists()
    assert "opener-patterns" in ref.read_text()


def test_write_local_no_refs_dir_when_empty(tmp_path):
    write_local_files(_SKILL_NO_REFS, tmp_path)
    assert not (tmp_path / "simple-skill" / "refs").exists()
