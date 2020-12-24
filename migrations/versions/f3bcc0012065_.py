"""empty message

Revision ID: f3bcc0012065
Revises: 538e5dc9c310
Create Date: 2020-12-24 14:26:39.384102

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f3bcc0012065'
down_revision = '538e5dc9c310'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('category', sa.Column('icon', sa.String(length=20), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('category', 'icon')
    # ### end Alembic commands ###
