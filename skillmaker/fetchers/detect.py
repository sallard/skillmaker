import re
from enum import Enum


class ContentType(Enum):
    YOUTUBE = "youtube"
    LINKEDIN = "linkedin"
    TWEET = "tweet"
    BLOG = "blog"
    PDF = "pdf"
    TEXT = "text"


_YOUTUBE_RE = re.compile(r'(?:youtube\.com/watch\?v=|youtu\.be/)([A-Za-z0-9_-]{11})')
_LINKEDIN_POST_RE = re.compile(r'linkedin\.com/(?:posts|feed/update)/')
_TWEET_RE = re.compile(r'(?:twitter\.com|x\.com)/\w+/status/\d+')


def detect_content_type(source: str) -> ContentType:
    if source.lower().endswith('.pdf') and not source.startswith('http'):
        return ContentType.PDF
    if _YOUTUBE_RE.search(source):
        return ContentType.YOUTUBE
    if _LINKEDIN_POST_RE.search(source):
        return ContentType.LINKEDIN
    if _TWEET_RE.search(source):
        return ContentType.TWEET
    if source.startswith('http'):
        return ContentType.BLOG
    return ContentType.TEXT


def extract_youtube_id(url: str) -> str:
    m = _YOUTUBE_RE.search(url)
    if not m:
        raise ValueError(f"No YouTube video ID found in: {url}")
    return m.group(1)
