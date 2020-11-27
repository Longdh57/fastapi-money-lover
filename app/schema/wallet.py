from typing import Optional, List

from pydantic import BaseModel

from app.schema.base import SchemaBase


class WalletSchemaBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

    class Config:
        orm_mode = True


class WalletSchemaCreate(WalletSchemaBase):
    name: str


class WalletSchemaUpdate(WalletSchemaBase):
    pass


class WalletSchema(SchemaBase):
    class WalletListSchema(WalletSchemaBase):
        id: int

    code: int = 200
    success: bool = True
    message: str = ""
    data: Optional[List[WalletListSchema]]
