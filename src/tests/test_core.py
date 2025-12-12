from core.security import hash_password, verify_password
from core.jwt_manager import create_access_token
from jose import jwt
from core.config import SECRET_KEY, ALGORITHM

def test_password_hashing():
    pwd = "secret"
    hashed = hash_password(pwd)
    assert hashed != pwd
    assert verify_password(pwd, hashed) is True
    assert verify_password("wrong", hashed) is False

def test_jwt_generation():
    data = {"sub": "tester"}
    token = create_access_token(data)
    decoded = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    assert decoded["sub"] == "tester"
    assert "exp" in decoded