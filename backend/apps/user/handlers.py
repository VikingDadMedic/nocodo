from fastapi import APIRouter, Depends

from utils.database import database, get_database
from .authentication import get_current_user
from .models import user
from .schema import User

user_router = APIRouter()


@user_router.get(path="/me", response_model=User)
async def read_user(
        current_user: User = Depends(get_current_user),
        db: database = Depends(get_database)
):
    query = user.select().where(
        user.c.id == current_user.id
    )
    _user = await db.fetch_one(query=query)
    return _user
