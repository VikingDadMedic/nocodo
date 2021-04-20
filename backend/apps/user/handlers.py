from datetime import datetime
from typing import Mapping
from fastapi import APIRouter, Depends, status

from utils.database import database, get_database
from apps.auth.utils import get_current_user, crypto_context
from .models import user
from .schema import User, UserCreate

user_router = APIRouter()


@user_router.get(path="/me", response_model=User)
async def read_current_user(
        current_user: User = Depends(get_current_user),
        db: database = Depends(get_database)
) -> Mapping:
    query = user.select().where(
        user.c.id == current_user.id
    )
    _user = await db.fetch_one(query=query)
    return _user


@user_router.post(path="", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(
        user_data: UserCreate,
        db: database = Depends(get_database)
) -> Mapping:
    values = {
        "username": user_data.username,
        "hashed_password": crypto_context.hash(user_data.password),
        "is_account_verified": False,
        "created_at": datetime.utcnow()
    }
    user_id = await db.execute(query=user.insert(), values=values)

    # Read this newly inserted user from DB and return
    query = user.select().where(
        user.c.id == user_id
    )
    _user = await db.fetch_one(query=query)
    return _user
