from app.db.base_class import BareBaseModel
from sqlalchemy import Column, Text, Integer, BigInteger


class Transaction(BareBaseModel):
    amount = Column(BigInteger, default=0)
    description = Column(Text)
    category_id = Column(Integer, index=True)
    wallet_id = Column(Integer, index=True)
