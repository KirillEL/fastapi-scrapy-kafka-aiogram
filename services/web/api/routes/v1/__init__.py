from fastapi import APIRouter

from .public import public_router

main_router: APIRouter = APIRouter(
    prefix="/api/v1"
)

main_router.include_router(public_router)


__all__ = ['main_router']