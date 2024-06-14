from app.config.database import Base
from sqlalchemy import Column, Integer

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Detail(Base):
    __tablename__ = "details"

    id = Column(Integer, primary_key=True, index=True)
    price = Column(Integer)
    quantity = Column(Integer)
    total = Column(Integer)
    discount_amount  = Column(Integer, nullable=True)
    
    sale_id = Column(Integer, ForeignKey("sales.id"))
    sale = relationship("SaleModel", back_populates="details")
    
    item_id = Column(Integer, ForeignKey("items.id"))
    item = relationship("Item", back_populates="details")
