from typing import Any

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi_sqlalchemy import db
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.security import get_password_hash
from app.db.base_class import get_db
from app.models import User
from app.schema.base import DataResponse
from app.schema.token import Token
from app.schema.user import UserDetailSchema

router = APIRouter()


@router.post("", response_model=DataResponse[Token])
def login_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username
    password = form_data.password
    if username == 'admin' and password == 'secret123':
        return DataResponse().success_response({
            "access_token": 'xxx'
        })
    else:
        return DataResponse().custom_response(resp_code='400', message='Error Request')


@router.post("/get-password-hash")
def get_password(passsword: str):
    return get_password_hash(passsword)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.API_PREFIX}/login")


@router.get("/test-data", response_model=DataResponse)
def test(token: str = Depends(oauth2_scheme)):
    return DataResponse().success_response({
        "token": token
    })


def fake_decode_token(token):
    first_user = db.session.query(User).first()
    print(first_user)
    return UserDetailSchema(
        id=first_user.id,
        full_name=first_user.full_name,
        username=first_user.username,
        email=first_user.email
    )


async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    return user


@router.get("/me")
async def read_users_me(current_user: UserDetailSchema = Depends(get_current_user)):
    return current_user
