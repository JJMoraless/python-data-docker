from app.config.database import Base
from sqlalchemy import Column, Integer, String, Boolean

from sqlalchemy.orm import relationship


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    price = Column(Integer)
    description = Column(String)
    img = Column(String, nullable=True)
    details = relationship("Detail", back_populates="item")
    is_active = Column(Boolean, default=True)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
