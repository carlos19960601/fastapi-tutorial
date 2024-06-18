import inspect
from typing import Callable

from core.cache.base import BaseKeyMaker


class CustomKeyMaker(BaseKeyMaker):
    async def make(self, function: Callable, prefix: str) -> str:
        path = f"{prefix}::{inspect.getmodule(function).__name__}.{function.__name__}"
        args = ""
