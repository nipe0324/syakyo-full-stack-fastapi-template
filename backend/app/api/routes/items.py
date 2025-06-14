import uuid
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import func, select

from app.api.deps import CurrentUser, SessionDep
from app.database.item import Item
from app.models import ItemsPublic

router = APIRouter(prefix="/items", tags=["items"])


@router.get("/", response_model=ItemsPublic)
def read_items(
    session: SessionDep, current_user: CurrentUser, skip: int = 0, limit: int = 100
) -> ItemsPublic:
    """
    Retrieve items.
    """

    if current_user.is_superuser:
        count_statement = select(func.count()).select_from(Item)
        count = session.exec(count_statement).one()
        statement = select(Item).offset(skip).limit(limit)
        items = session.exec(statement).all()
    else:
        count_statement = select(func.count()).select_from(Item).where(Item.owner_id == current_user.id)
        count = session.exec(count_statement).one()
        statement = select(Item).where(Item.owner_id == current_user.id).offset(skip).limit(limit)
        items = session.exec(statement).all()

    return ItemsPublic(data=items, count=count)

