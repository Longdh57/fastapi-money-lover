from fastapi import APIRouter

from app.api.api_v1 import wallets, categories, transactions

router = APIRouter()
router.include_router(wallets.router, tags=["wallets"], prefix="/wallet")
router.include_router(categories.router, tags=["categories"], prefix="/category")
router.include_router(transactions.router, tags=["transactions"], prefix="/transaction")