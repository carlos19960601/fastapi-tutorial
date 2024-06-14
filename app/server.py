from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware

from app.container import Container
from app.user.adapter.input.api import router as user_router
from core.config import config
from core.fastapi.middlewares.sqlalchemy import SQLAlchemyMiddleware


def init_routers(app: FastAPI) -> None:
    app.include_router(user_router)


def make_middleware() -> list[Middleware]:
    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        ),
        Middleware(SQLAlchemyMiddleware),
    ]

    return middleware


def create_app() -> FastAPI:
    container = Container()

    app = FastAPI(
        docs_url=None if config.ENV == "prod" else "/docs",
        redoc_url=None if config.ENV == "prod" else "/redoc",
        middleware=make_middleware(),
    )
    app.container = container

    init_routers(app)
    return app


app = create_app()
