from domain.users.models import User
from domain.users.repository import UserRepository
from core.security import hash_password, verify_password

class UsersService:

    @staticmethod
    def register(username: str, password: str):
        hashed = hash_password(password)
        user = User.create(username, hashed)
        return UserRepository.save(user)

    @staticmethod
    def get(username: str):
        return UserRepository.get_by_username(username)

    @staticmethod
    def verify_login(username: str, password: str):
        user = UserRepository.get_by_username(username)
        if not user or not verify_password(password, user.password):
            return None
        return user
