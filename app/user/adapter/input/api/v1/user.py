from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Query

from app.container import Container
from app.user.adapter.input.api.v1.request import CreateUserRequest
from app.user.application.dto import CreateUserResponseDTO, GetUserListResponseDTO
from app.user.domain.command import CreateUserCommand
from app.user.domain.usecase.user import UserUseCase

user_router = APIRouter()


@user_router.get(
    "",
    response_model=list[GetUserListResponseDTO],
)
@inject
async def get_user_list(
    limit: int = Query(10, description="limit"),
    prev: int = Query(None, description="Prev ID"),
    usecase: UserUseCase = Depends(Provide[Container.user_service]),
):
    return await usecase.get_user_list(limit=limit, prev=prev)


@user_router.post(
    "",
    response_model=CreateUserResponseDTO,
)
async def create_user(
    request: CreateUserRequest,
    usecase: UserUseCase = Depends(Provide[Container.user_service]),
):
    command = CreateUserCommand(**request.model_dump())
    await usecase.create_user(command=command)
    return {"email": request.email, "nickname": request.nickname}
