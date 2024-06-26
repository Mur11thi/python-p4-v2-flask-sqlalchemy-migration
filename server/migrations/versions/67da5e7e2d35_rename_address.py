"""rename address

Revision ID: 67da5e7e2d35
Revises: 24b2351a9b42
Create Date: 2024-06-26 12:06:33.965550

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67da5e7e2d35'
down_revision = '24b2351a9b42'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("departments" , "address" , new_column_name = "location")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("departments" , "location" , new_column_name = "address")
    # ### end Alembic commands ###
