"""empty message

Revision ID: 877d22999d4c
Revises: b784b9cf43ac
Create Date: 2023-03-19 21:50:29.269080

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '877d22999d4c'
down_revision = 'b784b9cf43ac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('dogs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('owner_id', sa.Integer(), nullable=False))
        batch_op.alter_column('weight',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=2),
               existing_nullable=False)
        batch_op.create_foreign_key(None, 'owner', ['owner_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('dogs', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.alter_column('weight',
               existing_type=sa.Float(precision=2),
               type_=sa.REAL(),
               existing_nullable=False)
        batch_op.drop_column('owner_id')

    # ### end Alembic commands ###