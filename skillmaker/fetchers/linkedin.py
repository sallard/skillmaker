import httpx
from skillmaker.config import HARVEST_API_KEY

_API_URL = "https://api.harvest-api.com/linkedin/post"


def fetch_linkedin_post(url: str) -> str:
    resp = httpx.get(
        _API_URL,
        headers={"X-API-Key": HARVEST_API_KEY},
        params={"url": url},
        timeout=30.0,
    )
    resp.raise_for_status()
    element = resp.json().get("element", {})
    text = element.get("content", "")
    if not text:
        raise ValueError(f"Empty post returned for {url}")
    author = element.get("author", {}).get("name", "Unknown")
    return f"Author: {author}\n\n{text}"
