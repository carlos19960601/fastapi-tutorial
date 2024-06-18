from functools import wraps
from typing import Type

from sqlalchemy import func

from core.cache import CacheTag
from core.cache.base import BaseBackend, BaseKeyMaker


class CacheManager:
    def __init__(self) -> None:
        self.backend = None
        self.key_maker = None

    def init(self, backend: Type[BaseBackend], key_marker: Type[BaseKeyMaker]) -> None:
        self.backend = backend
        self.key_maker = key_marker

    def cached(self, prefix: str = None, tag: CacheTag = None, ttl: int = 60):
        def _cached(function):
            @wraps(function)
            async def __cached(*args, **kwargs):
                if not self.backend or not self.key_maker:
                    raise ValueError("Backend or KeyMaker not initialized")

                key = await self.key_maker.make(
                    function=func, prefix=prefix if prefix else tag.value
                )


Cache = CacheManager()
