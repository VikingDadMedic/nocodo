from datetime import datetime

from sqlalchemy import (
    Table, Column, Integer, String, DateTime, Boolean, ForeignKey
)

from utils.database import metadata


user = Table(
    "user_user",
    metadata,

    Column("id", Integer, primary_key=True),

    # This is a unique identifier for each user. It can be an actual username or an email
    Column("username", String(length=200), nullable=False, unique=True),
    Column("hashed_password", String(length=64), nullable=True),

    Column("is_email_verified", Boolean, nullable=False, default=False),
    Column("created_at", DateTime, nullable=False, default=datetime.utcnow)
)


email_verification_token = Table(
    "user_email_verification_token",
    metadata,

    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey("user_user.id"), nullable=False),

    Column("token", String(length=32), nullable=False),

    Column("created_at", DateTime, nullable=False, default=datetime.utcnow)
)


forgot_password_token = Table(
    "user_forgot_password_token",
    metadata,

    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey("user_user.id"), nullable=False),

    Column("token", String(length=32), nullable=False),

    Column("created_at", DateTime, nullable=False, default=datetime.utcnow)
)

"""
social_authentication = Table(
    "user_social_authentication",
    metadata,

    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey("user_user.id"), nullable=False),

    Column("provider", String(length=60), nullable=False),
    Column("identifier", String(length=200), nullable=False),

    Column("created_at", DateTime, nullable=False, default=datetime.utcnow)
)
"""
