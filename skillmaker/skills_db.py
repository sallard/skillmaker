import re
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class SkillSummary:
    slug: str
    title: str
    applies_to: list[str]
    covers: list[str]
    body_excerpt: str
    path: Path


def _extract_string(content: str, name: str) -> str:
    m = re.search(rf"export const {name}\s*=\s*'([^']*)'", content)
    return m.group(1) if m else ""


def _extract_array(content: str, name: str) -> list[str]:
    m = re.search(rf"export const {name}\s*=\s*\[([^\]]*)\]", content, re.DOTALL)
    if not m:
        return []
    return re.findall(r"'([^']*)'", m.group(1))


def _extract_template_literal(content: str, name: str) -> str:
    m = re.search(rf"export const {name}\s*=\s*`([\s\S]*?)`", content)
    return m.group(1).strip() if m else ""


def parse_skill_file(content: str, path: Path = Path(".")) -> SkillSummary:
    body = _extract_template_literal(content, "body")
    return SkillSummary(
        slug=_extract_string(content, "slug"),
        title=_extract_string(content, "title"),
        applies_to=_extract_array(content, "applies_to"),
        covers=_extract_array(content, "covers"),
        body_excerpt=body[:500],
        path=path,
    )


def read_all_skills(skills_dir: Path) -> list[SkillSummary]:
    summaries = []
    for index_file in sorted(skills_dir.glob("*/index.ts")):
        content = index_file.read_text()
        summaries.append(parse_skill_file(content, path=index_file))
    return summaries
