from app.db.base_class import BareBaseModel
from sqlalchemy import Column, String, Text, Integer


class Category(BareBaseModel):
    name = Column(String, unique=True, index=True)
    description = Column(Text)
    quota = Column(Integer, default=0)
