from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from app import crud
from app.api import deps
from app.helpers.enums import CategoryType
from app.models import Category
from app.schema.category import CategoryListSchema, CategoryDetailSchema, CategorySchemaCreate
from app.helpers.response_helper import ResponseHelper

router = APIRouter()


@router.get("", response_model=CategoryListSchema)
async def get(page: int = 0, pageSize: int = 100, type: str = CategoryType.KHOAN_CHI.value):
    page = page
    page_size = pageSize
    categories = crud.category.q(Category.type == type).order_by(Category.name.asc()).all()
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
