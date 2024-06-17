from fastapi import APIRouter, Depends

from app.controllers.auth import AuthController
from app.controllers.user import UserController
from app.models import User
from app.schemas.extras.token import Token
from app.schemas.requests.users import LoginUserRequest, RegisterUserRequest
from app.schemas.responses.users import UserResponse
from core.factory import Factory
from core.fastapi.dependencies.authentication import AuthenticationRequired
from core.fastapi.dependencies.current_user import get_current_user

user_router = APIRouter()


@user_router.get("/", dependencies=[Depends(AuthenticationRequired)])
async def get_users(
    user_controller: UserController = Depends(Factory().get_user_controller),
) -> list[UserResponse]:
    users = await user_controller.get_all()
    return users


@user_router.post("/", status_code=201)
async def register_user(
    register_user_request: RegisterUserRequest,
    auth_controller: AuthController = Depends(Factory().get_auth_controller),
) -> UserResponse:
    return await auth_controller.register(
        email=register_user_request.email,
        password=register_user_request.password,
        username=register_user_request.username,
    )


@user_router.post("/login")
async def login_user(
    login_user_request: LoginUserRequest,
    auth_controller: AuthController = Depends(Factory().get_auth_controller),
) -> Token:
    return await auth_controller.login(
        email=login_user_request.email,
        password=login_user_request.password,
    )


@user_router.get("/me", dependencies=[Depends(AuthenticationRequired)])
def get_user(user: User = Depends(get_current_user)) -> UserResponse:
    return user
