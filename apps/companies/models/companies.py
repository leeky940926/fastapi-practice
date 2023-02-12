from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from apps.configs.databases import Base


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(timezone=True), nullable=False, default=datetime.now())
    name = Column(String(length=100), nullable=False)
