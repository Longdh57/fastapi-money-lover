from typing import List

from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from app import crud
from app.api import deps
from app.helpers.response_helper import ResponseHelper
from app.models.wallet import Wallet
from app.schema.wallet import WalletSchemaCreate, WalletListSchema, WalletSchemaUpdate, WalletDetailSchema

router = APIRouter()


@router.get("", response_model=WalletListSchema)
async def get(page: int = 0, pageSize: int = 10):
    page = page
    page_size = pageSize
    wallets = crud.wallet.get_multi(skip=page, limit=page_size)
    total_items = 4
    return {
        "data": wallets,
        "metadata": ResponseHelper.pagination_meta(page, page_size, total_items)
    }


@router.get("/{wallet_id}", response_model=WalletDetailSchema)
async def get(wallet_id: int):
    wallet = crud.wallet.get(id=wallet_id, error_out=True)
    return {"data": wallet}


@router.post("", response_model=WalletDetailSchema)
async def create(*, wallet: WalletSchemaCreate):
    db_wallet = Wallet(
        name=wallet.name,
        description=wallet.description
    )
    wallet = crud.wallet.create(obj_in=db_wallet)
    return {"data": wallet}


@router.put("/{wallet_id}", response_model=WalletDetailSchema)
async def update(*, wallet_id: int, db: Session = Depends(deps.get_db), wallet_data: WalletSchemaUpdate):
    wallet = crud.wallet.get(db=db, id=wallet_id, error_out=True)
    wallet = crud.wallet.update(db=db, db_obj=wallet, obj_in=wallet_data)
    return {"data": wallet}
