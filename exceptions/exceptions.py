class ApiError(Exception):
    def __init__(
        self,
        method: str,
        url: str,
        message: str,
        status_code: int | None = None,
    ):
        super().__init__(message)
        self.method = method
        self.url = url
        self.message = message
        self.status_code = status_code

    def __str__(self) -> str:
        return (
            f"{self.message}\n"
            f"Method: {self.method}\n"
            f"URL: {self.url}"
        )

class ApiNetworkError(ApiError):
    pass


class ApiTimeoutError(ApiNetworkError):
    def __init__(self, method: str, url: str):
        super().__init__(
            method=method,
            url=url,
            message="Request timed out",
        )


class ApiConnectionError(ApiNetworkError):
    def __init__(self, method: str, url: str):
        super().__init__(
            method=method,
            url=url,
            message="Connection failed",
        )


class ApiInvalidUrlError(ApiError):
    def __init__(self, method: str, url: str):
        super().__init__(
            method=method,
            url=url,
            message="Invalid URL",
        )