import uuid

from sqlmodel import Field, SQLModel, Session, Relationship

from app.database.user_repo import User
from app.models import ItemCreate

class Item(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    title: str = Field(min_length=1, max_length=255)
    descrption: str | None = Field(default=None, max_length=255)
    owner_id: uuid.UUID = Field(foreign_key="user.id", nullable=False, ondelete="CASCADE")
    owner: User | None = Relationship(back_populates="items")


def get_by_id(*, session: Session, item_id: uuid.UUID) -> Item | None:
    return session.get(User, item_id)


def create_item(*, session: Session, item_create: ItemCreate, owner_id: int) -> Item:
    item = Item.model_validate(item_create, update={"owner_id": owner_id})
    session.add(item)
    session.commit()
    session.refresh(item)
    return item
