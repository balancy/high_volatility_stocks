"""Rename some fields in Stock model, add Analytics Recommendations

Revision ID: d9887a98f40e
Revises: aaa03014016d
Create Date: 2021-09-22 15:02:11.422943

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'd9887a98f40e'
down_revision = 'aaa03014016d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('stocks', sa.Column('market__cap', sa.String(), nullable=True))
    op.add_column('stocks', sa.Column('p_e', sa.Float(), nullable=True))
    op.add_column('stocks', sa.Column('fwd__p_e', sa.Float(), nullable=True))
    op.add_column('stocks', sa.Column('p_s', sa.Float(), nullable=True))
    op.add_column('stocks', sa.Column('p_b', sa.Float(), nullable=True))
    op.add_column('stocks', sa.Column('dividend', sa.Float(), nullable=True))
    op.add_column('stocks', sa.Column('curr__r', sa.Float(), nullable=True))
    op.add_column('stocks', sa.Column('quick__r', sa.Float(), nullable=True))
    op.add_column('stocks', sa.Column('gross__m', sa.Float(), nullable=True))
    op.add_column('stocks', sa.Column('oper__m', sa.Float(), nullable=True))
    op.add_column('stocks', sa.Column('profit__m', sa.Float(), nullable=True))
    op.add_column('stocks', sa.Column('avg__volume', sa.String(), nullable=True))
    op.add_column('stocks', sa.Column('recom', sa.Float(), nullable=True))
    op.drop_column('stocks', 'ps')
    op.drop_column('stocks', 'curr_r')
    op.drop_column('stocks', 'forward_pe')
    op.drop_column('stocks', 'div')
    op.drop_column('stocks', 'market_cap')
    op.drop_column('stocks', 'gross_m')
    op.drop_column('stocks', 'pe')
    op.drop_column('stocks', 'profit_m')
    op.drop_column('stocks', 'oper_m')
    op.drop_column('stocks', 'volume')
    op.drop_column('stocks', 'quick_r')
    op.drop_column('stocks', 'pb')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('stocks', sa.Column('pb', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.add_column('stocks', sa.Column('quick_r', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.add_column('stocks', sa.Column('volume', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('stocks', sa.Column('oper_m', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.add_column('stocks', sa.Column('profit_m', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.add_column('stocks', sa.Column('pe', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.add_column('stocks', sa.Column('gross_m', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.add_column('stocks', sa.Column('market_cap', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('stocks', sa.Column('div', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.add_column('stocks', sa.Column('forward_pe', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.add_column('stocks', sa.Column('curr_r', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.add_column('stocks', sa.Column('ps', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.drop_column('stocks', 'recom')
    op.drop_column('stocks', 'avg__volume')
    op.drop_column('stocks', 'profit__m')
    op.drop_column('stocks', 'oper__m')
    op.drop_column('stocks', 'gross__m')
    op.drop_column('stocks', 'quick__r')
    op.drop_column('stocks', 'curr__r')
    op.drop_column('stocks', 'dividend')
    op.drop_column('stocks', 'p_b')
    op.drop_column('stocks', 'p_s')
    op.drop_column('stocks', 'fwd__p_e')
    op.drop_column('stocks', 'p_e')
    op.drop_column('stocks', 'market__cap')
    # ### end Alembic commands ###
