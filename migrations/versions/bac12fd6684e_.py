"""empty message

Revision ID: bac12fd6684e
Revises: 5eddb0c6c4f1
Create Date: 2023-07-21 18:37:59.672761

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bac12fd6684e'
down_revision = '5eddb0c6c4f1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('encuesta', sa.Column('cerveza_id', sa.Integer(), nullable=True))
    op.drop_constraint('encuesta_cerveza_recomendada_id_fkey', 'encuesta', type_='foreignkey')
    op.create_foreign_key(None, 'encuesta', 'cerveza', ['cerveza_id'], ['cerveza_id'])
    op.drop_column('encuesta', 'cerveza_recomendada_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('encuesta', sa.Column('cerveza_recomendada_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'encuesta', type_='foreignkey')
    op.create_foreign_key('encuesta_cerveza_recomendada_id_fkey', 'encuesta', 'cerveza', ['cerveza_recomendada_id'], ['cerveza_id'])
    op.drop_column('encuesta', 'cerveza_id')
    # ### end Alembic commands ###
