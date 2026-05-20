import anthropic
from dataclasses import dataclass, field
from skillmaker.config import ANTHROPIC_API_KEY, CLAUDE_MODEL
from skillmaker.analyzer import AnalysisResult
from skillmaker.skills_db import SkillSummary

_SPEC_RULES = """
SKILL AUTHORING RULES (follow exactly):
1. slug: kebab-case, matches folder name.
2. title: Title Case, <= 60 chars.
3. applies_to: pick from: sales, linkedin_writing, gmail, calendar, drive, notion, youtube, hires, intent_discover, topic_posts, chart, business_card.
4. mode annotation MUST be the full union: 'for_generating' | 'for_understanding' | 'mixed' = '...'.
5. body: Markdown, ## Rules (5-10 imperative bullets) + ## Anti-patterns (3-6 bullets). Optional ## Structure section.
6. Skill body must stay under 700 tokens (~2800 chars). Move heavy detail to refs.
7. Each ref needs triggers.keywords (3-8 lowercase strings). Ref body <= 2500 tokens.
8. NO em-dashes anywhere. Use comma+space instead. ASCII quotes only. No backticks inside template literals.
9. Voice: imperative bullets, second person, present tense. No marketing language.
10. covers: 3-8 lowercase subject tags. use_when: one prose sentence.
"""

_GENERATE_TOOL = {
    "name": "generate_skill",
    "description": "Generate TypeScript skill files following the kb-skill-authoring-spec.",
    "input_schema": {
        "type": "object",
        "properties": {
            "skill_slug": {"type": "string"},
            "index_ts": {"type": "string", "description": "Full TypeScript content of index.ts"},
            "refs": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "slug": {"type": "string"},
                        "content": {"type": "string", "description": "Full TypeScript content of the ref file"}
                    },
                    "required": ["slug", "content"]
                }
            },
            "handoff_note": {"type": "string"}
        },
        "required": ["skill_slug", "index_ts", "refs", "handoff_note"]
    }
}


@dataclass
class GeneratedRef:
    slug: str
    content: str


@dataclass
class GeneratedSkill:
    slug: str
    index_ts: str
    refs: list[GeneratedRef] = field(default_factory=list)
    handoff_note: str = ""


def generate_skill(
    content: str,
    analysis: AnalysisResult,
    existing_skills: list[SkillSummary],
) -> GeneratedSkill:
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    relevant_bodies = "\n\n".join(
        f"=== {s.slug}/index.ts ===\n{s.body_excerpt}"
        for s in existing_skills
        if s.slug in analysis.relevant_skills
    )
    message = client.messages.create(
        model=CLAUDE_MODEL,
        max_tokens=4096,
        tools=[_GENERATE_TOOL],
        tool_choice={"type": "tool", "name": "generate_skill"},
        messages=[{
            "role": "user",
            "content": (
                f"{_SPEC_RULES}\n\n"
                f"Action: {analysis.action}\n"
                f"Key insights from content: {analysis.key_insights}\n\n"
                f"Existing relevant skill files:\n{relevant_bodies or 'None'}\n\n"
                f"Source content:\n{content[:6000]}\n\n"
                "Generate complete TypeScript skill files. "
                "If updating an existing skill, include the full updated index.ts. "
                "Split heavy detail into refs with distinct triggers."
            )
        }]
    )
    tool_block = next((b for b in message.content if b.type == "tool_use"), None)
    if tool_block is None:
        raise RuntimeError("Claude did not return a tool_use block — check your API key and model name")
    data = tool_block.input
    refs = [GeneratedRef(slug=r["slug"], content=r["content"]) for r in data.get("refs", [])]
    return GeneratedSkill(
        slug=data["skill_slug"],
        index_ts=data["index_ts"],
        refs=refs,
        handoff_note=data.get("handoff_note", ""),
    )
