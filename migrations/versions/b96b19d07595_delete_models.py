"""delete models

Revision ID: b96b19d07595
Revises: 
Create Date: 2023-02-12 15:54:39.519844

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b96b19d07595'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('singers_company_id_idx', table_name='singers')
    op.drop_table('singers')
    op.drop_table('companies')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('companies',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('companies_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='companies_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('singers',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('company_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['company_id'], ['companies.id'], name='singers_company_id_fkey'),
    sa.PrimaryKeyConstraint('id', 'company_id', name='singers_pkey')
    )
    op.create_index('singers_company_id_idx', 'singers', ['company_id'], unique=False)
    # ### end Alembic commands ###
