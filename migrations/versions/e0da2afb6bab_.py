"""empty message

Revision ID: e0da2afb6bab
Revises: f3bcc0012065
Create Date: 2020-12-28 22:44:27.345419

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e0da2afb6bab'
down_revision = 'f3bcc0012065'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('category', sa.Column('deleted', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('category', 'deleted')
    # ### end Alembic commands ###
