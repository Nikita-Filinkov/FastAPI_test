import pyshorteners
from sqlalchemy import select, insert

from src.database import async_session_maker
from src.models.urls_table import Urls
from sqlalchemy.exc import IntegrityError


def shorten_url(base_url):
    return pyshorteners.Shortener().tinyurl.short(base_url)


class UrlService:

    @classmethod
    async def download_in_base(cls, base_url):
        short_url = shorten_url(base_url)
        async with async_session_maker() as session:
            try:
                query = insert(Urls).values(urls=base_url, short_urls=short_url)
                await session.execute(query)
                await session.commit()
            except IntegrityError:
                return None

    @classmethod
    async def find_url(cls, short_url):
        async with async_session_maker() as session:
            query = select(Urls.urls).where(Urls.short_urls == short_url)
            result = await session.execute(query)
            url = result.scalar_one_or_none()
            return url

