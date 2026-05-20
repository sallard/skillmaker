import httpx
import pytest
from unittest.mock import patch, MagicMock
from skillmaker.fetchers.linkedin import fetch_linkedin_post

_POST_URL = "https://www.linkedin.com/posts/johndoe_activity-123/"


def test_returns_post_text():
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "author": {"name": "John Doe"},
        "text": "This is my LinkedIn post content about cold emailing.",
    }

    with patch("skillmaker.fetchers.linkedin.httpx.get", return_value=mock_response):
        result = fetch_linkedin_post(_POST_URL)
        assert "This is my LinkedIn post content" in result
        assert "John Doe" in result


def test_raises_on_http_error():
    mock_response = MagicMock()
    mock_response.raise_for_status.side_effect = httpx.HTTPStatusError("401", request=MagicMock(), response=MagicMock())

    with patch("skillmaker.fetchers.linkedin.httpx.get", return_value=mock_response):
        with pytest.raises(httpx.HTTPStatusError):
            fetch_linkedin_post(_POST_URL)


def test_raises_on_empty_text():
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "author": {"name": "Jane"}, "text": ""
    }

    with patch("skillmaker.fetchers.linkedin.httpx.get", return_value=mock_response):
        with pytest.raises(ValueError, match="Empty post"):
            fetch_linkedin_post(_POST_URL)


def test_sends_url_as_query_param():
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "author": {"name": "Jane"}, "text": "content",
    }

    with patch("skillmaker.fetchers.linkedin.httpx.get", return_value=mock_response) as mock_get:
        fetch_linkedin_post(_POST_URL)
        
        # Verify the call
        mock_get.assert_called_once()
        call_kwargs = mock_get.call_args[1]
        assert call_kwargs["params"]["url"] == _POST_URL
