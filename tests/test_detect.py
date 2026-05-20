import pytest
from skillmaker.fetchers.detect import ContentType, detect_content_type, extract_youtube_id


def test_youtube_watch_url():
    assert detect_content_type("https://www.youtube.com/watch?v=dQw4w9WgXcQ") == ContentType.YOUTUBE


def test_youtube_short_url():
    assert detect_content_type("https://youtu.be/dQw4w9WgXcQ") == ContentType.YOUTUBE


def test_linkedin_posts_url():
    assert detect_content_type("https://www.linkedin.com/posts/johndoe_activity-12345/") == ContentType.LINKEDIN


def test_linkedin_feed_update_url():
    assert detect_content_type("https://www.linkedin.com/feed/update/urn:li:activity:12345/") == ContentType.LINKEDIN


def test_tweet_x_domain():
    assert detect_content_type("https://x.com/user/status/123456789") == ContentType.TWEET


def test_tweet_twitter_domain():
    assert detect_content_type("https://twitter.com/user/status/987654321") == ContentType.TWEET


def test_blog_url():
    assert detect_content_type("https://example.com/blog/my-post") == ContentType.BLOG


def test_pdf_local_path():
    assert detect_content_type("/Users/me/Downloads/playbook.pdf") == ContentType.PDF


def test_raw_text():
    assert detect_content_type("This is raw text about cold email strategy.") == ContentType.TEXT


def test_extract_youtube_id_watch():
    assert extract_youtube_id("https://www.youtube.com/watch?v=dQw4w9WgXcQ") == "dQw4w9WgXcQ"


def test_extract_youtube_id_short():
    assert extract_youtube_id("https://youtu.be/dQw4w9WgXcQ") == "dQw4w9WgXcQ"


def test_extract_youtube_id_invalid_raises():
    with pytest.raises(ValueError, match="No YouTube video ID"):
        extract_youtube_id("https://example.com/not-youtube")
