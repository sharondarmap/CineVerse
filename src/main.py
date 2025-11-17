from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
from uuid import uuid4
from datetime import date

app = FastAPI(title="CineVerse API")

class UserCreate(BaseModel):
    username: str

class User(BaseModel):
    user_id: str
    username: str

class FilmCreate(BaseModel):
    title: str
    synopsis: str
    release_year: int

class Film(BaseModel):
    film_id: str
    title: str
    synopsis: str
    release_year: int

class LogEntry(BaseModel):
    log_id: str
    watched_date: date
    rating: float

class Review(BaseModel):
    review_id: str
    review_text: str
    has_spoiler: bool

class FilmActivity(BaseModel):
    activity_id: str
    user_id: str
    film_id: str
    logs: List[LogEntry] = []
    review: Review | None = None

class WatchlistItem(BaseModel):
    film_id: str
    added_date: date

class Watchlist(BaseModel):
    user_id: str
    items: List[WatchlistItem] = []


# simulasi database disimpan di memory untuk spesifikasi API

db_users: Dict[str, User] = {}
db_films: Dict[str, Film] = {}
db_activities: Dict[str, FilmActivity] = {}
db_watchlists: Dict[str, Watchlist] = {}


# USER API

@app.post("/users", response_model=User)
def register_user(data: UserCreate):
    user_id = str(uuid4())
    user = User(user_id=user_id, username=data.username)
    db_users[user_id] = user
    return user

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: str):
    if user_id not in db_users:
        raise HTTPException(404, "User not found")
    return db_users[user_id]


# FILM API

@app.post("/films", response_model=Film)
def add_film(data: FilmCreate):
    film_id = str(uuid4())
    film = Film(
        film_id=film_id,
        title=data.title,
        synopsis=data.synopsis,
        release_year=data.release_year
    )
    db_films[film_id] = film
    return film

@app.get("/films/{film_id}", response_model=Film)
def get_film(film_id: str):
    if film_id not in db_films:
        raise HTTPException(404, "Film not found")
    return db_films[film_id]

@app.get("/films", response_model=List[Film])
def list_films():
    return list(db_films.values())


# FILM ACTIVITY API

class ActivityCreate(BaseModel):
    user_id: str
    film_id: str

@app.post("/activity", response_model=FilmActivity)
def create_activity(data: ActivityCreate):
    if data.user_id not in db_users:
        raise HTTPException(404, "User not found")
    if data.film_id not in db_films:
        raise HTTPException(404, "Film not found")

    activity_id = str(uuid4())
    activity = FilmActivity(
        activity_id=activity_id,
        user_id=data.user_id,
        film_id=data.film_id
    )
    db_activities[activity_id] = activity
    return activity


class LogCreate(BaseModel):
    watched_date: date
    rating: float

@app.post("/activity/{activity_id}/log", response_model=FilmActivity)
def add_log(activity_id: str, data: LogCreate):
    if activity_id not in db_activities:
        raise HTTPException(404, "Activity not found")

    log = LogEntry(
        log_id=str(uuid4()),
        watched_date=data.watched_date,
        rating=data.rating
    )
    db_activities[activity_id].logs.append(log)
    return db_activities[activity_id]


class ReviewCreate(BaseModel):
    review_text: str
    has_spoiler: bool

@app.post("/activity/{activity_id}/review", response_model=FilmActivity)
def write_review(activity_id: str, data: ReviewCreate):
    if activity_id not in db_activities:
        raise HTTPException(404, "Activity not found")

    review = Review(
        review_id=str(uuid4()),
        review_text=data.review_text,
        has_spoiler=data.has_spoiler
    )
    db_activities[activity_id].review = review
    return db_activities[activity_id]


@app.get("/users/{user_id}/activities", response_model=List[FilmActivity])
def list_activities(user_id: str):
    return [a for a in db_activities.values() if a.user_id == user_id]


# WATCHLIST API


@app.post("/watchlist/{user_id}/{film_id}", response_model=Watchlist)
def add_to_watchlist(user_id: str, film_id: str):
    if user_id not in db_users:
        raise HTTPException(404, "User not found")
    if film_id not in db_films:
        raise HTTPException(404, "Film not found")

    if user_id not in db_watchlists:
        db_watchlists[user_id] = Watchlist(user_id=user_id, items=[])

    item = WatchlistItem(film_id=film_id, added_date=date.today())
    db_watchlists[user_id].items.append(item)
    return db_watchlists[user_id]

@app.get("/watchlist/{user_id}", response_model=Watchlist)
def get_watchlist(user_id: str):
    if user_id not in db_watchlists:
        return Watchlist(user_id=user_id, items=[])
    return db_watchlists[user_id]

@app.delete("/watchlist/{user_id}/{film_id}", response_model=Watchlist)
def remove_watchlist_item(user_id: str, film_id: str):
    if user_id not in db_watchlists:
        raise HTTPException(404, "Watchlist not found")

    db_watchlists[user_id].items = [
        i for i in db_watchlists[user_id].items if i.film_id != film_id
    ]
    return db_watchlists[user_id]

# ROOT

@app.get("/")
def home():
    return {"message": "CineVerse API is running!"}