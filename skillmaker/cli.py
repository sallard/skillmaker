import typer
from pathlib import Path
from typing import Optional
from skillmaker.config import SKILLS_DIR
from skillmaker.fetchers import fetch_content
from skillmaker.skills_db import read_all_skills
from skillmaker.analyzer import analyze_content
from skillmaker.generator import generate_skill
from skillmaker.bundle import format_bundle, write_local_files

app = typer.Typer(help="SkillMaker: generate TypeScript kb skills from any content source.")


@app.callback()
def _main() -> None:
    """SkillMaker CLI."""


@app.command()
def process(
    source: str = typer.Argument(..., help="URL, PDF path, or raw text to process"),
    skills_dir: Path = typer.Option(SKILLS_DIR, help="Path to local skills directory"),
    write: bool = typer.Option(False, "--write", help="Write generated files to disk"),
    file: Optional[Path] = typer.Option(None, "--file", help="Path to a PDF file"),
):
    """Fetch content, evaluate against existing skills, and generate or update skill files."""
    actual_source = str(file) if file else source

    typer.echo(f"Fetching content: {actual_source[:80]}...")
    content = fetch_content(actual_source)
    typer.echo(f"Fetched {len(content)} characters.")

    typer.echo(f"Reading existing skills from: {skills_dir}")
    existing = read_all_skills(skills_dir)
    typer.echo(f"Found {len(existing)} existing skill(s).")

    typer.echo("Analyzing value...")
    analysis = analyze_content(content, existing)
    typer.echo(f"Reason: {analysis.reason}")

    if not analysis.adds_value:
        typer.echo("\nThis content does not add value to the existing skills. No files generated.")
        raise typer.Exit(0)

    typer.echo("\nKey insights:")
    for insight in analysis.key_insights:
        typer.echo(f"  - {insight}")

    typer.echo("\nGenerating skill files...")
    relevant = [s for s in existing if s.slug in analysis.relevant_skills]
    skill = generate_skill(content, analysis, relevant)
    typer.echo(f"Generated: {skill.slug} with {len(skill.refs)} ref(s).")

    bundle = format_bundle(skill)
    typer.echo("\n" + "=" * 60)
    typer.echo("PASTEABLE BUNDLE:")
    typer.echo("=" * 60)
    typer.echo(bundle)
    typer.echo("=" * 60)

    if write:
        write_local_files(skill, skills_dir)
        typer.echo(f"\nFiles written to: {skills_dir / skill.slug}/")
    else:
        typer.echo("\nRun with --write to save files to disk.")
