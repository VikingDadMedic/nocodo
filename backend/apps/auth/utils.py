from typing import Optional
from fastapi import Depends, HTTPException
import jwt
from starlette import status
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer

from apps.user.models import user
from apps.user.schema import User
from utils.config import settings
from utils.database import database, get_database
from .schema import TokenData


crypto_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def _current_user(
        token: str,
        db: database = Depends(get_database)
) -> Optional[User]:
    """
    For a given JSON Web Token (which comes to the API through HTTP Headers) we try to find the user with the username
    that is saved in the token. Token is created in the user creation or login API endpoints.

    :param token: str The JWT token that is sent to API as HTTP Header
    :param db: database Connection to our database
    :return: Optional[User] Either we find a valid user in the database and return that user or return None
    """
    if token is None:
        return None
    payload = jwt.decode(token, settings.public_key, algorithms=[settings.jwt_hash_algorithm])
    username: str = payload.get("username")
    if username is None:
        return None
    token_data = TokenData(username=username)
    query = user.select().where(
        user.c.username == token_data.username
    )
    result = await db.fetch_one(query=query)
    if result is None:
        return None
    return User(**result)


async def get_current_user(
        token: str = Depends(oauth2_scheme),
        db: database = Depends(get_database)
) -> User:
    """
    This method simply uses the `_current_user` method to find the current user but raises an HTTP 401 Exception in
    case user is not found.

    :param token: str The JWT token that is sent to API as HTTP Header
    :param db: database Connection to our database
    :return: User Returns a user that is currently authenticated else raise a HTTP 401 Exception
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    _user = await _current_user(token=token, db=db)
    if _user is None:
        raise credentials_exception
    return _user


async def get_optional_current_user(
        token: Optional[str] = Depends(oauth2_scheme),
        db: database = Depends(get_database)
) -> Optional[User]:
    """
    This method simply uses the `_current_user` method to find the current user if valid or else return None.

    :param token: str The JWT token that is sent to API as HTTP Header
    :param db: database Connection to our database
    :return: Optional[User] Either we find a valid user in the database and return that user or return None
    """
    if token is None:
        return None
    _user = await _current_user(token=token, db=db)
    return _user


async def authenticate_user(
        username: str,
        password: str,
        db: database
) -> user:
    """
    Given a username and password we try to see if these are valid in the database and either successfully login or
    fail.

    :param username: str The username of the user trying to authenticate
    :param password: str The password of the user that they selected when registering
    :param db: database Connection to our database
    :return: user The SQLAlchemy user Record
    """
    query = user.select().where(
        user.c.username == username
    )
    result = await db.fetch_one(query=query)
    if not result:
        return False
    if not crypto_context.verify(password, result["hashed_password"]):
        return False
    return result


def create_access_token(
        data: dict,
) -> str:
    to_encode = data.copy()
    encoded_jwt = jwt.encode(
        to_encode,
        settings.secret_key,
        algorithm=settings.jwt_hash_algorithm
    )
    return encoded_jwt
