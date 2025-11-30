from pydantic import BaseModel
from uuid import uuid4
from datetime import date

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
    logs: list[LogEntry] = []
    review: Review | None = None

    @staticmethod
    def create(user_id: str, film_id: str):
        return FilmActivity(
            activity_id=str(uuid4()),
            user_id=user_id,
            film_id=film_id,
            logs=[],
            review=None
        )
