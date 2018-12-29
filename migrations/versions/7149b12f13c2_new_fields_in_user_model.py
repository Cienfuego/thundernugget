"""new fields in user model

Revision ID: 7149b12f13c2
Revises: 336f8325434a
Create Date: 2018-12-29 16:54:32.974426

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7149b12f13c2'
down_revision = '336f8325434a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
