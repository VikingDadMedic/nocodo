from datetime import datetime, timedelta
from typing import Optional

from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy import desc

from utils.config import settings
from utils.database import database, get_database
from .models import user, temporary_login_password
from .schema import User, TokenData, Token

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
authentication_router = APIRouter()


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


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
        query = temporary_login_password.select().where(
            temporary_login_password.c.user_id == result["id"],
            temporary_login_password.c.created_at > (datetime.utcnow() - timedelta(hours=72))
        ).ordey_by(
            desc(temporary_login_password.c.id)
        )
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


@authentication_router.post("/token", response_model=Token)
async def login_for_access_token(
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: database = Depends(get_database)
):
    result = await authenticate_user(
        username=form_data.username,
        password=form_data.password,
        db=db
    )
    if not result:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.access_token_expires_minutos)
    access_token = create_access_token(
        data={
            "username": result["email"]
        }, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
