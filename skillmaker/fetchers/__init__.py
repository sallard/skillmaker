from .detect import ContentType, detect_content_type
from .firecrawl import fetch_with_firecrawl
from .youtube import fetch_youtube_transcript
from .linkedin import fetch_linkedin_post
from .pdf import extract_pdf_text


def fetch_content(source: str) -> str:
    """Route a URL, PDF path, or raw text to the correct fetcher."""
    content_type = detect_content_type(source)
    if content_type == ContentType.YOUTUBE:
        return fetch_youtube_transcript(source)
    if content_type == ContentType.LINKEDIN:
        return fetch_linkedin_post(source)
    if content_type in (ContentType.TWEET, ContentType.BLOG):
        return fetch_with_firecrawl(source)
    if content_type == ContentType.PDF:
        return extract_pdf_text(source)
    return source  # ContentType.TEXT: return as-is
