from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from src.schemas.schema import SchemUrls
from src.services.service import UrlService, shorten_url

router = APIRouter()


@router.post('/', status_code=201)
async def post_url(base_url: SchemUrls):
    base_url = str(base_url.url)
    short_url = shorten_url(base_url)
    await UrlService.download_in_base(base_url, short_url)
    return {'short_url': short_url}


@router.get('/', status_code=307)
async def get_short_url(short_url):
    return RedirectResponse(await UrlService.find_url(short_url))
