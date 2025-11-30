from pydantic import BaseModel
from datetime import date

class ActivityCreate(BaseModel):
    user_id: str
    film_id: str

class LogCreate(BaseModel):
    watched_date: date
    rating: float

class ReviewCreate(BaseModel):
    review_text: str
    has_spoiler: bool
