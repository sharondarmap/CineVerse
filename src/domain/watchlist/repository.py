from infrastructure.memory_db import db_watchlists
from domain.watchlist.models import Watchlist, WatchlistItem
from datetime import date

class WatchlistRepository:

    @staticmethod
    def add(user_id: str, film_id: str):
        if user_id not in db_watchlists:
            db_watchlists[user_id] = Watchlist(user_id=user_id, items=[])

        item = WatchlistItem(film_id=film_id, added_date=date.today())
        db_watchlists[user_id].items.append(item)
        return db_watchlists[user_id]

    @staticmethod
    def get(user_id: str):
        return db_watchlists.get(user_id, Watchlist(user_id=user_id, items=[]))

    @staticmethod
    def remove(user_id: str, film_id: str):
        if user_id not in db_watchlists:
            return None

        wl = db_watchlists[user_id]
        wl.items = [i for i in wl.items if i.film_id != film_id]
        return wl
