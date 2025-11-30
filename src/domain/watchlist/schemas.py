from pydantic import BaseModel

class WatchlistResponse(BaseModel):
    user_id: str
    items: list
