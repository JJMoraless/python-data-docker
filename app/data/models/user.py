from app.config.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .empleoyee_manager import EmployeeManagerModel


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

    managers = relationship(
        "UserModel",
        secondary="employees_managers",
        primaryjoin=id == EmployeeManagerModel.employee_id,
        secondaryjoin=id == EmployeeManagerModel.manager_id,
        backref="employees",  # crea employees para acceder a los empleados de un manager
    )

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
