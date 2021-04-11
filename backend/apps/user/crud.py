from typing import Optional, Mapping
from datetime import datetime

from utils.database import database
from .models import user


async def get_or_create_user_with_email(
        db: database,
        email: str,
        created_at: Optional[datetime] = None,
) -> Optional[Mapping]:
    created_at = datetime.utcnow() if created_at is None else created_at

    query = user.select().where(
        user.c.email == email
    )
    existing_user = await db.fetch_one(query=query)
    if existing_user is None:
        # This is a new email address in our system, let's create a user
        query = user.insert().values(
            email=email,
            is_email_verified=False,
            is_phone_verified=False,
            created_at=created_at
        )
        user_id = await db.execute(query=query)
    else:
        user_id = existing_user["id"]

    query = user.select().where(
        user.c.id == user_id
    )
    user_obj = await db.fetch_one(query=query)
    return user_obj
