# Import all the models, so that Base has them before being
# imported by Alembic
from app.models.base_model import Base  # noqa
from app.models.category import Category  # noqa
from app.models.wallet import Wallet  # noqa
from app.models.transaction import Transaction  # noqa
from app.models.user import User  # noqa
