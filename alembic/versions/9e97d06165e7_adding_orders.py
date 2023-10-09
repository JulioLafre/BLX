"""Adding Orders

Revision ID: 9e97d06165e7
Revises: 
Create Date: 2023-10-09 13:40:44.289740

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9e97d06165e7'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orders',
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('delivery_adress', sa.String(), nullable=True),
    sa.Column('delivery_type', sa.String(), nullable=True),
    sa.Column('note', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['products.product_id'], name='fk_product_order'),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], name='fk_user_order'),
    sa.PrimaryKeyConstraint('order_id')
    )
    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_orders_order_id'), ['order_id'], unique=False)

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_orders_order_id'))

    op.drop_table('orders')
    # ### end Alembic commands ###
