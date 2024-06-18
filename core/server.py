from fastapi import Depends, FastAPI, Request
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from api import router
from core.config import config
from core.exceptions.base import CustomException
from core.fastapi.dependencies import Logging
from core.fastapi.middlewares import AuthenticationMiddleware, SQLAlchemyMiddleware
from core.fastapi.middlewares.authentication import AuthBackend


def on_auth_error(request: Request, exc: Exception):
    status_code, error_code, message = 402, None, str(str)
    if isinstance(exc, CustomException):
        status_code = int(exc.code)
        error_code = exc.error_code
        message = exc.message

    return JSONResponse(
        status_code=status_code,
        content={"error_code": error_code, "message": message},
    )


def init_routers(app: FastAPI) -> None:
    app.include_router(router)


def init_listeners(app: FastAPI) -> None:
    @app.exception_handler(CustomException)
    async def custom_exception_handler(request: Request, exc: CustomException):
        return JSONResponse(
            status_code=exc.code,
            content={"error_code": exc.error_code, "message": exc.message},
        )


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
        Middleware(AuthenticationMiddleware, backend=AuthBackend()),
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
    init_listeners(app)

    return app


app = create_app()
app = create_app()
app = create_app()
app = create_app()
app = create_app()
app = create_app()
