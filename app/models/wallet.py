from sqlalchemy import Column, String, Text
from app.models.base_model import BareBaseModel


class Wallet(BareBaseModel):
    name = Column(String, unique=True, index=True)
    description = Column(Text)
