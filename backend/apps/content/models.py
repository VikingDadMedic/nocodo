from datetime import datetime

from sqlalchemy import (
    Table, Column, Integer, String, Text, DateTime, SmallInteger, ForeignKey, JSON, UniqueConstraint
)

from utils.database import metadata


placeholder = Table(
    "content_placeholder",
    metadata,

    Column("id", Integer, primary_key=True),

    # This is stored as a slug
    Column("identifier", String(length=100), nullable=False, unique=True),

    Column("user_id", Integer, ForeignKey("user_user.id"), nullable=True),
    Column("created_at", DateTime, nullable=False, default=datetime.utcnow),
)

text = Table(
    "content_text",
    metadata,

    Column("id", Integer, primary_key=True),
    Column("text_id", ForeignKey("content_text.id"), nullable=False),
    Column("locale", String(length=40), nullable=False, default="us-en"),
    Column("text", Text, nullable=False),

    Column("user_id", Integer, ForeignKey("user_user.id"), nullable=True),
    Column("created_at", DateTime, nullable=False, default=datetime.utcnow),
)


version = Table(
    "content_version",
    metadata,

    Column("id", Integer, primary_key=True),
    Column("text_id", ForeignKey("content_text.id"), nullable=False),
    # Column("locale", String(length=40), nullable=False, default="us-en"),

    # This is automatically incremented for `text_id` and `locale` combination
    Column("version", SmallInteger, nullable=False),

    # This is the difference of this version from its previous one, for the same `text_id` and `locale`
    Column("delta", JSON, nullable=False),

    Column("user_id", Integer, ForeignKey("user_user.id"), nullable=True),
    Column("created_at", DateTime, nullable=False, default=datetime.utcnow),

    UniqueConstraint("text_id", "locale", name="unique_page_id_position"),
)


image = Table(
    "content_image",
    metadata,

    Column("id", Integer, primary_key=True),
    Column("path", String(length=200), nullable=False),
    Column("extension", String(length=10), nullable=False),

    Column("user_id", Integer, ForeignKey("user_user.id"), nullable=True),
    Column("created_at", DateTime, nullable=False, default=datetime.utcnow),
)
