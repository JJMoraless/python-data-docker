from app.config.database import Base
from sqlalchemy import Column, Integer, String


class CountryModel(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    code_iso_3 = Column(String, unique=True)
    code_phone = Column(String)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
