from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from apps.configs.databases import Base


class Singer(Base):
    __tablename__ = "singers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime(True), nullable=False, default=datetime.now())
    name = Column(String(length=100))
    company_id = Column(Integer, ForeignKey(column="companies.id"), index=True)

    company = relationship("Company", backref="singer", foreign_keys=company_id)
