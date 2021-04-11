from datetime import datetime

from sqlalchemy import (
    Table, Column, Integer, String, DateTime, ForeignKey, JSON
)

from utils.database import metadata


settings = Table(
    "system_settings",
    metadata,

    Column("id", Integer, primary_key=True),
    Column("label", String(length=100), nullable=False),
    Column("key", String(length=60), nullable=False, unique=True),

    # This is the difference of this version from its previous one, for the same `text_id` and `locale`
    Column("value", JSON, nullable=False),

    Column("user_id", Integer, ForeignKey("user_user.id"), nullable=True),
    Column("created_at", DateTime, nullable=False, default=datetime.utcnow),
)


"""
locale = Table(
    "system_locale",
    metadata,

    Column("id", Integer, primary_key=True),
    Column("label", String(length=100), nullable=False),
    Column("locale", String(length=40), nullable=False),

    Column("user_id", Integer, ForeignKey("user_user.id"), nullable=True),
    Column("created_at", DateTime, nullable=False, default=datetime.utcnow),
)
"""
