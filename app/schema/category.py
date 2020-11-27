from typing import Optional, List

from pydantic import BaseModel

from app.helpers.enums import CategoryType
from app.schema.base import SchemaBase


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


class CategorySchema(SchemaBase):
    class CategoryListSchema(CategorySchemaBase):
        id: int

    code: int = 200
    success: bool = True
    message: str = ""
    data: Optional[List[CategoryListSchema]]
