from src.config.database import Base
from sqlalchemy import Column, Integer, String

from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(Integer)
    name = Column(String)
    password = Column(String)

    sales = relationship("Sale", back_populates="user")
