from datetime import datetime
from typing import Optional

from pydantic import BaseModel, constr

from .models import PronounChoices


class User(BaseModel):
    id: int
    email: constr(max_length=200)

    first_name: Optional[constr(max_length=60)]
    last_name: Optional[constr(max_length=60)]
    pronoun: Optional[PronounChoices]
    timezone: Optional[constr(max_length=100)]
    image_hash: Optional[constr(max_length=32)]
    image_extension: Optional[constr(max_length=8, strip_whitespace=True)]

    phone_number: Optional[int]
    phone_country: Optional[constr(max_length=2)]

    is_email_verified: bool = False
    is_phone_verified: bool = False
    created_at: datetime


class UserCreate(BaseModel):
    email: constr(max_length=200, strip_whitespace=True)

    first_name: Optional[constr(max_length=60, strip_whitespace=True)]
    last_name: Optional[constr(max_length=60, strip_whitespace=True)]
    pronoun: Optional[PronounChoices]
    timezone: Optional[constr(max_length=100)]

    phone_number: Optional[int]
    phone_country: Optional[constr(max_length=2)]


class UserUpdate(BaseModel):
    first_name: Optional[constr(max_length=60, strip_whitespace=True)]
    last_name: Optional[constr(max_length=60, strip_whitespace=True)]
    pronoun: Optional[PronounChoices]
    timezone: Optional[constr(max_length=100, strip_whitespace=True)]

    phone_number: Optional[int]
    phone_country: Optional[constr(max_length=2, strip_whitespace=True)]


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
