from fastapi import APIRouter

from app.schema.user import UserLogin, UserInfo

router = APIRouter()


@router.post("/login", response_model=UserLogin)
async def login():
    return {
        "code": 200,
        "data": {
            "token": "admin-token"
        }
    }


@router.get("/info", response_model=UserInfo)
async def info():
    return {
        "code": 200,
        "data": {
            "avatar": "https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif",
            "introduction": "Hello Long",
            "name": "Super Admin",
            "roles": ["admin"]
        }
    }
