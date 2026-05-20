import tempfile
import httpx
from skillmaker.config import HARVEST_API_KEY

_API_URL = "https://api.harvest-api.com/linkedin/post"


def fetch_linkedin_post(url: str) -> dict:
    """Returns {"text": str, "image_paths": list[str]}"""
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

    image_paths = []
    for img in element.get("postImages", []):
        img_url = img.get("url", "")
        if not img_url:
            continue
        img_resp = httpx.get(img_url, timeout=30.0, follow_redirects=True)
        img_resp.raise_for_status()
        content_type = img_resp.headers.get("content-type", "")
        suffix = ".png" if "png" in content_type else ".jpg"
        with tempfile.NamedTemporaryFile(suffix=suffix, delete=False) as f:
            f.write(img_resp.content)
            image_paths.append(f.name)

    return {
        "text": f"Author: {author}\n\n{text}",
        "image_paths": image_paths,
    }
