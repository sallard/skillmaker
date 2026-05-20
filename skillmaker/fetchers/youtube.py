import httpx
from skillmaker.config import RAPIDAPI_KEY
from skillmaker.fetchers.detect import extract_youtube_id

_API_HOST = "youtube-video-summarizer-gpt-ai.p.rapidapi.com"
_API_URL = f"https://{_API_HOST}/api/v1/get-transcript-v2"


def fetch_youtube_transcript(url: str) -> str:
    video_id = extract_youtube_id(url)
    resp = httpx.get(
        _API_URL,
        headers={
            "x-rapidapi-host": _API_HOST,
            "x-rapidapi-key": RAPIDAPI_KEY,
        },
        params={"video_id": video_id, "platform": "youtube"},
        timeout=30.0,
    )
    resp.raise_for_status()
    data = resp.json()
    text = data.get("transcript") or data.get("summary") or data.get("text", "")
    if not text:
        raise ValueError(f"Empty transcript for video {video_id}")
    return text
