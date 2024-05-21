from src.config.database import Base
from sqlalchemy import Column, Integer, String

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Detail(Base):
    __tablename__ = "details"

    id = Column(Integer, primary_key=True, index=True)
    price = Column(Integer)
    description = Column(String)
    img = Column(String)
    
    sale_id = Column(Integer, ForeignKey("sales.id"))
    sale = relationship("Sale", back_populates="details")
    
    item_id = Column(Integer, ForeignKey("items.id"))
    item = relationship("Item", back_populates="details")
