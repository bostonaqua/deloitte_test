"""users table

Revision ID: 61433edda358
Revises: 
Create Date: 2018-08-18 05:28:03.102495

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61433edda358'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    users = op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    # ### end Alembic commands ###
    op.bulk_insert(users,
                   [
                       {'username':'admin',
                        'password_hash':'pbkdf2:sha256:50000$UGacVVGc$efef65ff2d3f35c77e0b3cba99d52b223e86ef48f1f93c421bc1474c634aee0c'}
                   ])


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
