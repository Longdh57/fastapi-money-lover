from app.db.base_class import BareBaseModel
from sqlalchemy import Column, String, Text, Integer

from app.helpers.enums import CategoryType


class Category(BareBaseModel):
    name = Column(String, unique=True, index=True)
    description = Column(Text)
    quota = Column(Integer, default=0)
    type = Column(String, default=CategoryType.KHOAN_CHI.value, index=True)
