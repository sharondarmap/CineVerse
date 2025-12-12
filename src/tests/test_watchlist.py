# tests/test_watchlist.py

def create_film(client, headers):
    res = client.post("/films", json={"title": "WL Movie", "synopsis": "T", "release_year": 2021}, headers=headers)
    return res.json()["film_id"]

def test_watchlist_lifecycle(client, auth_headers, current_user):
    film_id = create_film(client, auth_headers)
    user_id = current_user["user_id"]

    # 1. Add to Watchlist (POST /{uid}/{fid})
    res_add = client.post(f"/watchlist/{user_id}/{film_id}", headers=auth_headers)
    assert res_add.status_code == 200
    # Cek response harus mengandung item
    data = res_add.json()
    assert len(data["items"]) == 1
    assert data["items"][0]["film_id"] == film_id

    # 2. Get Watchlist (GET /{uid})
    res_get = client.get(f"/watchlist/{user_id}", headers=auth_headers)
    assert res_get.status_code == 200
    assert len(res_get.json()["items"]) == 1

    # 3. Remove from Watchlist (DELETE /{uid}/{fid})
    res_del = client.delete(f"/watchlist/{user_id}/{film_id}", headers=auth_headers)
    assert res_del.status_code == 200
    assert len(res_del.json()["items"]) == 0

def test_remove_watchlist_not_found(client, auth_headers, current_user):
    # Coba hapus saat watchlist user belum pernah dibuat
    # Ini akan men-trigger return None di repository
    user_id = "random-user-id" 
    film_id = "random-film-id"
    
    res = client.delete(f"/watchlist/{user_id}/{film_id}", headers=auth_headers)
    assert res.status_code == 404