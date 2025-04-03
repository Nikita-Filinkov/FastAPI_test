from sqlalchemy import Column, Integer, String

from src.database import Base


class Urls(Base):
    __tablename__ = 'Urls'

    id = Column(Integer, primary_key=True)
    urls = Column(String, nullable=False, unique=True)
    short_urls = Column(String, nullable=False)
