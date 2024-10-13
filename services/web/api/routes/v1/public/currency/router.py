from fastapi import APIRouter

currency_router: APIRouter = APIRouter(
    prefix="/currency",
    tags=["Currency"]
)

