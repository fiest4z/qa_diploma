import requests
from typing import Optional


class BaseAPI:
    def __init__(self, base_url: str, token: Optional[str] = None):
        self.base_url = base_url
        self.headers = {}

        if token:
            self.headers["X-API-KEY"] = token

    def get(self, endpoint: str, params: dict | None = None) -> requests.Response:
        return requests.get(
            url=f"{self.base_url}{endpoint}",
            headers=self.headers,
            params=params
        )

    def put(self, endpoint: str, params: dict | None = None) -> requests.Response:
        return requests.put(
            url=f"{self.base_url}{endpoint}",
            headers=self.headers,
            params=params
        )
