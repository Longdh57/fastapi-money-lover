from typing import Optional

from pydantic import BaseModel


class CategorySchemaBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    quota: Optional[int] = None

    class Config:
        orm_mode = True


class CategorySchemaCreate(CategorySchemaBase):
    name: str


class CategorySchemaUpdate(CategorySchemaBase):
    name: str


class CategorySchema(CategorySchemaBase):
    id: int
