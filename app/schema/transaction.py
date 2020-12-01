from datetime import date
from typing import Optional, List

from pydantic import BaseModel

from app.schema.base import SchemaBase, MetadataSchema


class TransactionSchemaBase(BaseModel):
    amount: Optional[int] = None
    description: Optional[str] = None
    date_tran: Optional[date] = None
    category_id: Optional[int] = None
    wallet_id: Optional[int] = None

    class Config:
        orm_mode = True


class TransactionListSchema(SchemaBase):
    class TransactionSchema(TransactionSchemaBase):
        id: int

    data: Optional[List[TransactionSchema]]
    metadata: Optional[MetadataSchema]


class TransactionDetailSchema(SchemaBase):
    class TransactionDetail(TransactionSchemaBase):
        id: int

    data: Optional[TransactionDetail]


class TransactionSchemaCreate(TransactionSchemaBase):
    amount: int
    date_tran: str
    category_id: int
    wallet_id: int


class TransactionSchemaUpdate(TransactionSchemaBase):
    pass
