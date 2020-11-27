from typing import Optional, List

from pydantic import BaseModel


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
