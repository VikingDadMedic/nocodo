from datetime import datetime

from sqlalchemy import (
    Table, Column, Integer, String, DateTime, SmallInteger, Boolean, ForeignKey, UniqueConstraint
)

from utils.database import metadata


page = Table(
    "interface_page",
    metadata,

    Column("id", Integer, primary_key=True),
    Column("url", String(length=200), unique=True)
)

block = Table(
    "interface_block",
    metadata,

    Column("id", Integer, primary_key=True),

    # Each block is always inside a page
    Column("page_id", ForeignKey("interface_page.id"), nullable=False),

    # A block can be inside another block
    Column("block_id", ForeignKey("interface_block.id"), nullable=True),

    # This is the position of this block among its siblings
    Column("position", SmallInteger, nullable=False, default=0),
    Column("class_name", String(length=200)),

    Column("is_email_verified", Boolean, nullable=False, default=False),
    Column("is_phone_verified", Boolean, nullable=False, default=False),

    Column("user_id", Integer, ForeignKey("user_user.id"), nullable=True),
    Column("created_at", DateTime, nullable=False, default=datetime.utcnow),

    UniqueConstraint("page_id", "block_id", "position", name="unique_page_id_block_id_position"),
)
