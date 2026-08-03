from unittest.mock import MagicMock, patch
from api_client.client import ApiClient
from exceptions.exceptions import ApiTimeoutError, ApiConnectionError, ApiInvalidUrlError
import pytest
import requests

def test_request_returns_response_from_session():

    client = ApiClient("http://test")

    mock_response = MagicMock()
    mock_response.status_code = 200

    with patch.object(client.session,"request") as mock_request:

        mock_request.return_value = mock_response
        result = client._request("GET","users/1")

        assert result is mock_response

        mock_request.assert_called_once_with(
            method="GET",
            url="http://test/users/1",
            timeout=10,
            json=None,
        )

def test_request_raises_api_timeout_error_on_timeout():

    client = ApiClient("http://test")


    with patch.object(client.session,"request") as mock_request:

        mock_request.side_effect = requests.exceptions.Timeout()
        with pytest.raises(ApiTimeoutError):
            client._request("GET","users/1")

        mock_request.assert_called_once_with(
            method="GET",
            url="http://test/users/1",
            timeout=10,
            json=None,
        )

@pytest.mark.parametrize(
    "request_exception, expected_exception",
    [
        (requests.exceptions.Timeout, ApiTimeoutError),
        (requests.exceptions.ConnectionError, ApiConnectionError),
        (requests.exceptions.InvalidURL, ApiInvalidUrlError),
    ]
)
def test_request_maps_requests_exceptions(request_exception, expected_exception):
    client = ApiClient("http://test")

    with patch.object(client.session,"request") as mock_request:
        mock_request.side_effect = request_exception

        with pytest.raises(expected_exception):
            client._request("GET", "users/1")

        mock_request.assert_called_once_with(
            method="GET",
            url="http://test/users/1",
            timeout=10,
            json=None,
        )

@pytest.mark.parametrize(
    "method_name, endpoint, json_data",
    [
        ("get", "users/1", None),
        ("post", "users/1", {"name": "Kuba","username": "kubix","email": "kubix@gmail.com",}),
        ("put", "users/1", {"name": "Kuba","username": "kubix","email": "kubix@gmail.com",}),
        ("patch", "users/1", {"name": "Kuba","username": "kubix","email": "kubix@gmail.com",}),
        ("delete", "users/1", None),
    ]
)
def test_client_methods_call_request(method_name, endpoint, json_data):
    client = ApiClient("http://test")

    with patch.object(client, "_request") as mock_request:
        mock_request.return_value = MagicMock()
        method = getattr(client, method_name)

        if json_data is None:
            result = method(endpoint)
            mock_request.assert_called_once_with(method_name.upper(), endpoint)
        else:
            result = method(endpoint, json_data)
            mock_request.assert_called_once_with(method_name.upper(), endpoint, json_data)

        assert result is mock_request.return_value
        