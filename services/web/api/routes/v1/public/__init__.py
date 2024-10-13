from fastapi import APIRouter
from .currency import currency_router

public_router: APIRouter = APIRouter(
    prefix=""
)

public_router.include_router(currency_router)