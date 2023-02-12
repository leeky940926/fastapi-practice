from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from apps.configs.databases import Base


class Album(Base):
    __tablename__ = "albums"

    id = Column(Integer, primary_key=True)
    name = Column(String(length=200), nullable=False)
    singer_id = Column(ForeignKey("singers.id"), index=True)

    singer = relationship("Singer", backref="album", foreign_keys=singer_id)
