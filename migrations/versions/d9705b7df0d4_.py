"""empty message

Revision ID: d9705b7df0d4
Revises: bac12fd6684e
Create Date: 2023-07-21 18:52:26.590751

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd9705b7df0d4'
down_revision = 'bac12fd6684e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('encuesta_cerveza_id_fkey', 'encuesta', type_='foreignkey')
    op.drop_column('encuesta', 'cerveza_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('encuesta', sa.Column('cerveza_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('encuesta_cerveza_id_fkey', 'encuesta', 'cerveza', ['cerveza_id'], ['cerveza_id'])
    # ### end Alembic commands ###