import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

DB_URI = os.getenv('MYSQL_URI', 'mysql+pymysql://user:password@localhost/wqbrain')

engine = create_engine(DB_URI)
SessionLocal = sessionmaker(bind=engine)


def init_db():
    Base.metadata.create_all(engine)
