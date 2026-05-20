import anthropic
from dataclasses import dataclass, field
from skillmaker.config import ANTHROPIC_API_KEY, CLAUDE_MODEL
from skillmaker.skills_db import SkillSummary

_ANALYZE_TOOL = {
    "name": "analyze_content",
    "description": "Analyze whether submitted content adds value to the existing skill library.",
    "input_schema": {
        "type": "object",
        "properties": {
            "adds_value": {
                "type": "boolean",
                "description": "True if the content introduces knowledge not already covered."
            },
            "reason": {
                "type": "string",
                "description": "One sentence explaining the decision."
            },
            "relevant_skills": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Slugs of existing skills this content relates to."
            },
            "action": {
                "type": "string",
                "enum": ["create_new_skill", "update_existing", "no_action"],
                "description": "What to do with this content."
            },
            "key_insights": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Specific new insights extracted from the content."
            }
        },
        "required": ["adds_value", "reason", "relevant_skills", "action", "key_insights"]
    }
}


@dataclass
class AnalysisResult:
    adds_value: bool
    reason: str
    relevant_skills: list[str]
    action: str
    key_insights: list[str] = field(default_factory=list)


def _build_skills_summary(skills: list[SkillSummary]) -> str:
    if not skills:
        return "No existing skills."
    lines = []
    for s in skills:
        lines.append(f"- slug={s.slug}, title={s.title}, covers={s.covers}")
        lines.append(f"  body excerpt: {s.body_excerpt[:200]}")
    return "\n".join(lines)


def analyze_content(content: str, existing_skills: list[SkillSummary]) -> AnalysisResult:
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    skills_summary = _build_skills_summary(existing_skills)
    message = client.messages.create(
        model=CLAUDE_MODEL,
        max_tokens=1024,
        tools=[_ANALYZE_TOOL],
        tool_choice={"type": "tool", "name": "analyze_content"},
        messages=[{
            "role": "user",
            "content": (
                f"Existing skills in the library:\n{skills_summary}\n\n"
                f"New content to evaluate:\n{content[:4000]}\n\n"
                "Does this content add meaningful new knowledge not already covered by the existing skills?"
            )
        }]
    )
    tool_block = next(b for b in message.content if b.type == "tool_use")
    data = tool_block.input
    return AnalysisResult(
        adds_value=data["adds_value"],
        reason=data["reason"],
        relevant_skills=data["relevant_skills"],
        action=data["action"],
        key_insights=data.get("key_insights", []),
    )
