from sqlalchemy import Column, String, Boolean

from app.models.base_model import BareBaseModel


class User(BareBaseModel):
    full_name = Column(String, nullable=True)
    username = Column(String(20), index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
