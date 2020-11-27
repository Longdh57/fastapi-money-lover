from fastapi import Depends

from .base import CRUDBase
from app.models import Wallet, Category, Transaction
from app.schema.wallet import WalletSchemaCreate, WalletSchemaUpdate
from app.schema.category import CategorySchemaCreate, CategorySchemaUpdate
from app.schema.transaction import TransactionSchemaCreate, TransactionSchemaUpdate
from app.api import deps

wallet = CRUDBase[Wallet, WalletSchemaCreate, WalletSchemaUpdate](Wallet, Depends(deps.get_db))
category = CRUDBase[Category, CategorySchemaCreate, CategorySchemaUpdate](Category, Depends(deps.get_db))
transaction = CRUDBase[Transaction, TransactionSchemaCreate, TransactionSchemaUpdate](Transaction, Depends(deps.get_db))
