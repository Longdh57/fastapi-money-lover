from .base import CRUDBase
from app.models import Wallet, Category, Transaction
from app.schema.wallet import WalletSchemaCreate, WalletSchemaUpdate
from app.schema.category import CategorySchemaCreate, CategorySchemaUpdate
from app.schema.transaction import TransactionSchemaCreate, TransactionSchemaUpdate

wallet = CRUDBase[Wallet, WalletSchemaCreate, WalletSchemaUpdate](Wallet)
category = CRUDBase[Category, CategorySchemaCreate, CategorySchemaUpdate](Category)
transaction = CRUDBase[Transaction, TransactionSchemaCreate, TransactionSchemaUpdate](Transaction)
