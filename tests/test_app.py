import os
import sys

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "app"))
)

from app import app


def test_homepage():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert b"Welcome to ShopEase" in response.data


def test_health():
    response = app.test_client().get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_version():
    response = app.test_client().get("/version")
    assert response.status_code == 200
    assert response.json["version"] == "1.0"
