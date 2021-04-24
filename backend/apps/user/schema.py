from datetime import datetime
from typing import Optional
from pydantic import BaseModel, constr

from apps.auth.schema import Token


class User(BaseModel):
    id: int
    username: constr(max_length=200)

    is_account_verified: bool = False
    created_at: datetime


class UserCreate(BaseModel):
    username: constr(max_length=200, strip_whitespace=True)
    password: constr(max_length=32, strip_whitespace=True)


class UserUpdate(BaseModel):
    first_name: Optional[constr(max_length=60, strip_whitespace=True)]
    last_name: Optional[constr(max_length=60, strip_whitespace=True)]


class UserWithToken(User, Token):
    pass
