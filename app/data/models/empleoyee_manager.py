from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database import Base


class EmployeeManagerModel(Base):
    __tablename__ = "employees_managers"

    employee_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    manager_id = Column(Integer, ForeignKey("users.id"), primary_key=True)

    employee = relationship("UserModel", foreign_keys=[employee_id])
    manager = relationship("UserModel", foreign_keys=[manager_id])

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
