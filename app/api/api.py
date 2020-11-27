from fastapi import APIRouter

from app.api.api_v1 import api_wallet, api_category, api_transaction, api_user

router = APIRouter()
router.include_router(api_wallet.router, tags=["wallets"], prefix="/wallet")
router.include_router(api_category.router, tags=["categories"], prefix="/category")
router.include_router(api_transaction.router, tags=["transactions"], prefix="/transaction")
router.include_router(api_user.router, tags=["user"], prefix="/user")
