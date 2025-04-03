from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from decouple import config

from src.config import get_db_url

# DB_HOST = config('DB_HOST')
# DB_PORT = config('DB_PORT')
# DB_USER = config('DB_USER')
# DB_PASS = config('DB_PASS')
# DB_NAME = config('DB_NAME')

DATABASE_URL = get_db_url()

engine = create_async_engine(DATABASE_URL)

async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class Base(DeclarativeBase):
    pass
