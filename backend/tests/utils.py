from datetime import datetime
import databases
from contextlib import asynccontextmanager
from sqlalchemy import create_engine
from fastapi.testclient import TestClient

from main import app
from apps.user.models import user
from apps.auth.utils import crypto_context
from utils.config import settings
from utils.database import get_database, get_test_database, metadata


test_username = "testuser00202"
test_password = "testuserpassword"


def get_app():
    app.dependency_overrides[get_database] = get_test_database
    return app


def get_client():
    app.dependency_overrides[get_database] = get_test_database
    client = TestClient(app=app)
    return client


@asynccontextmanager
async def get_connected_test_database():
    test_url = "postgresql://{user}:{password}@{host}/test_{name}".format(**settings.database)
    test_database = databases.Database(url=test_url)
    engine = create_engine(test_url)
    try:
        metadata.create_all(engine)
        await test_database.connect()
        yield test_database
    finally:
        await test_database.disconnect()
        metadata.drop_all(engine)


@asynccontextmanager
async def get_test_user():
    global test_username
    global test_password
    async with get_connected_test_database() as db:
        user_id = await db.execute(query=user.insert(), values={
            "username": test_username,
            "hashed_password": crypto_context.hash(test_password),
            "is_account_verified": False,
            "created_at": datetime.utcnow()
        })
        _user = await db.fetch_one(query=user.select().where(
            user.c.id == user_id
        ))
        yield _user
