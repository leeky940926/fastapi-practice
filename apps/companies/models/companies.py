from configs.databases import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True)
    name = Column(String(length=100))

    singers = relationship("Singer", back_populates="singers")
