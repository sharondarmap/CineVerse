from fastapi import APIRouter, HTTPException
from uuid import uuid4

from domain.users.schemas import UserCreate, UserLogin, UserResponse
from domain.users.models import User
from domain.users.repository import UserRepository

from core.security import hash_password, verify_password
from core.jwt_manager import create_access_token

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register", response_model=UserResponse)
def register(data: UserCreate):
    existing = UserRepository.get_by_username(data.username)
    if existing:
        raise HTTPException(400, "Username already exists")

    hashed = hash_password(data.password)

    user = User(
        user_id=str(uuid4()),
        username=data.username,
        password_hash=hashed
    )

    UserRepository.save(user)

    return UserResponse(
        user_id=user.user_id,
        username=user.username
    )


@router.post("/login")
def login(data: UserLogin):
    user = UserRepository.get_by_username(data.username)
    if not user:
        raise HTTPException(400, "Invalid username or password")

    if not verify_password(data.password, user.password_hash):
        raise HTTPException(400, "Invalid username or password")

    token = create_access_token({"sub": user.username})

    return {"access_token": token, "token_type": "bearer"}
