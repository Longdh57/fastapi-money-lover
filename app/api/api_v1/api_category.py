from datetime import datetime
from typing import Optional

from sqlalchemy import func
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from app import crud
from app.db.base_class import get_db
from app.helpers.enums import CategoryType
from app.models import Category, Transaction
from app.schema.base import ResponseSchemaBase
from app.utils.exception import AppBaseException
from app.helpers.response_helper import ResponseHelper
from app.utils.utils import get_from_date_and_to_date
from app.schema.category import CategoryListSchema, CategoryDetailSchema, CategorySchemaCreate

router = APIRouter()


@router.get('', response_model=CategoryListSchema)
async def get(
        db: Session = Depends(get_db),
        type: Optional[CategoryType] = None,
        month: int = None,
        year: int = None,
        all: bool = False,
        page: int = 0,
        pageSize: int = 100
):
    page = page
    page_size = pageSize
    _query = crud.category.q()
    if type is not None:
        _query = _query.filter(Category.type == type)
    if all is False:
        _query = _query.filter(Category.deleted == None)

    from_date, to_date = get_from_date_and_to_date(month=month, year=year)

    total_amounts = db.query(Transaction.category_id, func.sum(Transaction.amount).label('total_amount')).filter(
        Transaction.date_tran >= from_date,
        Transaction.date_tran < to_date
    ).group_by(Transaction.category_id).all()
    mapping_cat_amount = {total_amount.category_id: total_amount.total_amount for total_amount in total_amounts}

    categories = _query.order_by(Category.name.asc()).all()
    cat_data = []
    for category in categories:
        category = category.__dict__
        category['total_amount'] = mapping_cat_amount[category['id']] if category['id'] in mapping_cat_amount else 0
        cat_data.append(category)
    total_items = 10
    return {
        'data': categories,
        'metadata': ResponseHelper.pagination_meta(page, page_size, total_items)
    }


@router.post('', response_model=CategoryDetailSchema)
async def create(*, db: Session = Depends(get_db), category: CategorySchemaCreate):
    db_category = Category(
        name=category.name,
        description=category.description,
        quota=category.quota,
        type=category.type
    )
    category = crud.category.create(db=db, obj_in=db_category)
    return {"data": category}


@router.get('/{category_id}', response_model=CategoryDetailSchema)
async def get(category_id: int, db: Session = Depends(get_db)):
    category = crud.category.get(db=db, id=category_id, error_out=True)
    return {'data': category}


@router.put('/{category_id}/archive', response_model=ResponseSchemaBase)
async def archive(*, db: Session = Depends(get_db), category_id: int):
    category = crud.category.get(db=db, id=category_id, error_out=True)
    if db.query(Transaction).filter(Transaction.category_id == category_id).count() > 0 and category.deleted is None:
        raise AppBaseException(status_code=400, code='400', message="Không thể archive category này")
    crud.category.update(db=db, db_obj=category, obj_in={
        'deleted': datetime.now() if category.deleted is None else None
    })
    return {'message': 'Success'}
