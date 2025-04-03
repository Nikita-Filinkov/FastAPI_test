from pydantic import BaseModel, HttpUrl


class SchemUrls(BaseModel):
    url: HttpUrl

