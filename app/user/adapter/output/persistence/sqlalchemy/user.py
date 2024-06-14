from typing import Optional

from sqlalchemy import select

from app.user.domain.entity.user import User, UserRead
from app.user.domain.repository import UserRepo
from core.db.session import session, session_factory


# Repo层的实现
class UserSQLAlchemyRepo(UserRepo):
    async def get_users(
        self, *, limit: int = 12, prev: Optional[int] = None
    ) -> list[User]:
        query = select(User)

        if prev:
            query = query.where(User.id < prev)

        if limit > 12:
            limit = 12

        query = query.limit(limit)

        async with session_factory() as read_session:
            result = await read_session.execute(query)

        return result.scalars().all()

    # * 表示位置参数和关键字参数的分隔
    async def save(self, *, user: User) -> None:
        session.add(user)
