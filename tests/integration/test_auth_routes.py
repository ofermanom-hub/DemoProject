import pytest
from httpx import AsyncClient, ASGITransport
from src.main import app


@pytest.mark.asyncio
async def test_register_and_login() -> None:
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        r = await client.post("/api/v1/auth/register", json={"email": "a@b.com", "password": "pass"})
        assert r.status_code == 201

        r = await client.post("/api/v1/auth/token", json={"email": "a@b.com", "password": "pass"})
        assert r.status_code == 200
        assert "access_token" in r.json()
