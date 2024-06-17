from typing import Optional

from app.models import User
from core.repository import BaseRepository


class UserRepository(BaseRepository[User]):
    async def get_by_username(self, username: str) -> Optional[User]:
        query = self._query()
        query = query.where(User.username == username)

        return await self._one_or_none(query)

    async def get_by_email(self, email: str) -> Optional[User]:
        query = self._query()
        query = query.where(User.email == email)

        return await self._one_or_none(query)
