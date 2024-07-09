"""empty message

Revision ID: 83a63273052a
Revises: b7f1172bc710
Create Date: 2024-07-08 21:48:57.711461

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83a63273052a'
down_revision = 'b7f1172bc710'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('formacao', sa.Column('nome', sa.String(length=50), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('formacao', 'nome')
    # ### end Alembic commands ###
