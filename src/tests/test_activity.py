# tests/test_activity.py

def create_film(client, headers):
    res = client.post("/films", json={"title": "Act Movie", "synopsis": "T", "release_year": 2020}, headers=headers)
    return res.json()["film_id"]

def test_activity_lifecycle(client, auth_headers, current_user):
    film_id = create_film(client, auth_headers)
    user_id = current_user["user_id"]

    # 1. Create Activity (POST /activity)
    payload_create = {"user_id": user_id, "film_id": film_id}
    res_create = client.post("/activity", json=payload_create, headers=auth_headers)
    assert res_create.status_code == 200
    activity_id = res_create.json()["activity_id"]

    # 2. Add Log (POST /activity/{id}/log)
    payload_log = {"watched_date": "2023-10-10", "rating": 5.0}
    res_log = client.post(f"/activity/{activity_id}/log", json=payload_log, headers=auth_headers)
    assert res_log.status_code == 200
    # Cek apakah log masuk
    assert res_log.json()["logs"][0]["rating"] == 5.0

    # 3. Add Review (POST /activity/{id}/review)
    payload_review = {"review_text": "Great!", "has_spoiler": False}
    res_review = client.post(f"/activity/{activity_id}/review", json=payload_review, headers=auth_headers)
    assert res_review.status_code == 200
    assert res_review.json()["review"]["review_text"] == "Great!"

def test_add_log_not_found(client, auth_headers):
    # Coba add log ke activity ID ngawur
    payload_log = {"watched_date": "2023-10-10", "rating": 5.0}
    res = client.post("/activity/invalid-uuid/log", json=payload_log, headers=auth_headers)
    assert res.status_code == 404

def test_add_review_not_found(client, auth_headers):
    # Coba add review ke activity ID ngawur
    payload_review = {"review_text": "Bad", "has_spoiler": False}
    res = client.post("/activity/invalid-uuid/review", json=payload_review, headers=auth_headers)
    assert res.status_code == 404

def test_list_user_activities(client, auth_headers, current_user):
    # Setup data
    film_id = create_film(client, auth_headers)
    user_id = current_user["user_id"]
    client.post("/activity", json={"user_id": user_id, "film_id": film_id}, headers=auth_headers)

    # Test GET
    res = client.get(f"/activity/user/{user_id}", headers=auth_headers)
    assert res.status_code == 200
    assert isinstance(res.json(), list)
    assert len(res.json()) > 0