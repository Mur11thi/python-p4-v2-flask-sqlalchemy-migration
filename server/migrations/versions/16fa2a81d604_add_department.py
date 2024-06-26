"""add Department

Revision ID: 16fa2a81d604
Revises: 58e90bc11748
Create Date: 2024-06-26 11:37:57.881313

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16fa2a81d604'
down_revision = '58e90bc11748'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('department')
    # ### end Alembic commands ###
