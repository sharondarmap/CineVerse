from pydantic import BaseModel
from uuid import uuid4

class Film(BaseModel):
    film_id: str
    title: str
    synopsis: str
    release_year: int

    @staticmethod
    def create(title: str, synopsis: str, year: int):
        return Film(
            film_id=str(uuid4()),
            title=title,
            synopsis=synopsis,
            release_year=year
        )
