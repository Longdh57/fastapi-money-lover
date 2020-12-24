from typing import Optional, List

from pydantic import BaseModel

from app.helpers.enums import CategoryType
from app.schema.base import SchemaBase, MetadataSchema


class CategorySchemaBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    quota: Optional[int] = 0
    type: Optional[str] = None
    icon: Optional[str] = None

    class Config:
        orm_mode = True


class CategoryListSchema(SchemaBase):
    class CategoryList(CategorySchemaBase):
        id: int
        total_amount: int = 0

    data: Optional[List[CategoryList]]
    metadata: Optional[MetadataSchema]


class CategoryDetailSchema(SchemaBase):
    class CategoryDetail(CategorySchemaBase):
        id: int

    data: Optional[CategoryDetail]


class CategorySchemaCreate(CategorySchemaBase):
    name: str
    type: CategoryType


class CategorySchemaUpdate(CategorySchemaBase):
    name: str
