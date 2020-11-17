from typing import List

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from app.api import deps
from app import crud
from app.models.transaction import Transaction
from app.schema.transaction import TransactionSchemaCreate, TransactionSchema

router = APIRouter()


@router.get("", response_model=List[TransactionSchema])
async def get(db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 100):
    transactions = crud.transaction.get_multi(db=db, skip=skip, limit=limit)
    return transactions


@router.post("", response_model=TransactionSchemaCreate)
async def create(*, db: Session = Depends(deps.get_db), transaction: TransactionSchemaCreate):
    wallet = crud.wallet.get(db=db, id=transaction.wallet_id)
    if wallet is None:
        return
    category = crud.category.get(db=db, id=transaction.category_id)
    if category is None:
        return
    db_transaction = Transaction(
        amount=transaction.amount,
        description=transaction.description,
        category_id=transaction.category_id,
        wallet_id=transaction.wallet_id
    )
    db_transaction = crud.transaction.create(db=db, obj_in=db_transaction)
    return db_transaction
