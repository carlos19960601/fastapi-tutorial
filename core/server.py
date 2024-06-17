from fastapi import Depends, FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware

from api import router
from core.config import config
from core.fastapi.dependencies import Logging
from core.fastapi.middlewares import SQLAlchemyMiddleware


def init_routers(app: FastAPI) -> None:
    app.include_router(router)


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
    app = FastAPI(
        title="FastAPI Boilerplate",
        docs_url=None if config.ENV == "prod" else "/docs",
        redoc_url=None if config.ENV == "prod" else "/redoc",
        dependencies=[Depends(Logging)],
        middleware=make_middleware(),
    )
    init_routers(app)
    return app


app = create_app()
