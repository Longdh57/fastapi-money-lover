from datetime import datetime

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from app import crud
from app.api import deps
from app.models.transaction import Transaction
from app.schema.transaction import TransactionSchemaCreate, TransactionSchema, TransactionSchemaUpdate, \
    TransactionSchemaCreateResponse

router = APIRouter()


@router.get("", response_model=TransactionSchema)
async def get(db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 100):
    transactions = crud.transaction.get_multi(db=db, skip=skip, limit=limit)
    return {"data": transactions}


@router.post("", response_model=TransactionSchemaCreateResponse)
async def create(*, db: Session = Depends(deps.get_db), transaction: TransactionSchemaCreate):
    wallet = crud.wallet.get(db=db, id=transaction.wallet_id)
    category = crud.category.get(db=db, id=transaction.category_id)
    date_tran = datetime.strptime(transaction.date_tran, '%d/%m/%Y').date()
    db_transaction = Transaction(
        amount=transaction.amount,
        description=transaction.description,
        date_tran=date_tran,
        category_id=wallet.id,
        wallet_id=category.id
    )
    db_transaction = crud.transaction.create(db=db, obj_in=db_transaction)
    return {"data": {
        "amount": db_transaction.amount,
        "description": db_transaction.description,
        "date_tran": db_transaction.date_tran,
        "category_id": db_transaction.category_id,
        "wallet_id": db_transaction.wallet_id
    }}


@router.get("/{transaction_id}", response_model=TransactionSchema)
async def get(transaction_id: int, db: Session = Depends(deps.get_db)):
    transaction = crud.transaction.get(db=db, id=transaction_id, error_out=True)
    return transaction


@router.put("/{transaction_id}", response_model=TransactionSchemaUpdate)
async def update(*, transaction_id: int, db: Session = Depends(deps.get_db), transaction_data: TransactionSchemaUpdate):
    crud.wallet.get(db=db, id=transaction_data.wallet_id)
    crud.category.get(db=db, id=transaction_data.category_id)
    transaction = crud.transaction.get(db=db, id=transaction_id, error_out=True)
    transaction = crud.transaction.update(db=db, db_obj=transaction, obj_in=transaction_data)
    return transaction
