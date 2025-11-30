from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from core.config import SECRET_KEY, ALGORITHM
from infrastructure.memory_db import db_users

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        if user_id not in db_users:
            raise HTTPException(401, "Invalid user")
        return db_users[user_id]
    except:
        raise HTTPException(401, "Invalid token")
