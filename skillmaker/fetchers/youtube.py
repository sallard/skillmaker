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
    payload = resp.json()

    # Nested format: {"data": {"transcripts": {"<lang>": {"custom": [{"text": "..."}]}}}}
    inner = payload.get("data", payload)
    transcripts = inner.get("transcripts", {})
    if transcripts:
        lang_data = next(iter(transcripts.values()))
        segments = lang_data.get("custom") or lang_data.get("segments", [])
        if segments:
            title = inner.get("videoInfo", {}).get("name", "")
            body = " ".join(s["text"] for s in segments if s.get("text"))
            return f"{title}\n\n{body}".strip() if title else body

    # Flat format fallback: {"transcript": "...", "summary": "..."}
    text = inner.get("transcript") or inner.get("summary") or inner.get("text", "")
    if not text:
        raise ValueError(f"Empty transcript for video {video_id}")
    return text
