from uuid import uuid4
from domain.users.models import User
from domain.users.repository import UserRepository
from domain.users.schemas import UserResponse
from core.security import hash_password

class UsersService:

    @staticmethod
    def register(username: str, password: str):
        # Cek username sudah ada
        if UserRepository.get_by_username(username):
            raise ValueError("Username already exists")

        hashed = hash_password(password)

        user = User(
            user_id=str(uuid4()),
            username=username,
            password_hash=hashed
        )

        UserRepository.save(user)

        return UserResponse(
            user_id=user.user_id,
            username=user.username
        )
