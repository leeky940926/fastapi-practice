import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

RDS_DB_NAME = os.environ.get("RDS_DB_NAME")
RDS_USERNAME = os.environ.get("RDS_USERNAME")
RDS_PASSWORD = os.environ.get("RDS_PASSWORD")
RDS_HOSTNAME = os.environ.get("RDS_HOSTNAME")
RDS_PORT = os.environ.get("RDS_PORT")

Base = declarative_base()

DATABASE_URL = f"postgresql://{RDS_USERNAME}:{RDS_PASSWORD}@{RDS_HOSTNAME}:{RDS_PORT}/{RDS_DB_NAME}"

engine = create_engine(url=DATABASE_URL)

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
