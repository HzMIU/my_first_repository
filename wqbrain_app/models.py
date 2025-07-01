from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Alpha(Base):
    __tablename__ = 'alpha'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    value = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
