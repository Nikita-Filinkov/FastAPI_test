from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from src.schemas.schema import SchemUrls
from src.services.service import UrlService

router = APIRouter(
    prefix="/",
    tags=["ShortUrls"]
)


@router.post('', status_code=201)
async def post_url(base_url: SchemUrls):
    return await UrlService.download_in_base(str(base_url.url))


@router.get('', status_code=307)
async def get_short_url(short_url):
    return RedirectResponse(await UrlService.find_url(short_url))
