from src.config.database import Base
from sqlalchemy import Column, Integer, String

from sqlalchemy.orm import relationship


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    price = Column(Integer)
    description = Column(String)
    img = Column(String)
    
    
    details = relationship("Detail", back_populates="item")
