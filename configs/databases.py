import os

from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

RDS_DB_NAME = os.environ.get("RDS_DB_NAME")
RDS_USERNAME = os.environ.get("RDS_USERNAME")
RDS_PASSWORD = os.environ.get("RDS_PASSWORD")
RDS_HOSTNAME = os.environ.get("RDS_HOSTNAME")
RDS_PORT = os.environ.get("RDS_PORT")

POSTGRES_INDEXES_NAMING_CONVENTION = {
    "ix": "%(column_0_label)s_idx",
    "uq": "%(table_name)s_%(column_0_name)s_key",
    "ck": "%(table_name)s_%(constraint_name)s_check",
    "fk": "%(table_name)s_%(column_0_name)s_fkey",
    "pk": "%(table_name)s_pkey",
}
metadata = MetaData(naming_convention=POSTGRES_INDEXES_NAMING_CONVENTION)
Base = declarative_base(metadata=metadata)
target_metadata = Base.metadata

DATABASE_URL = f"postgresql://{RDS_USERNAME}:{RDS_PASSWORD}@{RDS_HOSTNAME}:{RDS_PORT}/{RDS_DB_NAME}"

engine = create_engine(url=DATABASE_URL, echo=True)

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
