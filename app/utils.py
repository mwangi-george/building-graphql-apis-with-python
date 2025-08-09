import jwt
from graphql import GraphQLError
from loguru import logger
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from datetime import datetime, timedelta, timezone

from app.settings.config import SECRET_KEY, ALGORITHM, TOKEN_EXPIRY_IN_MINUTES



def generate_token(email: str) -> str:
    payload = {
        "sub": email,
        "exp": datetime.now(tz=timezone.utc) + timedelta(minutes=TOKEN_EXPIRY_IN_MINUTES),
    }
    try:
        token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
        return token
    except Exception as e:
        logger.error(f"Failed to generate token: {str(e)}")
        raise Exception("Failed to generate token")

def hash_password(password: str) -> str:
    ph = PasswordHasher()
    return ph.hash(password)

def verify_password(hashed_password: str, plain_password: str):
    ph = PasswordHasher()
    try:
        ph.verify(hashed_password, plain_password)
    except VerifyMismatchError:
        raise GraphQLError("Invalid password")