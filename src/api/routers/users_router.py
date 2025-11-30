from fastapi import APIRouter, Depends
from api.dependencies import get_current_user
from application.users_service import UsersService
from domain.users.schemas import UserCreate, UserResponse

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/me", response_model=UserResponse)
def get_me(user = Depends(get_current_user)):
    return UserResponse(
        user_id=user.user_id,
        username=user.username
    )

@router.post("", response_model=UserResponse)
def register_user(data: UserCreate):
    user = UsersService.register(data.username, data.password)
    return user
