import httpx
from skillmaker.config import FIRECRAWL_API_KEY

_SCRAPE_URL = "https://api.firecrawl.dev/v1/scrape"


def fetch_with_firecrawl(url: str) -> str:
    resp = httpx.post(
        _SCRAPE_URL,
        headers={
            "Authorization": f"Bearer {FIRECRAWL_API_KEY}",
            "Content-Type": "application/json",
        },
        json={"url": url, "formats": ["markdown"]},
        timeout=30.0,
    )
    resp.raise_for_status()
    data = resp.json()
    if not data.get("success"):
        raise RuntimeError(f"Firecrawl failed for {url}: {data}")
    return data["data"]["markdown"]
