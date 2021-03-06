"""empty message

Revision ID: b3d5adf67fbb
Revises: 
Create Date: 2021-03-30 17:03:49.636508

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b3d5adf67fbb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('itemcode', sa.String(), nullable=True),
    sa.Column('kindname', sa.String(), nullable=True),
    sa.Column('unit', sa.String(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('day_bf_price', sa.Integer(), nullable=True),
    sa.Column('week_bf_price', sa.Integer(), nullable=True),
    sa.Column('two_week_bf_price', sa.Integer(), nullable=True),
    sa.Column('month_bf_price', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cart',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('itemcode', sa.String(), nullable=True),
    sa.Column('myprice', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cart')
    op.drop_table('product')
    # ### end Alembic commands ###
