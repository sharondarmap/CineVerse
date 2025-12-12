def test_get_me_success(client, auth_headers):
    response = client.get("/users/me", headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"

def test_get_me_unauthorized(client):
    response = client.get("/users/me")
    assert response.status_code == 401
    assert "Not authenticated" in response.json()["detail"]

def test_get_me_invalid_token(client):
    headers = {"Authorization": "Bearer invalidtoken123"}
    response = client.get("/users/me", headers=headers)
    assert response.status_code == 401
    assert "Could not validate token" in response.json()["detail"]