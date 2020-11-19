from typing import Optional

from pydantic import BaseModel

from app.helpers.enums import CategoryType


class CategorySchemaBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    quota: Optional[int] = None
    type: Optional[str] = None

    class Config:
        orm_mode = True


class CategorySchemaCreate(CategorySchemaBase):
    name: str
    type: CategoryType


class CategorySchemaUpdate(CategorySchemaBase):
    name: str


class CategorySchema(CategorySchemaBase):
    id: int
