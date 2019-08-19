"""empty message

Revision ID: 47ff57773455
Revises: 1c88a196e64a
Create Date: 2019-08-14 11:13:32.431617

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '47ff57773455'
down_revision = '1c88a196e64a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('notes', 'lookupId',
               existing_type=postgresql.UUID(),
               type_=sa.String(length=36),
               existing_nullable=True)
    op.alter_column('notes', 'message',
               existing_type=sa.VARCHAR(length=100),
               nullable='False')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('notes', 'message',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    op.alter_column('notes', 'lookupId',
               existing_type=sa.String(length=36),
               type_=postgresql.UUID(),
               existing_nullable=True)
    # ### end Alembic commands ###