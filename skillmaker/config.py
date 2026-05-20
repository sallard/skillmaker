from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

ANTHROPIC_API_KEY: str = os.environ["ANTHROPIC_API_KEY"]
FIRECRAWL_API_KEY: str = os.environ["FIRECRAWL_API_KEY"]
RAPIDAPI_KEY: str = os.environ["RAPIDAPI_KEY"]
HARVEST_API_KEY: str = os.environ["HARVEST_API_KEY"]
SKILLS_DIR: Path = Path(os.environ.get("SKILLS_DIR", "supabase/functions/_shared/chat/kb/skills"))
CLAUDE_MODEL: str = os.environ.get("CLAUDE_MODEL", "claude-sonnet-4-6")
