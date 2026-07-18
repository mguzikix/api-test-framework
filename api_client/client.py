import requests


class ApiClient:
    def __init__(
        self,
        base_url: str,
        token: str | None = None,
        timeout: int = 10,
    ):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.token = token
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        if token:
            self.headers["Authorization"] = f"Bearer {token}"

    def set_token(self, token: str) -> None:
        self.token = token
        self.headers["Authorization"] = f"Bearer {token}"

    def _request(
        self,
        method: str,
        endpoint: str,
        json_data: dict | list | None = None,
    ) -> requests.Response:
        endpoint = endpoint.lstrip("/")

        return requests.request(
            method=method,
            url=f"{self.base_url}/{endpoint}",
            timeout=self.timeout,
            headers=self.headers,
            json=json_data,
        )

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