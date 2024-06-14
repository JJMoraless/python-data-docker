from app.config.database import Base
from sqlalchemy import Column, Integer, String

from sqlalchemy.orm import relationship


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    password = Column(String)

    sales = relationship("SaleModel", back_populates="user")
    emails_acounts = relationship("EmailAccountModel", back_populates="user")

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
