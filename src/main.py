import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from src.schemas.schema import SchemUrls
from src.services.service import UrlService

app = FastAPI()


@app.post('/', status_code=201)
async def post_url(base_url: SchemUrls):

    return await UrlService.download_in_base(str(base_url.url))


@app.get('/', status_code=307)
async def get_short_url(short_url):
    return RedirectResponse(await UrlService.find_url(short_url))


if __name__ == "__main__":
    uvicorn.run("src.main:app", host="127.0.0.1", port=8080, reload=True)
