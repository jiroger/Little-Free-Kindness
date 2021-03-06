"""empty message

Revision ID: 11bd03df671d
Revises: f2c790aeab60
Create Date: 2019-08-15 15:34:59.135342

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11bd03df671d'
down_revision = 'f2c790aeab60'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('notes', 'message',
               existing_type=sa.VARCHAR(length=100),
               nullable='False')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('notes', 'message',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    # ### end Alembic commands ###
