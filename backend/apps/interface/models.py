from datetime import datetime

from sqlalchemy import (
    Table, Column, Integer, String, DateTime, SmallInteger, Boolean, JSON, ForeignKey, UniqueConstraint
)

from utils.database import metadata


page = Table(
    "interface_page",
    metadata,

    Column("id", Integer, primary_key=True),

    # This URL can be a format string with identifiers for use in React Router
    Column("url", String(length=200), nullable=False, unique=True),

    Column("title", String(length=200), nullable=True),
    Column("keywords", String(length=200), nullable=True),
    Column("description", String(length=200), nullable=True),
    Column("is_live", Boolean, default=False),

    Column("user_id", Integer, ForeignKey("user_user.id"), nullable=False),
    Column("created_at", DateTime, nullable=False, default=datetime.utcnow)
)


block = Table(
    "interface_block",
    metadata,

    Column("id", Integer, primary_key=True),

    # Each block is always inside a page
    Column("page_id", ForeignKey("interface_page.id"), nullable=False),

    # A block can be inside another block
    Column("parent_block_id", ForeignKey("interface_block.id"), nullable=True),

    # This is the name of the parameter, in the parent block, if this block is passed to another as child
    # This is nullable since a block can reside directly inside a page
    Column("parameter_name", String(length=60), nullable=True),

    # This is the positing of this block among its siblings which are all passed to the parent
    Column("position", SmallInteger, nullable=False),

    Column("class_names", JSON, nullable=False),
    Column("styles", JSON, nullable=True),
    Column("event_handlers", JSON, nullable=True),

    Column("user_id", Integer, ForeignKey("user_user.id"), nullable=False),
    Column("created_at", DateTime, nullable=False, default=datetime.utcnow),

    UniqueConstraint("page_id", "parent_block_id", "parameter_name", "position", name="unique_hierarchy_of_block"),
)
