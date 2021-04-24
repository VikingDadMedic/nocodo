from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class PageEdit(BaseModel):
    url: str
    title: Optional[str]
    keywords: Optional[str]
    description: Optional[str]
    is_live: Optional[bool]


class Page(BaseModel):
    id: int
    url: str

    title: Optional[str]
    keywords: Optional[str]
    description: Optional[str]
    is_live: Optional[bool]

    user_id: int
    created_at: datetime


class BlockEdit(BaseModel):
    page_id: int
    parent_block_id: Optional[int]

    parameter_name: Optional[str]
    position: int
    class_names: dict
    styles: Optional[dict]
    event_handlers: Optional[dict]


class Block(BaseModel):
    id: int
    page_id: int
    parent_block_id: Optional[int]

    parameter_name: Optional[str]
    position: int
    class_names: dict
    styles: Optional[dict]
    event_handlers: Optional[dict]

    user_id: int
    created_at: datetime
