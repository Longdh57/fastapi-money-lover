from typing import Optional

from pydantic import BaseModel


class SchemaBase(BaseModel):
    __abstract__ = True

    code: int
    success: bool
    message: str
