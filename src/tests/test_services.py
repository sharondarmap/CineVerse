import pytest
from application.users_service import UsersService
from application.films_service import FilmsService
from infrastructure.memory_db import db_users, db_films


def test_user_service_register_duplicate():
    UsersService.register("duplicate_user", "pass123")
    with pytest.raises(ValueError) as excinfo:
        UsersService.register("duplicate_user", "pass123")
    assert "already exists" in str(excinfo.value)

def test_film_service_methods():
    # 1. Create
    film = FilmsService.add("Service Movie", "Syn", 2022)
    assert film.title == "Service Movie"
    
    # 2. Get All
    films = FilmsService.list()
    assert len(films) >= 1
    
    # 3. Get By ID 
    fetched = FilmsService.get(film.film_id)
    assert fetched.title == "Service Movie"
    
    assert FilmsService.get("invalid-id") is None