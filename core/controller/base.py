from typing import Generic, Type, TypeVar

from core.database.session import Base
from core.exceptions import NotFoundException
from core.repository import BaseRepository

ModelType = TypeVar("ModelType", bound=Base)


class BaseController(Generic[ModelType]):
    def __init__(self, model: Type[ModelType], repository: BaseRepository) -> None:
        self.model_class = model
        self.repository = repository

    async def get_all(self, skip: int = 0, limit: int = 100) -> list[ModelType]:
        return await self.repository.get_all(skip, limit)

    async def get_by_id(self, id_: int) -> ModelType:
        db_obj = await self.repository.get_by(field="id", value=id_)

        if not db_obj:
            raise NotFoundException(
                f"{self.model_class.__tablename__.title()} with id: {id_} does not exist"
            )

        return db_obj
