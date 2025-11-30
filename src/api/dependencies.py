from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from core.config import SECRET_KEY, ALGORITHM
from domain.users.repository import UserRepository

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")

        if username is None:
            raise HTTPException(401, "Invalid token")

        user = UserRepository.get_by_username(username)
        if not user:
            raise HTTPException(401, "User does not exist")

        return user

    except JWTError:
        raise HTTPException(401, "Could not validate token")
