from fastapi.testclient import TestClient

from main import app


def get_client():
    client = TestClient(app=app)
    return client
