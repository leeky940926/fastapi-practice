from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from databases import Base


class City(Base):
    __tablename__ = "city"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(True), nullable=False, default=datetime.now())
    name = Column(String(10), nullable=False)


class Town(Base):
    __tablename__ = "town"

    id = Column(Integer, primary_key=True)
    city_id = Column(ForeignKey(column=City.id), nullable=False)
    created_at = Column(DateTime(True), nullable=False, default=datetime.now())
    name = Column(String(10), nullable=False)

    city = relationship(City)
