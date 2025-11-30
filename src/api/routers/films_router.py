from fastapi import APIRouter, Depends, HTTPException
from application.films_service import FilmsService
from domain.films.schemas import FilmCreate, FilmResponse
from api.dependencies import get_current_user

router = APIRouter(prefix="/films", tags=["Films"])

@router.post("", response_model=FilmResponse)
def add_film(data: FilmCreate, current_user=Depends(get_current_user)):
    return FilmsService.add(data.title, data.synopsis, data.release_year)

@router.get("/{film_id}", response_model=FilmResponse)
def get_film(film_id: str):
    film = FilmsService.get(film_id)
    if not film:
        raise HTTPException(404, "Film not found")
    return film

@router.get("", response_model=list[FilmResponse])
def list_films():
    return FilmsService.list()
