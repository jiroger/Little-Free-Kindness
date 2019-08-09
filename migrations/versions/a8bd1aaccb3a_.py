"""empty message

Revision ID: a8bd1aaccb3a
Revises: feca874298c6
Create Date: 2019-08-09 16:04:34.267903

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a8bd1aaccb3a'
down_revision = 'feca874298c6'
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
               nullable=False)
    # ### end Alembic commands ###
