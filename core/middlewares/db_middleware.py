from typing import Callable, Awaitable, Dict, Any
import asyncpg
from aiogram import BaseMiddleware
from aiogram.types import Message

from configs import config_logger
from core.utils.db_connect import Request


logger = config_logger.get_logger("config_db_connection")


class DbSession(BaseMiddleware):
    def __init__(self, connector: asyncpg.pool.Pool):
        super().__init__()
        self.connector = connector

    async def __call__(self,
                       handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
                       event: Message,
                       data: Dict[str, Any],
                       ) -> Any:
        async with self.connector.acquire() as connect:
            logger.debug("Acquiring connection...")
            data["request"] = Request(connect)
            return await handler(event, data)
