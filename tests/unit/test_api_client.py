from unittest.mock import MagicMock, patch
from api_client.client import ApiClient
from exceptions.exceptions import ApiTimeoutError
import pytest
import requests

def test_request_returns_response_from_session():

    client = ApiClient("http://test")

    mock_response = MagicMock()
    mock_response.status_code = 200

    with patch.object(client.session,"request") as mock_request:

        mock_request.return_value = mock_response
        result = client._request("GET","users/1")

        mock_request.assert_called_once()
        assert result is mock_response


def test_request_raises_api_timeout_error_on_timeout():

    client = ApiClient("http://test")


    with patch.object(client.session,"request") as mock_request:

        mock_request.side_effect = requests.exceptions.Timeout()
        with pytest.raises(ApiTimeoutError):
            client._request("GET","users/1")

        mock_request.assert_called_once()