import databases
from contextlib import asynccontextmanager
from sqlalchemy import create_engine
from fastapi.testclient import TestClient

from main import app
from utils.config import settings
from utils.database import get_database, get_test_database, metadata


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
