from typing import List

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from app.api import deps
from app import crud
from app.models.category import Category
from app.schema.category import CategorySchemaCreate, CategorySchema

router = APIRouter()


@router.get("", response_model=List[CategorySchema])
async def get(db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 100):
    categories = crud.category.get_multi(db=db, skip=skip, limit=limit)
    return categories


@router.post("", response_model=CategorySchemaCreate)
async def create(*, db: Session = Depends(deps.get_db), category: CategorySchemaCreate):
    db_category = Category(
        name=category.name,
        description=category.description,
        quota=category.quota,
        type=category.type
    )
    db_category = crud.category.create(db=db, obj_in=db_category)
    return db_category


@router.get("/{category_id}", response_model=CategorySchema)
async def get(category_id: int, db: Session = Depends(deps.get_db)):
    category = crud.category.get(db=db, id=category_id, error_out=True)
    return category
