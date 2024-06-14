import select
from typing import Optional

from app.user.adapter.output.repository_adapter import UserRepositoryAdapter
from app.user.application.exception import (
    DuplicateEmailOrNicknameException,
    PasswordDoesNotMatchException,
)
from app.user.domain.command import CreateUserCommand
from app.user.domain.entity.user import User, UserRead
from app.user.domain.usecase.user import UserUseCase
from core.db import Transactional


class UserService(UserUseCase):
    def __init__(self, repository: UserRepositoryAdapter):
        self.repository = repository

    async def get_user_list(
        self, limit: int = 12, prev: Optional[int] = None
    ) -> list[UserRead]:
        return await self.repository.get_users(limit, prev)

    @Transactional()
    async def create_user(self, command: CreateUserCommand) -> None:
        if command.password1 != command.password2:
            raise PasswordDoesNotMatchException

        is_exist = await self.repository.get_user_by_email_or_nickname(
            email=command.email, nickname=command.nickname
        )

        if is_exist:
            raise DuplicateEmailOrNicknameException

        user = User.create(
            email=command.email, password=command.password1, nickname=command.nickname
        )

        await self.repository.save(user=user)
