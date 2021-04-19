from datetime import datetime
import pytest
from httpx import AsyncClient

from tests.utils import get_app, get_client, get_connected_test_database
from apps.user.models import user
from apps.authentication.utils import crypto_context, create_access_token


def test_read_current_user_no_authentication():
    client = get_client()
    response = client.get("/users/me")
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_read_current_user():
    username = "testuser00202"
    app = get_app()
    access_token = create_access_token(
        data={
            "username": username
        }
    )

    async with get_connected_test_database() as db:
        await db.execute(query=user.insert(), values={
            "username": username,
            "hashed_password": crypto_context.hash("testuserpassword"),
            "is_account_verified": False,
            "created_at": datetime.utcnow()
        })

        async with AsyncClient(app=app, base_url="http://localhost") as client:
            response = await client.get(
                "/users/me",
                headers={
                    "Authorization": "Bearer {}".format(access_token)
                }
            )

        assert response.status_code == 200


def test_register_user():
    client = get_client()
    pass
