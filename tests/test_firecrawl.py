import httpx
import json
import pytest
from unittest.mock import patch, MagicMock
from skillmaker.fetchers.firecrawl import fetch_with_firecrawl


def test_returns_markdown():
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "success": True,
        "data": {"markdown": "# My Post\n\nGreat content."}
    }

    with patch("skillmaker.fetchers.firecrawl.httpx.post", return_value=mock_response):
        result = fetch_with_firecrawl("https://example.com/blog/post")
        assert result == "# My Post\n\nGreat content."


def test_raises_on_firecrawl_failure():
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "success": False,
        "error": "URL not reachable"
    }

    with patch("skillmaker.fetchers.firecrawl.httpx.post", return_value=mock_response):
        with pytest.raises(RuntimeError, match="Firecrawl failed"):
            fetch_with_firecrawl("https://example.com/broken")


def test_raises_on_http_error():
    mock_response = MagicMock()
    mock_response.raise_for_status.side_effect = httpx.HTTPStatusError("401", request=MagicMock(), response=MagicMock())

    with patch("skillmaker.fetchers.firecrawl.httpx.post", return_value=mock_response):
        with pytest.raises(httpx.HTTPStatusError):
            fetch_with_firecrawl("https://example.com/blog/post")


def test_sends_correct_payload():
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "success": True,
        "data": {"markdown": "content"}
    }

    with patch("skillmaker.fetchers.firecrawl.httpx.post", return_value=mock_response) as mock_post:
        fetch_with_firecrawl("https://example.com/my-page")

        # Verify the call
        mock_post.assert_called_once()
        call_kwargs = mock_post.call_args[1]

        # Verify the json payload
        body = call_kwargs["json"]
        assert body["url"] == "https://example.com/my-page"
        assert "markdown" in body["formats"]
