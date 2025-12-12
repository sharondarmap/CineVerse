def test_register_success(client):
    response = client.post("/auth/register", json={"username": "newuser", "password": "pass"})
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "newuser"
    assert "user_id" in data

def test_register_duplicate_username(client):
    payload = {"username": "user1", "password": "pass"}
    client.post("/auth/register", json=payload)
    # Register lagi
    response = client.post("/auth/register", json=payload)
    assert response.status_code == 400
    assert "already exists" in response.json()["detail"]

def test_login_success(client):
    # Register dulu
    client.post("/auth/register", json={"username": "loginuser", "password": "securepass"})
    # Login
    response = client.post("/auth/login", json={"username": "loginuser", "password": "securepass"})
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_wrong_password(client):
    client.post("/auth/register", json={"username": "wrongpass", "password": "securepass"})
    response = client.post("/auth/login", json={"username": "wrongpass", "password": "wrong123"})
    assert response.status_code == 400
    assert "Invalid username or password" in response.json()["detail"]

def test_login_user_not_found(client):
    response = client.post("/auth/login", json={"username": "ghost", "password": "boo"})
    assert response.status_code == 400