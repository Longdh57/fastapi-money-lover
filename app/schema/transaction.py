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
        category_name: str
        category_type: str

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


class TransactionTotalAmount(SchemaBase):
    class TotalAmount(BaseModel):
        khoan_thu: int = 0
        khoan_chi: int = 0
        cho_vay_di_vay: int = 0

    data: TotalAmount
