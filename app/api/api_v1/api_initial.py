import random
from datetime import datetime

from fastapi import APIRouter
from fastapi_sqlalchemy import db

from app.helpers.enums import WalletType, CategoryType
from app.models import Wallet, Category, Transaction

router = APIRouter()


@router.post("")
async def initial_data():
    mock_data = {
        'wallet': [
            {'name': 'Tiền mặt', 'description': 'Tiền mặt', 'type': WalletType.TIEN_MAT.value},
            {'name': 'Thẻ ngân hàng', 'description': 'Thẻ ngân hàng VCB', 'type': WalletType.THE_NGAN_HANG.value},
            {'name': 'Thẻ tín dụng', 'description': 'Thẻ tín dụng', 'type': WalletType.THE_TIN_DUNG.value},
        ],
        'category': [
            {
                'name': 'Ăn uống',
                'description': 'Ăn uống',
                'quota': 4000000,
                'type': CategoryType.KHOAN_CHI.value,
                'icon': 'food-fork'
            },
            {
                'name': 'Xe cộ',
                'description': 'Xe cộ',
                'quota': 700000,
                'type': CategoryType.KHOAN_CHI.value,
                'icon': 'drive-service'
            },
            {
                'name': 'Y tế',
                'description': 'Y tế',
                'quota': 1000000,
                'type': CategoryType.KHOAN_CHI.value,
                'icon': 'healthcare'
            },
            {
                'name': 'Học tập',
                'description': 'Học tập',
                'quota': 1000000,
                'type': CategoryType.KHOAN_CHI.value,
                'icon': 'book'
            },
            {
                'name': 'Khoản chi khác',
                'description': 'Khoản chi khác',
                'quota': 0,
                'type': CategoryType.KHOAN_CHI.value,
                'icon': ''
            },
            {
                'name': 'Lương',
                'description': 'Lương',
                'quota': 0,
                'type': CategoryType.KHOAN_THU.value,
                'icon': 'income-salary'
            },
            {
                'name': 'Khoản thu khác',
                'description': 'Khoản thu khác',
                'quota': 0,
                'type': CategoryType.KHOAN_THU.value,
                'icon': ''
            },
        ]
    }
    db.session.bulk_insert_mappings(Wallet, mock_data['wallet'])
    db.session.bulk_insert_mappings(Category, mock_data['category'])
    db.session.flush()
    db.session.commit()
    return {"message": "OK"}


@router.post("/trans")
async def initial_transaction_data():
    wallet_cash = db.session.query(Category).filter(Wallet.type == WalletType.TIEN_MAT.value).first()

    if wallet_cash:
        cat_eat = db.session.query(Category).filter(Category.name == 'Ăn uống').first()
        if cat_eat:
            mock_data_trans = [
                {
                    'amount': random.randint(10, 500)*1000,
                    'description': 'Ăn sáng',
                    'date_tran': datetime.now().date(),
                    'category_id': cat_eat.id,
                    'wallet_id': wallet_cash.id,
                },
                {
                    'amount': random.randint(10, 500)*1000,
                    'description': 'Ăn trưa',
                    'date_tran': datetime.now().date(),
                    'category_id': cat_eat.id,
                    'wallet_id': wallet_cash.id,
                },
                {
                    'amount': random.randint(10, 500)*1000,
                    'description': 'Ăn tối',
                    'date_tran': datetime.now().date(),
                    'category_id': cat_eat.id,
                    'wallet_id': wallet_cash.id,
                },
            ]
            db.session.bulk_insert_mappings(Transaction, mock_data_trans)

        cat_car = db.session.query(Category).filter(Category.name == 'Xe cộ').first()
        if cat_eat:
            mock_data_trans = [
                {
                    'amount': 50000,
                    'description': 'Đổ xăng',
                    'date_tran': datetime.now().date(),
                    'category_id': cat_car.id,
                    'wallet_id': wallet_cash.id,
                },
                {
                    'amount': random.randint(10, 100)*1000,
                    'description': 'Bắt Grap',
                    'date_tran': datetime.now().date(),
                    'category_id': cat_car.id,
                    'wallet_id': wallet_cash.id,
                }
            ]
            db.session.bulk_insert_mappings(Transaction, mock_data_trans)

        cat_salary = db.session.query(Category).filter(Category.name == 'Lương').first()
        if cat_salary:
            mock_data_trans = [
                {
                    'amount': random.randint(10, 20)*1000*1000,
                    'description': 'Lương tháng',
                    'date_tran': datetime.now().date(),
                    'category_id': cat_salary.id,
                    'wallet_id': wallet_cash.id,
                }
            ]
            db.session.bulk_insert_mappings(Transaction, mock_data_trans)

    db.session.flush()
    db.session.commit()
    return {"message": "OK"}
