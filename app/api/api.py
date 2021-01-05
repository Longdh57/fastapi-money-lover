from fastapi import APIRouter

from app.api.api_v1 import api_login, api_healthcheck, api_wallet, api_category, api_transaction, api_user

router = APIRouter()
router.include_router(api_login.router, tags=["login"], prefix="/login")
router.include_router(api_healthcheck.router, tags=["healthcheck"], prefix="/healthcheck")
router.include_router(api_category.router, tags=["categories"], prefix="/category")
router.include_router(api_transaction.router, tags=["transactions"], prefix="/transaction")
router.include_router(api_wallet.router, tags=["wallets"], prefix="/wallet")
router.include_router(api_user.router, tags=["user"], prefix="/user")
