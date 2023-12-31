"""empty message

Revision ID: 40cee0a02e3b
Revises: 
Create Date: 2023-08-12 14:24:48.925601

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40cee0a02e3b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cerveza',
    sa.Column('cerveza_id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(), nullable=True),
    sa.Column('marca', sa.String(), nullable=True),
    sa.Column('porcentaje_alcohol', sa.Float(), nullable=True),
    sa.Column('estilo', sa.String(), nullable=True),
    sa.Column('ibus', sa.Integer(), nullable=True),
    sa.Column('color', sa.String(), nullable=True),
    sa.Column('sabor', sa.String(), nullable=True),
    sa.Column('ingrediente_adicional', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('cerveza_id')
    )
    op.create_table('encuesta',
    sa.Column('encuesta_id', sa.Integer(), nullable=False),
    sa.Column('consumo_previo', sa.Boolean(), nullable=True),
    sa.Column('pref_estilo', sa.String(), nullable=True),
    sa.Column('gusta_amarga', sa.Boolean(), nullable=True),
    sa.Column('pref_sabor', sa.String(), nullable=True),
    sa.Column('pref_alcohol', sa.Integer(), nullable=True),
    sa.Column('ingrediente_adic', sa.String(), nullable=True),
    sa.Column('completed_at', sa.DateTime(), nullable=True),
    sa.Column('cliente_id', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('encuesta_id')
    )
    op.create_table('favoritos',
    sa.Column('favoritos_id', sa.Integer(), nullable=False),
    sa.Column('cliente_id', sa.String(), nullable=True),
    sa.Column('cerveza_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cerveza_id'], ['cerveza.cerveza_id'], ),
    sa.PrimaryKeyConstraint('favoritos_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favoritos')
    op.drop_table('encuesta')
    op.drop_table('cerveza')
    # ### end Alembic commands ###
