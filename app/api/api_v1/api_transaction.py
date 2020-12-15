from datetime import datetime, timedelta
from typing import Optional

from sqlalchemy import func
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from app import crud
from app.db.base_class import get_db
from app.models.category import Category
from app.models.transaction import Transaction
from app.helpers.response_helper import ResponseHelper
from app.schema.transaction import TransactionSchemaCreate, TransactionSchemaUpdate, TransactionListSchema, \
    TransactionDetailSchema, TransactionTotalAmount

router = APIRouter()


@router.get("", response_model=TransactionListSchema)
async def get(db: Session = Depends(get_db), *, wallet_id: int, category_id: int = None, page: int = 0,
              pageSize: int = 100):
    page = page
    page_size = pageSize
    from_date = (datetime.today().replace(day=1) - timedelta(days=1)).replace(day=25).date()
    to_date = datetime.today().replace(day=25).date()

    crud.wallet.get(id=wallet_id, error_out=True)
    if category_id:
        crud.category.get(id=category_id, error_out=True)

    _query = db.query(Transaction, Category) \
        .join(Transaction, Transaction.category_id == Category.id).filter(
        Transaction.date_tran >= from_date,
        Transaction.date_tran < to_date,
        Transaction.wallet_id == wallet_id
    )
    if category_id:
        _query = _query.filter(Transaction.category_id == category_id)
    query = _query.order_by(Transaction.date_tran.desc(), Transaction.id.desc()).all()

    transactions = [{
        "id": item.Transaction.id,
        "amount": item.Transaction.amount,
        "description": item.Transaction.description,
        "date_tran": item.Transaction.date_tran,
        "category_id": item.Transaction.category_id,
        "category_name": item.Category.name,
        "category_type": item.Category.type,
        "wallet_id": item.Transaction.wallet_id
    } for item in query]
    total_items = 10

    return {
        "data": transactions,
        "metadata": ResponseHelper.pagination_meta(page, page_size, total_items)
    }


@router.get("/total-amount", response_model=TransactionTotalAmount)
async def total_amount(db: Session = Depends(get_db), *, wallet_id: Optional[int] = None):
    if wallet_id:
        crud.wallet.get(id=wallet_id, error_out=True)
    from_date = (datetime.today().replace(day=1) - timedelta(days=1)).replace(day=25).date()
    to_date = datetime.today().replace(day=25).date()

    _query = db.query(func.sum(Transaction.amount).label('total_amount'), Category.type) \
        .join(Transaction, Transaction.category_id == Category.id) \
        .filter(Transaction.date_tran >= from_date, Transaction.date_tran < to_date)

    if wallet_id:
        _query = _query.filter(Transaction.wallet_id == wallet_id)

    total_trans = _query.group_by(Category.type).all()
    total_trans = {total_tran.type: total_tran.total_amount for total_tran in total_trans}

    return {
        "data": {
            'khoan_thu': total_trans['khoan_thu'] if 'khoan_thu' in total_trans else 0,
            'khoan_chi': total_trans['khoan_chi'] if 'khoan_chi' in total_trans else 0,
            'cho_vay_di_vay': total_trans['cho_vay_di_vay'] if 'cho_vay_di_vay' in total_trans else 0
        }
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
async def update(*, db: Session = Depends(get_db), transaction_id: int, transaction_data: TransactionSchemaUpdate):
    if transaction_data.wallet_id:
        crud.wallet.get(db=db, id=transaction_data.wallet_id)
    if transaction_data.category_id:
        crud.category.get(db=db, id=transaction_data.category_id)
    transaction = crud.transaction.get(db=db, id=transaction_id, error_out=True)
    transaction = crud.transaction.update(db=db, db_obj=transaction, obj_in=transaction_data)
    return {"data": transaction}
