"""empty message

Revision ID: a53adf50b872
Revises: 93997539dee0
Create Date: 2022-01-26 13:11:37.129539

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a53adf50b872'
down_revision = '93997539dee0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('cartera', 'parent_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('cartera', 'parent_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
