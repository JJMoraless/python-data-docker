from app.config.database import Base
from sqlalchemy import Column, Integer

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Detail(Base):
    __tablename__ = "details"

    price = Column(Integer)
    quantity = Column(Integer)
    total = Column(Integer)
    discount_amount = Column(Integer, nullable=True)

    sale_id = Column(Integer, ForeignKey("sales.id"), primary_key=True)
    sale = relationship("SaleModel", back_populates="details")

    item_id = Column(Integer, ForeignKey("items.id"), primary_key=True)
    item = relationship("Item", back_populates="details")

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
