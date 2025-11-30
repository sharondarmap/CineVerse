from fastapi import FastAPI
from api.routers.users_router import router as users_router
from api.routers.auth_router import router as auth_router
from api.routers.films_router import router as films_router
from api.routers.activity_router import router as activity_router
from api.routers.watchlist_router import router as watchlist_router

app = FastAPI(title="CineVerse API")

app.include_router(users_router)
app.include_router(auth_router)
app.include_router(films_router)
app.include_router(activity_router)
app.include_router(watchlist_router)

@app.get("/")
def home():
    return {"message": "CineVerse API is running!"}
