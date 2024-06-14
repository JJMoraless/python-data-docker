from app.config.database import Base
from sqlalchemy import Column, Integer, String, Double

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class SaleModel(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    currency = Column(String)

    items_quantity = Column(Integer)
    sub_total_amount = Column(Integer)
    total_discount_amount = Column(Double)
    total_tax_amount = Column(Double)
    total = Column(Double)

    # realtionships
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("UserModel", back_populates="sales")
    details = relationship("Detail", back_populates="sale")


    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


