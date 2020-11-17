from typing import Optional

from pydantic import BaseModel


class TransactionSchemaBase(BaseModel):
    amount: Optional[int] = None
    description: Optional[str] = None
    category_id: Optional[int] = None
    wallet_id: Optional[int] = None

    class Config:
        orm_mode = True


class TransactionSchemaCreate(TransactionSchemaBase):
    amount: int
    category_id: int
    wallet_id: int


class TransactionSchemaUpdate(TransactionSchemaBase):
    amount: int
    category_id: int
    wallet_id: int


class TransactionSchema(TransactionSchemaBase):
    id: int
