from pydantic import BaseModel
from datetime import date

class WatchlistItem(BaseModel):
    film_id: str
    added_date: date

class Watchlist(BaseModel):
    user_id: str
    items: list[WatchlistItem] = []
