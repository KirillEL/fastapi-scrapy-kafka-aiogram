from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .routes.v1 import main_router


def init_routers(_app: FastAPI) -> None:
    _app.include_router(main_router)


def init_middlewares(_app: FastAPI) -> None:
    _app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )


def create_app() -> FastAPI:
    _app = FastAPI(
        title="Web service",
        docs_url="/api/v1/docs",
        description="Web service",
        debug=True,
        version="1.0.0"
    )
    init_routers(_app=_app)
    init_middlewares(_app=_app)

    return _app


app: FastAPI = create_app()
