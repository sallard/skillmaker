import httpx
import pytest
from unittest.mock import patch, MagicMock
from skillmaker.fetchers.youtube import fetch_youtube_transcript


def test_returns_joined_transcript():
    mock_response = MagicMock()
    mock_response.json.return_value = [
        {"text": "Hello world.", "start": 0.0},
        {"text": "This is a test.", "start": 2.5},
    ]

    with patch("skillmaker.fetchers.youtube.httpx.get", return_value=mock_response):
        result = fetch_youtube_transcript("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        assert result == "Hello world. This is a test."


def test_raises_on_http_error():
    mock_response = MagicMock()
    mock_response.raise_for_status.side_effect = httpx.HTTPStatusError("403", request=MagicMock(), response=MagicMock())

    with patch("skillmaker.fetchers.youtube.httpx.get", return_value=mock_response):
        with pytest.raises(httpx.HTTPStatusError):
            fetch_youtube_transcript("https://www.youtube.com/watch?v=dQw4w9WgXcQ")


def test_raises_on_empty_transcript():
    mock_response = MagicMock()
    mock_response.json.return_value = []

    with patch("skillmaker.fetchers.youtube.httpx.get", return_value=mock_response):
        with pytest.raises(ValueError, match="Empty transcript"):
            fetch_youtube_transcript("https://www.youtube.com/watch?v=dQw4w9WgXcQ")


def test_raises_on_invalid_url():
    with pytest.raises(ValueError, match="No YouTube video ID"):
        fetch_youtube_transcript("https://example.com/not-youtube")
