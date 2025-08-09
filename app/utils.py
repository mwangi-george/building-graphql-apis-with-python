import jwt
from loguru import logger
from functools import wraps
from graphql import GraphQLError
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from datetime import datetime, timedelta, timezone

from app.db.database import SessionLocal
from app.db.models import User
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

def get_authenticated_user(context: dict) -> User:
    request_object = context.get('request')
    auth_header = request_object.headers.get('Authorization')

    if auth_header:
        token = auth_header.split(' ')[1]
        logger.debug(f'token: {token}')

        try:
            payload = jwt.decode(jwt=token, key=SECRET_KEY, algorithms=ALGORITHM)

            with SessionLocal() as session:
                user = session.query(User).filter_by(email=payload.get("sub")).first()
            if not user:
                raise GraphQLError('Could authenticate user')
            return user
        except jwt.ExpiredSignatureError:
            raise GraphQLError('Token has expired')
        except Exception:
            raise GraphQLError('Missing or ivalid token')
    else:
        raise GraphQLError("Missing authentication token")

def hash_password(password: str) -> str:
    ph = PasswordHasher()
    return ph.hash(password)

def verify_password(hashed_password: str, plain_password: str):
    ph = PasswordHasher()
    try:
        ph.verify(hashed_password, plain_password)
    except VerifyMismatchError:
        raise GraphQLError("Invalid password")

def admin_user(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        info = args[1]
        user = get_authenticated_user(info.context)

        if user.role != "admin":
            raise GraphQLError("You are not authorized to perform this action")
        return func(*args, **kwargs)
    return wrapper
