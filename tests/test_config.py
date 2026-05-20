import importlib
import pytest


def test_config_loads_keys_from_env(monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-ant-test")
    monkeypatch.setenv("FIRECRAWL_API_KEY", "fc-test")
    monkeypatch.setenv("RAPIDAPI_KEY", "rapid-test")
    monkeypatch.setenv("HARVEST_API_KEY", "harvest-test")
    monkeypatch.setenv("SKILLS_DIR", "/tmp/skills")
    monkeypatch.setenv("CLAUDE_MODEL", "claude-haiku-4-5-20251001")

    import skillmaker.config as cfg
    importlib.reload(cfg)

    assert cfg.ANTHROPIC_API_KEY == "sk-ant-test"
    assert cfg.FIRECRAWL_API_KEY == "fc-test"
    assert cfg.RAPIDAPI_KEY == "rapid-test"
    assert cfg.HARVEST_API_KEY == "harvest-test"
    assert str(cfg.SKILLS_DIR) == "/tmp/skills"
    assert cfg.CLAUDE_MODEL == "claude-haiku-4-5-20251001"


def test_config_skills_dir_default(monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "x")
    monkeypatch.setenv("FIRECRAWL_API_KEY", "x")
    monkeypatch.setenv("RAPIDAPI_KEY", "x")
    monkeypatch.setenv("HARVEST_API_KEY", "x")
    monkeypatch.delenv("SKILLS_DIR", raising=False)
    monkeypatch.delenv("CLAUDE_MODEL", raising=False)

    import skillmaker.config as cfg
    importlib.reload(cfg)

    assert "skills" in str(cfg.SKILLS_DIR)
    assert cfg.CLAUDE_MODEL == "claude-opus-4-7"
