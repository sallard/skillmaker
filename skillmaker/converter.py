import re
from pathlib import Path
from skillmaker.generator import GeneratedSkill, GeneratedRef
from skillmaker.skills_db import parse_frontmatter

_STOP_WORDS = {
    "the", "and", "for", "this", "that", "use", "how", "when", "what",
    "ask", "also", "any", "even", "with", "from", "about", "their",
    "into", "who", "are", "all", "has", "its", "not", "but", "can",
    "you", "your", "will", "they", "them", "out", "our", "was", "were",
    "have", "had", "been", "than", "then", "more", "some", "such",
    "always", "trigger", "questions", "user", "skill", "simple",
}

_APPLIES_TO_MAP: list[tuple[str, str]] = [
    ("linkedin", "linkedin_writing"),
    ("cold email", "sales"),
    ("outreach", "sales"),
    ("sales", "sales"),
    ("gmail", "gmail"),
    ("calendar", "calendar"),
    ("schedule", "calendar"),
    ("drive", "drive"),
    ("notion", "notion"),
    ("youtube", "youtube"),
    ("video", "youtube"),
    ("recruit", "hires"),
    ("hires", "hires"),
    ("intent", "intent_discover"),
    ("signal", "intent_discover"),
    ("topic post", "topic_posts"),
    ("chart", "chart"),
    ("graph", "chart"),
    ("business card", "business_card"),
]

_EM_DASH = "—"
_EN_DASH = "–"
_LDQUOTE = "“"
_RDQUOTE = "”"
_LSQUOTE = "‘"
_RSQUOTE = "’"


def _infer_applies_to(text: str) -> list[str]:
    text_lower = text.lower()
    seen: set[str] = set()
    result: list[str] = []
    for keyword, value in _APPLIES_TO_MAP:
        if keyword in text_lower and value not in seen:
            result.append(value)
            seen.add(value)
    return result[:4] or ["sales"]


def _meaningful_words(text: str, max_count: int = 8) -> list[str]:
    words = re.findall(r"\b[a-z][a-z-]{2,}\b", text.lower())
    seen: set[str] = set()
    result: list[str] = []
    for w in words:
        if w not in _STOP_WORDS and w not in seen:
            result.append(w)
            seen.add(w)
        if len(result) == max_count:
            break
    return result


def _sanitize_for_ts(text: str) -> str:
    text = text.replace(_EM_DASH, ", ").replace(_EN_DASH, "-")
    text = text.replace(_LDQUOTE, '"').replace(_RDQUOTE, '"')
    text = text.replace(_LSQUOTE, "'").replace(_RSQUOTE, "'")
    text = text.replace("`", "'")
    return text


def _make_index_ts(
    slug: str,
    description: str,
    applies_to: list[str],
    covers: list[str],
    body: str,
) -> str:
    title = slug.replace("-", " ").title()
    use_when = description.replace("'", "\\'")
    at_list = ", ".join(f"'{a}'" for a in applies_to)
    cv_list = ", ".join(f"'{c}'" for c in covers)
    return (
        f"export const slug = '{slug}'\n"
        f"export const title = '{title}'\n"
        f"export const applies_to = [{at_list}]\n"
        f"export const mode: 'for_generating' | 'for_understanding' | 'mixed' = 'mixed'\n"
        f"export const covers = [{cv_list}]\n"
        f"export const use_when = '{use_when}'\n"
        f"export const body = `\n{body}\n`\n"
    )


def _make_ref_ts(slug: str, body: str) -> str:
    keywords = _meaningful_words(slug.replace("-", " "), max_count=6)
    if not keywords:
        keywords = [slug]
    kw_list = ", ".join(f"'{k}'" for k in keywords)
    return (
        f"export const slug = '{slug}'\n"
        f"export const triggers = {{\n"
        f"  keywords: [{kw_list}]\n"
        f"}}\n"
        f"export const body = `\n{body}\n`\n"
    )


def convert_skill_md(skill_dir: Path) -> GeneratedSkill:
    raw = (skill_dir / "SKILL.md").read_text()
    meta, md_body = parse_frontmatter(raw)

    slug = meta.get("name", skill_dir.name)
    description = meta.get("description", "")

    applies_to = _infer_applies_to(description + " " + md_body[:300])
    covers = _meaningful_words(description)

    body_safe = _sanitize_for_ts(md_body[:2500])
    index_ts = _make_index_ts(slug, description, applies_to, covers, body_safe)

    refs: list[GeneratedRef] = []
    refs_dir = skill_dir / "references"
    if refs_dir.exists():
        for ref_file in sorted(refs_dir.glob("*.md")):
            ref_body = _sanitize_for_ts(ref_file.read_text()[:2500])
            refs.append(GeneratedRef(
                slug=ref_file.stem,
                content=_make_ref_ts(ref_file.stem, ref_body),
            ))

    return GeneratedSkill(slug=slug, index_ts=index_ts, refs=refs)
