"""empty message

Revision ID: 0eda63f2d7b6
Revises: 64674f3014de
Create Date: 2023-07-14 17:43:36.521958

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0eda63f2d7b6'
down_revision = '64674f3014de'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('encuesta', sa.Column('cliente_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'encuesta', 'cliente', ['cliente_id'], ['cliente_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'encuesta', type_='foreignkey')
    op.drop_column('encuesta', 'cliente_id')
    # ### end Alembic commands ###