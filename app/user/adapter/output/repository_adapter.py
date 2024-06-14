from typing import Optional

from app.user.domain.entity.user import User, UserRead
from app.user.domain.repository import UserRepo


class UserRepositoryAdapter:
    def __init__(self, user_repo: UserRepo):
        self.user_repo = user_repo

    async def get_users(
        self, limit: int = 12, prev: Optional[int] = None
    ) -> list[UserRead]:
        users = await self.user_repo.get_users(limit=limit, prev=prev)
        return [UserRead.model_validate(user) for user in users]

    async def get_user_by_email_or_nickname(
        self, *, email: str, nickname: str
    ) -> Optional[User]:
        return await self.user_repo.get_user_by_email_or_nickname(
            email=email, nickname=nickname
        )
