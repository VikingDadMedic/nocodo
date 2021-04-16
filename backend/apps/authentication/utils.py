from datetime import datetime, timedelta
from typing import Optional
from fastapi import Depends, HTTPException
from jose import jwt, JWTError
from starlette import status
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer

from apps.user.models import user
from apps.user.schema import User
from apps.authentication.schema import TokenData
from utils.config import settings
from utils.database import database, get_database


crypto_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_current_user(
        token: str = Depends(oauth2_scheme),
        db: database = Depends(get_database)
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.password_hash_algorithm])
        username: str = payload.get("username")
        if username is None:
            raise credentials_exception
    except JWTError as e:
        raise credentials_exception

    query = user.select().where(
        user.c.email == username
    )
    result = await db.fetch_one(query=query)

    if result is None:
        raise credentials_exception
    return User(**result)


async def get_optional_current_user(
        token: Optional[str] = Depends(oauth2_scheme),
        db: database = Depends(get_database)
) -> Optional[User]:
    if token is None:
        return None
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.password_hash_algorithm])
        username: str = payload.get("username")
        if username is None:
            return None
        token_data = TokenData(username=username)
    except JWTError:
        return None

    query = user.select().where(
        user.c.email == token_data.username
    )
    result = await db.fetch_one(query=query)

    if result is None:
        return None
    return User(**result)


async def authenticate_user(
        username: str,
        password: str,
        db: database
) -> user:
    query = user.select().where(
        user.c.email == username
    )
    result = await db.fetch_one(query=query)
    if not result:
        return False
    if user.hashed_password is None:
        # This is a temporary user, let's check the temporary password or link hash
        temps = await db.fetch_all(query=query)
        if len(temps) == 0:
            return False
        match = []
        if len(password) == 16:
            # This is URL hash, we use max 72 hours TTL
            match = [x for x in temps if x["hash"][:16] == password]
        elif len(password) == 7:
            # This is temporary verification password, we use 30 minutes TTL
            match = [x for x in temps if x["hash"][:7] == password and
                     x["created_at"] > (datetime.utcnow() - timedelta(minutes=72))]
        if len(match) == 0:
            return False
    elif not verify_password(password, user.hashed_password):
        return False
    return result


def verify_password(plain_password, hashed_password):
    return crypto_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return crypto_context.hash(password)


def create_access_token(
        data: dict,
        expires_delta: Optional[timedelta] = None
) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode,
        settings.secret_key,
        algorithm=settings.password_hash_algorithm
    )
    return encoded_jwt