from datetime import datetime
from app.db.base_class import BareBaseModel
from sqlalchemy import Column, Text, Integer, BigInteger, Date


class Transaction(BareBaseModel):
    amount = Column(BigInteger, default=0)
    description = Column(Text)
    date_tran = Column(Date, default=datetime.today().date())
    category_id = Column(Integer, index=True)
    wallet_id = Column(Integer, index=True)
