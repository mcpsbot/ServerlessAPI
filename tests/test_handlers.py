from app import main
from fastapi.testclient import TestClient

client = TestClient(main.app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200


def test_read_api_v1_users():
    response = client.get("/api/v1/users")
    assert response.status_code == 200
