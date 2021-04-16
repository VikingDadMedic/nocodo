from datetime import datetime
from typing import Optional

from pydantic import BaseModel, constr


class User(BaseModel):
    id: int
    email: constr(max_length=200)

    is_email_verified: bool = False
    created_at: datetime


class UserCreate(BaseModel):
    email: constr(max_length=200, strip_whitespace=True)
    password: constr(max_length=32, strip_whitespace=True)


class UserUpdate(BaseModel):
    first_name: Optional[constr(max_length=60, strip_whitespace=True)]
    last_name: Optional[constr(max_length=60, strip_whitespace=True)]
