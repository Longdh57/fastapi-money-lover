"""empty message

Revision ID: 244cb6b2b556
Revises: f9ae1e2f5738
Create Date: 2020-11-18 14:20:59.857030

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '244cb6b2b556'
down_revision = 'f9ae1e2f5738'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('category', sa.Column('type', sa.String(), nullable=True))
    op.create_index(op.f('ix_category_type'), 'category', ['type'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_category_type'), table_name='category')
    op.drop_column('category', 'type')
    # ### end Alembic commands ###
