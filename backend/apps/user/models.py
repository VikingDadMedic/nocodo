from datetime import datetime

from sqlalchemy import (
    Table, Column, Integer, String, DateTime, Boolean, ForeignKey
)

from utils.database import metadata


user = Table(
    "user_user",
    metadata,

    Column("id", Integer, primary_key=True),
    Column("email", String(length=200), nullable=False, unique=True),
    Column("hashed_password", String(length=64), nullable=True),

    Column("first_name", String(length=60), nullable=True),
    Column("last_name", String(length=60), nullable=True),

    Column("is_email_verified", Boolean, nullable=False, default=False),
    Column("is_phone_verified", Boolean, nullable=False, default=False),

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


terms_agreement = Table(
    "user_terms_agreement",
    metadata,

    Column("user_id", ForeignKey("user_user.id"), nullable=False),
    Column("terms_version", String(length=20), nullable=False),

    Column("created_at", DateTime, nullable=False, default=datetime.utcnow)
)
