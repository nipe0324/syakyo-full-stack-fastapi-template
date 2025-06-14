import uuid

from sqlmodel import Field, SQLModel, Session, Relationship

from app.database.user_repo import User
from app.model.item import ItemCreate, ItemUpdate

class Item(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    title: str = Field(min_length=1, max_length=255)
    description: str | None = Field(default=None, max_length=255)
    owner_id: uuid.UUID = Field(foreign_key="user.id", nullable=False, ondelete="CASCADE")
    # owner: User | None = Relationship(back_populates="items")


def get_by_id(*, session: Session, id: uuid.UUID) -> Item | None:
    return session.get(Item, id)


def create_item(*, session: Session, item_create: ItemCreate, owner_id: int) -> Item:
    new_item = Item.model_validate(item_create, update={"owner_id": owner_id})
    session.add(new_item)
    session.commit()
    session.refresh(new_item)
    return new_item


def update_item(*, session: Session, existing_item: Item, item_update: ItemUpdate) -> Item:
    update_dict = item_update.model_dump(exclude_unset=True)
    existing_item.sqlmodel_update(update_dict)
    session.add(existing_item)
    session.commit()
    session.refresh(existing_item)
    return existing_item


def delete_item(*, session: Session, existing_item: Item) -> None:
    session.delete(existing_item)
    session.commit()
    return
