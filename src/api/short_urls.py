from fastapi import FastAPI, APIRouter

from src.schemas.schema import SchemUrls
from src.services.service import shorten_url

router = APIRouter(
    prefix="/",
    tags=["ShortUrls"]
)


@router.post('')
async def download_url(url: SchemUrls, base_url):
    short_url = shorten_url(base_url)
    return short_url


@router.get('/{shorten_url_id}')
async def get_short_url_router(shorten_url_id: str) -> SchemUrls:
    pass
