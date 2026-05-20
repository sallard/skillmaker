import httpx
from skillmaker.config import RAPIDAPI_KEY
from skillmaker.fetchers.detect import extract_youtube_id

_API_HOST = "youtube-transcriptor.p.rapidapi.com"
_API_URL = f"https://{_API_HOST}/transcript"


def fetch_youtube_transcript(url: str) -> str:
    video_id = extract_youtube_id(url)
    resp = httpx.get(
        _API_URL,
        headers={
            "x-rapidapi-host": _API_HOST,
            "x-rapidapi-key": RAPIDAPI_KEY,
        },
        params={"video_id": video_id, "lang": "en"},
        timeout=30.0,
    )
    resp.raise_for_status()
    segments = resp.json()
    if not segments:
        raise ValueError(f"Empty transcript for video {video_id}")
    return " ".join(seg["text"] for seg in segments if "text" in seg)
