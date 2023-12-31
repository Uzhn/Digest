"""first

Revision ID: 839bf4069293
Revises: 
Create Date: 2023-07-24 11:20:01.327372

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '839bf4069293'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('subscriptions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('source_name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('digests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.Column('subscription_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['subscription_id'], ['subscriptions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_subscription',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('subscription_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['subscription_id'], ['subscriptions.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], )
    )
    op.create_table('digest_post_association',
    sa.Column('digest_id', sa.Integer(), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['digest_id'], ['digests.id'], ),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], )
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('digest_post_association')
    op.drop_table('user_subscription')
    op.drop_table('posts')
    op.drop_table('digests')
    op.drop_table('users')
    op.drop_table('subscriptions')
    # ### end Alembic commands ###
