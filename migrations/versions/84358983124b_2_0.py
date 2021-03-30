"""2.0

Revision ID: 84358983124b
Revises: 
Create Date: 2021-03-30 10:38:55.624370

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '84358983124b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('openId', sa.String(length=128), nullable=True),
    sa.Column('nickName', sa.String(length=50), nullable=True),
    sa.Column('gender', sa.Integer(), server_default='0', nullable=True),
    sa.Column('city', sa.String(length=50), nullable=True),
    sa.Column('province', sa.String(length=50), nullable=True),
    sa.Column('country', sa.String(length=50), nullable=True),
    sa.Column('avatarUrl', sa.String(length=128), nullable=True),
    sa.Column('preference', sa.Integer(), server_default='0', nullable=True),
    sa.Column('brightness', sa.Integer(), server_default='30', nullable=True),
    sa.Column('fontSize', sa.Integer(), server_default='14', nullable=True),
    sa.Column('background', sa.String(length=10), server_default='B1', nullable=True),
    sa.Column('turn', sa.String(length=10), server_default='T1', nullable=True),
    sa.Column('last_read', sa.Integer(), nullable=True),
    sa.Column('last_read_chapter_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('openId')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
