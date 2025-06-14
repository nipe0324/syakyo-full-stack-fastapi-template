import uuid
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import func, select

from app.api.deps import CurrentUser, SessionDep
from app.database.item_repo import Item
from app.models import ItemPublic, ItemsPublic, ItemCreate

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


@router.get("/{id}", response_model=ItemPublic)
def read_item(
    session: SessionDep, current_user: CurrentUser, id: uuid.UUID
) -> ItemPublic:
    """
    Get item by ID.
    """
    item = item_repo.get_by_id(session, id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    if not current_user.is_superuser and (item.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not engouh permissions")
    return item


@router.post("/", response_model=ItemPublic)
def create_item(
    *, session: SessionDep, current_user: CurrentUser, item_in: ItemCreate
) -> ItemPublic:
    """
    Create new item.
    """
    item = item_repo.create_item(session=session, item_create=item_in, owner_id=current_user.id)
    return item
