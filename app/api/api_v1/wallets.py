from typing import List

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from app import crud
from app.api import deps
from app.models.wallet import Wallet
from app.schema.wallet import WalletSchemaCreate, WalletSchema

router = APIRouter()


@router.get("", response_model=List[WalletSchema])
async def get(db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 100):
    wallets = crud.wallet.get_multi(db=db, skip=skip, limit=limit)
    return wallets


@router.post("", response_model=WalletSchemaCreate)
async def create(*, db: Session = Depends(deps.get_db), wallet: WalletSchemaCreate):
    db_wallet = Wallet(
        name=wallet.name,
        description=wallet.description
    )
    db_wallet = crud.wallet.create(db=db, obj_in=db_wallet)
    return db_wallet
