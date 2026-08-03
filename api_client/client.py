import logging

import requests

from exceptions.exceptions import (
    ApiConnectionError,
    ApiInvalidUrlError,
    ApiTimeoutError,
)

logger = logging.getLogger(__name__)


class ApiClient:
    def __init__(
        self,
        base_url: str,
        token: str | None = None,
        timeout: int = 10,
    ):
        self.session = requests.Session()
        self.timeout = timeout
        self.base_url = base_url.rstrip("/")

        self.session.headers.update({
            "Accept": "application/json",
            "Content-Type": "application/json",
        })

        if token:
            self.set_token(token)

    def set_token(self, token: str) -> None:
        self.session.headers.update({
            "Authorization": f"Bearer {token}",
        })

    def _request(
        self,
        method: str,
        endpoint: str,
        json_data: dict | list | None = None,
    ) -> requests.Response:
        endpoint = endpoint.lstrip("/")
        method = method.upper()
        url = f"{self.base_url}/{endpoint}"
        logger.debug(
            "Sending %s request to %s",
            method,
            url,
        )
        try:
            response = self.session.request(
                method=method,
                url=url,
                timeout=self.timeout,
                json=json_data,
            )

            logger.debug(
                "Received response: %s %s -> %s",
                method,
                url,
                response.status_code,
            )

        except requests.exceptions.Timeout as e:
            raise ApiTimeoutError(method, url) from e

        except requests.exceptions.InvalidURL as e:
            raise ApiInvalidUrlError(method, url) from e

        except requests.exceptions.ConnectionError as e:
            raise ApiConnectionError(method, url) from e

        return response

    def get(self, endpoint: str) -> requests.Response:
        return self._request("GET", endpoint)

    def post(
        self,
        endpoint: str,
        json_data: dict | list,
    ) -> requests.Response:
        return self._request("POST", endpoint, json_data)

    def put(
        self,
        endpoint: str,
        json_data: dict | list,
    ) -> requests.Response:
        return self._request("PUT", endpoint, json_data)

    def patch(
        self,
        endpoint: str,
        json_data: dict | list,
    ) -> requests.Response:
        return self._request("PATCH", endpoint, json_data)

    def delete(self, endpoint: str) -> requests.Response:
        return self._request("DELETE", endpoint)