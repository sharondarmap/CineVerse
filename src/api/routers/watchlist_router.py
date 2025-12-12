from fastapi import APIRouter, Depends, HTTPException
from application.watchlist_service import WatchlistService
from api.dependencies import get_current_user

router = APIRouter(prefix="/watchlist", tags=["Watchlist"])

@router.post("/{user_id}/{film_id}")
def add(user_id: str, film_id: str, current_user=Depends(get_current_user)):
    return WatchlistService.add(user_id, film_id)

@router.get("/{user_id}")
def get(user_id: str):
    return WatchlistService.get(user_id)

@router.delete("/{user_id}/{film_id}")
def delete(user_id: str, film_id: str, current_user=Depends(get_current_user)):
    wl = WatchlistService.remove(user_id, film_id)
    if wl is None:
        raise HTTPException(404, "Watchlist not found")
    return wl