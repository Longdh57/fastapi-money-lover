from datetime import datetime
from app.models.base_model import BareBaseModel
from sqlalchemy import Column, Text, Integer, BigInteger, Date, DateTime


class Transaction(BareBaseModel):
    amount = Column(BigInteger, default=0)
    description = Column(Text)
    date_tran = Column(Date, default=datetime.today().date())
    category_id = Column(Integer, index=True)
    wallet_id = Column(Integer, index=True)
    deleted = Column(DateTime, nullable=True)
