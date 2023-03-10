"""empty message

Revision ID: 93997539dee0
Revises: 1ae1c21e77fb
Create Date: 2022-01-25 10:53:55.877701

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '93997539dee0'
down_revision = '1ae1c21e77fb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cartera',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.Column('nivel', sa.String(length=2), nullable=True),
    sa.Column('serial', sa.String(length=20), nullable=True),
    sa.Column('descripcion', sa.String(length=150), nullable=True),
    sa.Column('cartera', sa.Boolean(), nullable=True),
    sa.Column('tercero', sa.Boolean(), nullable=True),
    sa.Column('proveedor', sa.Boolean(), nullable=True),
    sa.Column('centroCosto', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('registro_documentos_contables',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tipodocumento', sa.String(length=15), nullable=True),
    sa.Column('consecutivo', sa.Integer(), nullable=True),
    sa.Column('fecha', sa.Date(), nullable=True),
    sa.Column('proveedor_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['proveedor_id'], ['proveedor.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('registro_documentos_contables')
    op.drop_table('cartera')
    # ### end Alembic commands ###
