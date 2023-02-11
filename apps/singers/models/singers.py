from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

from configs.databases import Base


class Singer(Base):
    __tablename__ = "singers"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(True), nullable=False, default=datetime.now())
    name = Column(String(length=100))
    company_id = Column(
        Integer, ForeignKey(column="companies.id"), index=True, primary_key=True
    )
