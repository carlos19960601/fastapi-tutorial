from functools import wraps
from typing import Any

from core.db import session


class Transactional:
    def __call__(self, func) -> Any:
        @wraps(func)
        async def _transactional(*args, **kwargs):
            try:
                result = await func(*args, **kwargs)
                await session.commit()
            except Exception as e:
                await session.rollback()
                raise e
            return

        return _transactional
