from app.config.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey

from sqlalchemy.orm import relationship


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    password = Column(String)

    role_id = Column(Integer, ForeignKey("user_roles.id"))
    role = relationship("UserRoleModel", back_populates="users")

    sales = relationship("SaleModel", back_populates="user")
    emails_acounts = relationship("EmailAccountModel", back_populates="user")

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
