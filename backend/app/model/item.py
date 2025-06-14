import uuid

from sqlmodel import Field, SQLModel


# Shared properties
class ItemBase(SQLModel):
    title: str = Field(min_length=1, max_length=255)
    descrption: str | None = Field(default=None, max_length=255)


class ItemCreate(ItemBase):
    pass


class ItemUpdate(ItemBase):
    title: str | None = Field(default=None, min_length=1, max_length=255) # type: ignore


class ItemPublic(ItemBase):
    id: uuid.UUID
    owner_id: uuid.UUID


class ItemsPublic(SQLModel):
    data: list[ItemPublic]
    count: int

