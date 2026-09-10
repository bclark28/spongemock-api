"""Tests for the public API."""

import pytest

from spongemock_api import create_app


@pytest.fixture()
def client():
    app = create_app()
    app.config.update(TESTING=True)
    return app.test_client()


def test_health_returns_ok(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json == {"status": "ok"}


def test_spongemock_returns_mixed_case_text(client):
    response = client.get("/spongemock?text=Hello%20World%21")

    assert response.status_code == 200
    assert response.json["error"] is None
    assert response.json["mockedText"].lower() == "hello world!"


def test_spongemock_requires_text(client):
    response = client.get("/spongemock")

    assert response.status_code == 400
    assert response.json == {"error": "query is not valid", "mockedText": None}
