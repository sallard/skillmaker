from pathlib import Path
from skillmaker.generator import GeneratedSkill

_KB_BASE = "supabase/functions/_shared/chat/kb/skills"


def format_bundle(skill: GeneratedSkill) -> str:
    lines: list[str] = []
    lines.append(f"=== {_KB_BASE}/{skill.slug}/index.ts ===")
    lines.append(skill.index_ts)
    lines.append("")
    for ref in skill.refs:
        lines.append(f"=== {_KB_BASE}/{skill.slug}/refs/{ref.slug}.ts ===")
        lines.append(ref.content)
        lines.append("")
    camel = _to_camel(skill.slug)
    lines.append("=== HANDOFF ===")
    lines.append(f"Skill: {skill.slug}")
    lines.append(f"Files to apply: {1 + len(skill.refs)}")
    lines.append("After tests pass, add to kb/index.ts:")
    lines.append(f"  import * as {camel} from './skills/{skill.slug}/index.ts'")
    lines.append(f"  SKILLS.push({camel} as Skill)")
    if skill.handoff_note:
        lines.append(f"\nNote: {skill.handoff_note}")
    return "\n".join(lines)


def write_local_files(skill: GeneratedSkill, skills_dir: Path) -> None:
    skills_dir = skills_dir.resolve()
    skill_dir = (skills_dir / skill.slug).resolve()
    if not str(skill_dir).startswith(str(skills_dir)):
        raise ValueError(f"Unsafe skill slug: {skill.slug!r}")
    skill_dir.mkdir(parents=True, exist_ok=True)
    (skill_dir / "index.ts").write_text(skill.index_ts)
    if skill.refs:
        refs_dir = skill_dir / "refs"
        refs_dir.mkdir(exist_ok=True)
        for ref in skill.refs:
            ref_path = (refs_dir / f"{ref.slug}.ts").resolve()
            if not str(ref_path).startswith(str(refs_dir)):
                raise ValueError(f"Unsafe ref slug: {ref.slug!r}")
            ref_path.write_text(ref.content)


def _to_camel(kebab: str) -> str:
    parts = kebab.split("-")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])
