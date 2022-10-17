"""empty message

Revision ID: b02bd00b39c0
Revises: 0dce6f426074
Create Date: 2022-06-04 19:43:17.296054

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b02bd00b39c0'
down_revision = '0dce6f426074'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cartera', sa.Column('naturaleza', sa.Boolean(), nullable=True))
    op.add_column('cartera', sa.Column('tipo', sa.String(length=15), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cartera', 'tipo')
    op.drop_column('cartera', 'naturaleza')
    # ### end Alembic commands ###
