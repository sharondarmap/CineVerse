from domain.films.models import Film
from domain.films.repository import FilmRepository

class FilmsService:

    @staticmethod
    def add(title: str, synopsis: str, year: int):
        film = Film.create(title, synopsis, year)
        return FilmRepository.save(film)

    @staticmethod
    def get(film_id: str):
        return FilmRepository.get_by_id(film_id)

    @staticmethod
    def list():
        return FilmRepository.list_all()
