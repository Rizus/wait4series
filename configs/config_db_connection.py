import asyncpg

from configs.config_reader import config


async def create_pool():
    return await asyncpg.create_pool(user=config.DATABASE_USERNAME, password=config.DATABASE_PASSWORD,
                                     database=config.DATABASE_NAME, host=config.DATABASE_IP,
                                     port=config.DATABASE_PORT, command_timeout=config.DATABASE_TIMEOUT
                                     )
