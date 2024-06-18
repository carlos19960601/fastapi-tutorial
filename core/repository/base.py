from typing import Any, Generic, Optional, Type, TypeVar

from sqlalchemy import Select, func, select
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

    async def delete(self, model: ModelType) -> None:
        self.session.delete(model)

    async def get_all(self, skip: int = 0, limit: int = 100) -> list[ModelType]:
        query = self._query()
        query = query.offset(skip).limit(limit)

        return await self._all(query)

    async def get_by(
        self, field: str, value: Any, unique: bool = False
    ) -> Optional[ModelType]:
        query = self._query()
        query = await self._get_by(query, field, value)

        if unique:
            return await self._one(query)

        return await self._all(query)

    def _query(self, order_: Optional[dict] = None) -> Select:
        query = select(self.model_class)
        query = self._maybe_ordered(query, order_)

        return query

    async def _get_by(self, query: Select, field: str, value: Any) -> Select:
        return query.where(getattr(self.model_class, field) == value)

    def _maybe_ordered(self, query: Select, order_: Optional[dict]) -> Select:
        if order_:
            if order_["asc"]:
                for order in order_["asc"]:
                    query = query.order_by(getattr(self.model_class, order).asc())
            else:
                for order in order_["desc"]:
                    query = query.order_by(getattr(self.model_class, order).desc())

        return query

    async def _count(self, query: Select) -> int:
        query = query.subquery()
        query = await self.session.scalars(select(func.count()).select_from(query))
        return query.one()

    async def _one(self, query: Select) -> ModelType:
        query = await self.session.scalars(query)
        return query.one()

    async def _all(self, query: Select) -> list[ModelType]:
        result = await self.session.scalars(query)
        return result.all()

    async def _one_or_none(self, query: Select) -> Optional[ModelType]:
        result = await self.session.scalars(query)
        return result.one_or_none()
