from fastapi import APIRouter

from src.api.short_urls import router

main_router = APIRouter()

main_router.include_router(router)
