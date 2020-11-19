from typing import Optional

from pydantic import BaseModel


class WalletSchemaBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

    class Config:
        orm_mode = True


class WalletSchemaCreate(WalletSchemaBase):
    name: str


class WalletSchemaUpdate(WalletSchemaBase):
    pass


class WalletSchema(WalletSchemaBase):
    id: int