import re
from dataclasses import dataclass
from pathlib import Path


@dataclass
class SkillSummary:
    slug: str
    title: str
    applies_to: list[str]
    covers: list[str]
    body_excerpt: str
    path: Path


# ── TypeScript index.ts format ────────────────────────────────────────────────

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


# ── Markdown SKILL.md format ──────────────────────────────────────────────────

def parse_frontmatter(content: str) -> tuple[dict[str, str], str]:
    m = re.match(r"^---\n([\s\S]*?)\n---\n([\s\S]*)$", content.strip())
    if not m:
        return {}, content
    meta: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            key, _, val = line.partition(":")
            meta[key.strip()] = val.strip()
    return meta, m.group(2).strip()


def parse_skill_md(content: str, path: Path = Path(".")) -> SkillSummary:
    meta, body = parse_frontmatter(content)
    slug = meta.get("name", path.parent.name)
    description = meta.get("description", "")
    words = re.findall(r"\b[a-z][a-z_]{2,}\b", description.lower())
    covers = list(dict.fromkeys(words))[:8]
    return SkillSummary(
        slug=slug,
        title=slug.replace("-", " ").title(),
        applies_to=[],
        covers=covers,
        body_excerpt=body[:500],
        path=path,
    )


# ── Directory reader ──────────────────────────────────────────────────────────

def read_all_skills(skills_dir: Path) -> list[SkillSummary]:
    summaries = []
    seen: set[str] = set()
    for index_file in sorted(skills_dir.glob("*/index.ts")):
        content = index_file.read_text()
        s = parse_skill_file(content, path=index_file)
        seen.add(s.slug)
        summaries.append(s)
    for skill_md in sorted(skills_dir.glob("*/SKILL.md")):
        content = skill_md.read_text()
        s = parse_skill_md(content, path=skill_md)
        if s.slug not in seen:
            summaries.append(s)
    return summaries
