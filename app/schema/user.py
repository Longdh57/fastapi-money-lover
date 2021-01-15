from typing import Optional, List

from pydantic import BaseModel

from app.schema.base import ResponseSchemaBase


class Token(BaseModel):
    token: str


class UserLogin(BaseModel):
    code: int
    data: Optional[Token]


class Info(BaseModel):
    avatar: str
    introduction: str
    name: str
    roles: List[str]


class UserInfo(BaseModel):
    code: int
    data: Optional[Info]


class UserSchemaBase(BaseModel):
    full_name: Optional[str] = None
    username: Optional[str] = None
    email: Optional[str] = None
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False

    class Config:
        orm_mode = True


class UserDetailSchema(ResponseSchemaBase):
    class UserDetail(UserSchemaBase):
        id: int

    data: Optional[UserDetail]
