from datetime import datetime

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from app import crud
from app.api import deps
from app.helpers.response_helper import ResponseHelper
from app.models.transaction import Transaction
from app.schema.transaction import TransactionSchemaCreate, TransactionSchemaUpdate, \
    TransactionListSchema, TransactionDetailSchema

router = APIRouter()


@router.get("", response_model=TransactionListSchema)
async def get(page: int = 0, pageSize: int = 10):
    page = page
    page_size = pageSize
    transactions = crud.transaction.get_multi(skip=page, limit=page_size)
    total_items = 10
    return {
        "data": transactions,
        "metadata": ResponseHelper.pagination_meta(page, page_size, total_items)
    }


@router.get("/{transaction_id}", response_model=TransactionDetailSchema)
async def get(transaction_id: int):
    transaction = crud.transaction.get(id=transaction_id, error_out=True)
    return {"data": transaction}


@router.post("", response_model=TransactionDetailSchema)
async def create(*, transaction: TransactionSchemaCreate):
    wallet = crud.wallet.get(id=transaction.wallet_id)
    category = crud.category.get(id=transaction.category_id)
    date_tran = datetime.strptime(transaction.date_tran, '%d/%m/%Y').date()
    db_transaction = Transaction(
        amount=transaction.amount,
        description=transaction.description,
        date_tran=date_tran,
        category_id=wallet.id,
        wallet_id=category.id
    )
    db_transaction = crud.transaction.create(obj_in=db_transaction)
    return {"data": db_transaction}


@router.put("/{transaction_id}", response_model=TransactionDetailSchema)
async def update(*, db: Session = Depends(deps.get_db), transaction_id: int, transaction_data: TransactionSchemaUpdate):
    if transaction_data.wallet_id:
        crud.wallet.get(db=db, id=transaction_data.wallet_id)
    if transaction_data.category_id:
        crud.category.get(db=db, id=transaction_data.category_id)
    transaction = crud.transaction.get(db=db, id=transaction_id, error_out=True)
    transaction = crud.transaction.update(db=db, db_obj=transaction, obj_in=transaction_data)
    return {"data": transaction}
