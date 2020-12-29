from sqlalchemy import Column, String, Text

from app.helpers.enums import WalletType
from app.models.base_model import BareBaseModel


class Wallet(BareBaseModel):
    name = Column(String, unique=True, index=True)
    description = Column(Text)
    type = Column(String, default=WalletType.TIEN_MAT.value, index=True)
