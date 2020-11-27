from datetime import date
from typing import Optional, List

from pydantic import BaseModel

from app.schema.base import SchemaBase


class TransactionSchemaBase(BaseModel):
    amount: Optional[int] = None
    description: Optional[str] = None
    date_tran: Optional[date] = None
    category_id: Optional[int] = None
    wallet_id: Optional[int] = None

    class Config:
        orm_mode = True


class TransactionSchemaCreate(TransactionSchemaBase):
    amount: int
    date_tran: str
    category_id: int
    wallet_id: int


class TransactionSchemaUpdate(TransactionSchemaBase):
    amount: int
    category_id: int
    wallet_id: int


class TransactionSchema(SchemaBase):
    class TransactionListSchema(TransactionSchemaBase):
        id: int

    code: int = 200
    success: bool = True
    message: str = ""
    data: Optional[List[TransactionListSchema]]


class TransactionSchemaCreateResponse(SchemaBase):
    code: int = 200
    success: bool = True
    message: str = ""
    data: Optional[TransactionSchemaBase]
