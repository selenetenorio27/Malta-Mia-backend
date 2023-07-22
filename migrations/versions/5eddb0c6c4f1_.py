"""empty message

Revision ID: 5eddb0c6c4f1
Revises: 416779116735
Create Date: 2023-07-21 13:39:09.613565

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5eddb0c6c4f1'
down_revision = '416779116735'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cerveza', sa.Column('ingrediente_adicional', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cerveza', 'ingrediente_adicional')
    # ### end Alembic commands ###