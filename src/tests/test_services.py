# tests/test_services.py
import pytest
from application.users_service import UsersService
from application.films_service import FilmsService
from domain.users.repository import UserRepository
from domain.films.repository import FilmRepository

# Reset DB fixture (menggunakan autouse dari conftest)

def test_user_service_register_duplicate():
    # 1. Register user pertama
    UsersService.register("duplicate_user", "pass123")
    
    # 2. Coba register lagi dengan username sama -> Expect Error
    with pytest.raises(ValueError) as excinfo:
        UsersService.register("duplicate_user", "pass123")
    
    assert "already exists" in str(excinfo.value)

def test_film_service_methods():
    # Test Create
    film = FilmsService.create_film("Service Movie", "Syn", 2022)
    assert film.title == "Service Movie"
    
    # Test Get All
    films = FilmsService.get_all_films()
    assert len(films) >= 1
    
    # Test Get By ID
    fetched = FilmsService.get_film_by_id(film.film_id)
    assert fetched.title == "Service Movie"
    
    # Test Get Invalid
    assert FilmsService.get_film_by_id("invalid") is None