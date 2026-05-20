import os

# Must run before any skillmaker module is imported by pytest during collection.
os.environ.setdefault("ANTHROPIC_API_KEY", "sk-ant-test")
os.environ.setdefault("FIRECRAWL_API_KEY", "fc-test")
os.environ.setdefault("RAPIDAPI_KEY", "rapid-test")
os.environ.setdefault("HARVEST_API_KEY", "harvest-test")
os.environ.setdefault("SKILLS_DIR", "/tmp/test_skills")
os.environ.setdefault("CLAUDE_MODEL", "claude-haiku-4-5-20251001")
