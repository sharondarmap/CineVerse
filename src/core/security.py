from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt
from core.config import SECRET_KEY, ALGORITHM, ACCESS_EXPIRE_MINUTES

# gunakan sha256_crypt agar stabil di MacOS & uv
pwd_context = CryptContext(schemes=["sha256_crypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(password: str, hashed: str):
    return pwd_context.verify(password, hashed)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_EXPIRE_MINUTES)
    to_encode["exp"] = expire
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
