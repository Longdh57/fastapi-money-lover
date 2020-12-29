from typing import Optional, List

from pydantic import BaseModel

from app.schema.base import SchemaBase, MetadataSchema


class WalletSchemaBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None

    class Config:
        orm_mode = True


class WalletListSchema(SchemaBase):
    class WalletList(WalletSchemaBase):
        id: int

    data: Optional[List[WalletList]]
    metadata: Optional[MetadataSchema]


class WalletDetailSchema(SchemaBase):
    class WalletDetail(WalletSchemaBase):
        id: int

    data: Optional[WalletDetail]


class WalletSchemaCreate(WalletSchemaBase):
    name: str

    class Config:
        schema_extra = {
            "name": "Tiền mặt",
            "description": "Tiền mặt để trong nhà"
        }


class WalletSchemaUpdate(WalletSchemaBase):
    pass
