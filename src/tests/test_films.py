# tests/test_films.py

def test_films_crud(client, auth_headers):
    # Create
    payload = {"title": "Inception", "synopsis": "Dream", "release_year": 2010}
    res_create = client.post("/films", json=payload, headers=auth_headers)
    assert res_create.status_code == 200
    film_id = res_create.json()["film_id"]

    # Get All
    res_get = client.get("/films", headers=auth_headers) # Asumsi protected sesuai kode sebelumnya
    if res_get.status_code == 401:
        # Jika public endpoint
        res_get = client.get("/films")
    assert res_get.status_code == 200
    assert len(res_get.json()) > 0

    # Get One
    res_id = client.get(f"/films/{film_id}", headers=auth_headers)
    if res_id.status_code == 401:
         res_id = client.get(f"/films/{film_id}")
    assert res_id.status_code == 200
    assert res_id.json()["title"] == "Inception"

def test_get_film_not_found(client, auth_headers):
    # Coba akses ID ngawur
    # Pake header jaga-jaga kalau protected
    res = client.get("/films/invalid-id", headers=auth_headers) 
    assert res.status_code == 404