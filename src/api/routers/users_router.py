from fastapi import APIRouter
from application.users_service import UsersService
from domain.users.schemas import UserCreate, UserResponse

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("", response_model=UserResponse)
def register_user(data: UserCreate):
    user = UsersService.register(data.username, data.password)
    return user
