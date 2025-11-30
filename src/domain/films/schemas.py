from pydantic import BaseModel

class FilmCreate(BaseModel):
    title: str
    synopsis: str
    release_year: int

class FilmResponse(BaseModel):
    film_id: str
    title: str
    synopsis: str
    release_year: int
