from domain.watchlist.repository import WatchlistRepository

class WatchlistService:

    @staticmethod
    def add(user_id: str, film_id: str):
        return WatchlistRepository.add(user_id, film_id)

    @staticmethod
    def get(user_id: str):
        return WatchlistRepository.get(user_id)

    @staticmethod
    def remove(user_id: str, film_id: str):
        return WatchlistRepository.remove(user_id, film_id)
