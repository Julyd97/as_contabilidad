"""empty message

Revision ID: b23010a689dc
Revises: 8862403c4485
Create Date: 2021-07-29 12:19:47.126161

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b23010a689dc'
down_revision = '8862403c4485'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('email', table_name='user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('email', 'user', ['email'], unique=False)
    # ### end Alembic commands ###