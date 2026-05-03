"""Generic async HTTP client wrapper for external REST services."""
import httpx

from src.config.settings import settings


class ExternalAPIClient:
    def __init__(self) -> None:
        self._base = settings.external_api_base_url
        self._headers = {"Authorization": f"Bearer {settings.external_api_key}"}

    async def get(self, path: str) -> dict:
        async with httpx.AsyncClient(base_url=self._base, headers=self._headers) as client:
            response = await client.get(path)
            response.raise_for_status()
            return response.json()

    async def post(self, path: str, payload: dict) -> dict:
        async with httpx.AsyncClient(base_url=self._base, headers=self._headers) as client:
            response = await client.post(path, json=payload)
            response.raise_for_status()
            return response.json()


external_client = ExternalAPIClient()
