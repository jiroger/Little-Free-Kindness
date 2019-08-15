"""empty message

Revision ID: f2c790aeab60
Revises: b03b8fa780b7
Create Date: 2019-08-15 13:05:15.538832

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f2c790aeab60'
down_revision = 'b03b8fa780b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('notes', sa.Column('numDislikes', sa.Integer(), nullable=True))
    op.add_column('notes', sa.Column('numLikes', sa.Integer(), nullable=True))
    op.alter_column('notes', 'message',
               existing_type=sa.VARCHAR(length=100),
               nullable='False')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('notes', 'message',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    op.drop_column('notes', 'numLikes')
    op.drop_column('notes', 'numDislikes')
    # ### end Alembic commands ###
