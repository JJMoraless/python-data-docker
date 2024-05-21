from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_URL = "postgresql://jhon:123@posgrest:5432/ia_facilpos"

engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()
