# test_app.py
import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_create_task(client):
    response = client.post("/tasks", json={"title": "test task"})
    assert response.status_code == 201
    assert response.get_json()["title"] == "test task"


def test_create_task_missing_title(client):
    response = client.post("/tasks", json={})
    assert response.status_code == 400
