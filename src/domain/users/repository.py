from infrastructure.memory_db import db_users
from domain.users.models import User

class UserRepository:

    @staticmethod
    def save(user: User):
        db_users[user.user_id] = user
        return user

    @staticmethod
    def get_by_id(user_id: str):
        return db_users.get(user_id)

    @staticmethod
    def get_by_username(username: str):
        return next((u for u in db_users.values() if u.username == username), None)
