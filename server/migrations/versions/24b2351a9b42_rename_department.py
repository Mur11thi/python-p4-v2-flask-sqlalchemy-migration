"""rename department

Revision ID: 24b2351a9b42
Revises: 16fa2a81d604
Create Date: 2024-06-26 11:47:17.201237

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24b2351a9b42'
down_revision = '16fa2a81d604'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('department', 'departments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('departments', 'department')
    # ### end Alembic commands ###
