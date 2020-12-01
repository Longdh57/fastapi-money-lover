from typing import List

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from app import crud
from app.api import deps
from app.models import Category
from app.schema.category import CategoryListSchema, CategoryDetailSchema, CategorySchemaCreate
from app.helpers.response_helper import ResponseHelper

router = APIRouter()


@router.get("", response_model=CategoryListSchema)
async def get(db: Session = Depends(deps.get_db), page: int = 0, pageSize: int = 10):
    page = page
    page_size = pageSize
    categories = crud.category.get_multi(db=db, skip=page, limit=pageSize)
    total_items = 10
    return {
        "data": categories,
        "metadata": ResponseHelper.pagination_meta(page, page_size, total_items)
    }


@router.post("", response_model=CategoryDetailSchema)
async def create(*, db: Session = Depends(deps.get_db), category: CategorySchemaCreate):
    db_category = Category(
        name=category.name,
        description=category.description,
        quota=category.quota,
        type=category.type
    )
    category = crud.category.create(db=db, obj_in=db_category)
    return {"data": category}


@router.get("/{category_id}", response_model=CategoryDetailSchema)
async def get(category_id: int, db: Session = Depends(deps.get_db)):
    category = crud.category.get(db=db, id=category_id, error_out=True)
    return {"data": category}
