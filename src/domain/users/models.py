from pydantic import BaseModel
from uuid import uuid4

class User(BaseModel):
    user_id: str
    username: str
    password: str  # hashed password

    @staticmethod
    def create(username: str, hashed_password: str):
        return User(
            user_id=str(uuid4()),
            username=username,
            password=hashed_password
        )
