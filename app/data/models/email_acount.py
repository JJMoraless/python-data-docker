from app.config.database import Base
from sqlalchemy import Column, Integer, String

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class EmailAccountModel(Base):
    __tablename__ = "email_acounts"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    provider = Column(String, nullable=True)
    email = Column(String)
    password = Column(String)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("UserModel", back_populates="emails_acounts")

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
