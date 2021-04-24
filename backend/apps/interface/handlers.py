from datetime import datetime
from typing import Mapping
from fastapi import APIRouter, Depends, status

from utils.database import database, get_database
from apps.user.schema import User
from apps.auth.utils import get_current_user
from .models import page, block
from .schema import PageEdit, Page, BlockEdit, Block


interface_router = APIRouter()


@interface_router.post("/page", response_model=Page, status_code=status.HTTP_201_CREATED)
async def create_page(
        form_data: PageEdit,
        current_user: User = Depends(get_current_user),
        db: database = Depends(get_database)
) -> Mapping:
    values = {
        "url": form_data.url,
        "user_id": current_user.id,
        "created_at": datetime.utcnow()
    }
    page_id = await db.execute(query=page.insert(), values=values)

    # Read this newly inserted page
    _page = await db.fetch_one(query=page.select().where(
        page.c.id == page_id
    ))
    return _page


@interface_router.post("/block", response_model=Page, status_code=status.HTTP_201_CREATED)
async def create_page(
        form_data: BlockEdit,
        current_user: User = Depends(get_current_user),
        db: database = Depends(get_database)
) -> Mapping:
    values = {
        "page_id": form_data.page_id,
        "parent_block_id": form_data.parent_block_id,
        "parameter_name": form_data.parameter_name,
        "position": form_data.position,
        "class_names": form_data.class_names,
        "styles": form_data.styles,
        "event_handlers": form_data.event_handlers,

        "user_id": current_user.id,
        "created_at": datetime.utcnow()
    }
    block_id = await db.execute(query=block.insert(), values=values)

    # Read this newly inserted block
    _block = await db.fetch_one(query=block.select().where(
        block.c.id == block_id
    ))
    return _block
