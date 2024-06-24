from app.config.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class UserRoleModel(Base):
    __tablename__ = "user_roles"

    id = Column(Integer, primary_key=True, index=True)
    name_role = Column(String, unique=True, index=True)

    users = relationship("UserModel", back_populates="role")
