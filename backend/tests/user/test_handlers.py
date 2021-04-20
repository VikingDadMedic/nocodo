from datetime import datetime
import pytest
from httpx import AsyncClient

from tests.utils import test_username, test_password, get_app, get_client, get_connected_test_database, get_test_user
from apps.user.models import user
from apps.auth.utils import crypto_context, create_access_token


def test_read_current_user_no_authentication():
    client = get_client()
    response = client.get("/users/me")
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_read_current_user():
    app = get_app()
    access_token = create_access_token(
        data={
            "username": test_username
        }
    )

    async with get_test_user() as _user:
        async with AsyncClient(app=app, base_url="http://localhost") as client:
            response = await client.get(
                "/users/me",
                headers={
                    "Authorization": "Bearer {}".format(access_token)
                }
            )
        assert response.status_code == 200
        assert response.json()["id"] == _user["id"]


def test_register_user():
    client = get_client()
    response = client.post(
        "/users",
        json={
            "username": test_username,
            "password": test_password
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert "username" in data
    assert data["username"] == test_username


@pytest.mark.asyncio
async def test_login_with_password():
    app = get_app()

    async with get_test_user() as _user:
        async with AsyncClient(app=app, base_url="http://localhost") as client:
            response = await client.post(
                "/auth/login",
                data={
                    "username": test_username,
                    "password": test_password,
                }
            )
        assert response.status_code == 200
        assert "access_token" in response.json()
