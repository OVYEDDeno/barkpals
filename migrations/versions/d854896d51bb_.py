"""empty message

Revision ID: d854896d51bb
Revises: 877d22999d4c
Create Date: 2023-03-19 22:21:01.779526

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd854896d51bb'
down_revision = '877d22999d4c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('dogs', schema=None) as batch_op:
        batch_op.alter_column('weight',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=2),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('dogs', schema=None) as batch_op:
        batch_op.alter_column('weight',
               existing_type=sa.Float(precision=2),
               type_=sa.REAL(),
               existing_nullable=False)

    # ### end Alembic commands ###