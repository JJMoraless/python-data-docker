from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from . import envs

DB_URL = envs.DB_URL

engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()
