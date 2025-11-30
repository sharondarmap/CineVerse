from infrastructure.memory_db import db_films
from domain.films.models import Film

class FilmRepository:

    @staticmethod
    def save(film: Film):
        db_films[film.film_id] = film
        return film

    @staticmethod
    def get_by_id(film_id: str):
        return db_films.get(film_id)

    @staticmethod
    def list_all():
        return list(db_films.values())
