"""empty message

Revision ID: a46f1b1d4d82
Revises: 
Create Date: 2022-02-15 10:30:55.647125

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a46f1b1d4d82'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('example',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('something', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('example')
    # ### end Alembic commands ###