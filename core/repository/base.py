from typing import Any, Generic, Optional, Type, TypeVar

from sqlalchemy import Select, select
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import Base

ModelType = TypeVar("ModelType", bound=Base)


class BaseRepository(Generic[ModelType]):
    def __init__(self, model: Type[ModelType], db_session: AsyncSession) -> None:
        self.session = db_session
        self.model_class = model

    async def create(self, attributes: dict[str, Any] = None) -> ModelType:
        if attributes is None:
            attributes = {}
        model = self.model_class(**attributes)
        self.session.add(model)
        return model

    async def get_all(self, skip: int = 0, limit: int = 100) -> list[ModelType]:
        query = self._query()
        query = query.offset(skip).limit(limit)

        return await self._all(query)

    async def get_by(self, field: str, value: Any) -> ModelType:
        query = self._query()
        query = await self._get_by(query, field, value)

        return await self._all(query)

    def _query(self) -> Select:
        query = select(self.model_class)

        return query

    async def _all(self, query: Select) -> list[ModelType]:
        result = await self.session.scalars(query)
        return result.all()

    async def _get_by(self, query: Select, field: str, value: Any) -> Select:
        return query.where(getattr(self.model_class, field) == value)

    async def _one_or_none(self, query: Select) -> Optional[ModelType]:
        result = await self.session.scalars(query)
        return result.one_or_none()
