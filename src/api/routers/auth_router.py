from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from core.security import verify_password
from core.jwt_manager import create_access_token
from infrastructure.memory_db import db_users

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
def login(form: OAuth2PasswordRequestForm = Depends()):
    user = next((u for u in db_users.values() if u.username == form.username), None)
    if not user or not verify_password(form.password, user.password):
        raise HTTPException(400, "Invalid username or password")

    token = create_access_token({"sub": user.user_id})
    return {"access_token": token, "token_type": "bearer"}
