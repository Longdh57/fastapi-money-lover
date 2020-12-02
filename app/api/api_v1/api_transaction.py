from datetime import datetime, timedelta

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from app import crud
from app.api import deps
from app.helpers.response_helper import ResponseHelper
from app.models.category import Category
from app.models.transaction import Transaction
from app.schema.transaction import TransactionSchemaCreate, TransactionSchemaUpdate, TransactionListSchema, \
    TransactionDetailSchema

router = APIRouter()


@router.get("", response_model=TransactionListSchema)
async def get(db: Session = Depends(deps.get_db), *, wallet_id: int, page: int = 0, pageSize: int = 100):
    page = page
    page_size = pageSize
    crud.wallet.get(id=wallet_id, error_out=True)
    from_date = (datetime.today().replace(day=1) - timedelta(days=1)).replace(day=25).date()
    to_date = datetime.today().replace(day=25).date()
    query = db.query(Transaction, Category) \
        .join(Transaction, Transaction.category_id == Category.id).filter(
        Transaction.date_tran >= from_date,
        Transaction.date_tran < to_date,
        Transaction.wallet_id == wallet_id
    ).order_by(Transaction.date_tran.desc()).all()
    transactions = []
    for item in query:
        transactions.append({
            "id": item.Transaction.id,
            "amount": item.Transaction.amount,
            "description": item.Transaction.description,
            "date_tran": item.Transaction.date_tran,
            "category_id": item.Transaction.category_id,
            "category_name": item.Category.name,
            "category_type": item.Category.type,
            "wallet_id": item.Transaction.wallet_id
        })
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
    crud.wallet.get(id=transaction.wallet_id, error_out=True)
    crud.category.get(id=transaction.category_id, error_out=True)
    date_tran = datetime.strptime(transaction.date_tran, '%d/%m/%Y').date()
    db_transaction = Transaction(
        amount=transaction.amount,
        description=transaction.description,
        date_tran=date_tran,
        category_id=transaction.category_id,
        wallet_id=transaction.wallet_id
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
