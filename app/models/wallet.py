from sqlalchemy import Column, String, Text
from app.db.base_class import BareBaseModel


class Wallet(BareBaseModel):
    name = Column(String, unique=True, index=True)
    description = Column(Text)
