import pytest
from fastapi.testclient import TestClient
from main import app
from infrastructure.memory_db import db_users, db_films, db_activities, db_watchlists

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture(autouse=True)
def clear_db():
    db_users.clear()
    db_films.clear()
    db_activities.clear()
    db_watchlists.clear() # Reset watchlist juga

@pytest.fixture
def auth_headers(client):
    # Register
    client.post("/auth/register", json={"username": "testuser", "password": "password123"})
    # Login
    response = client.post("/auth/login", json={"username": "testuser", "password": "password123"})
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}

@pytest.fixture
def current_user(client, auth_headers):
    # Helper untuk mendapatkan ID user yang sedang login
    response = client.get("/users/me", headers=auth_headers)
    return response.json()