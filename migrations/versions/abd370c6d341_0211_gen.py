"""0211 gen

Revision ID: abd370c6d341
Revises: 0f53e3014219
Create Date: 2023-02-11 15:21:23.206214

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'abd370c6d341'
down_revision = '0f53e3014219'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('companies', sa.Column('representitive', sa.String(length=10), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('companies', 'representitive')
    # ### end Alembic commands ###