import asyncpg

from configs import config_logger
from configs.config_reader import config

logger = config_logger.get_logger("configs.config_db_connection")


async def create_pool():
    while True:
        try:
            logger.info("Creating pool...")
            pool = await asyncpg.create_pool(user=config.DATABASE_USERNAME, password=config.DATABASE_PASSWORD,
                                        database=config.DATABASE_NAME, host=config.DATABASE_IP,
                                        port=config.DATABASE_PORT, command_timeout=config.DATABASE_TIMEOUT
                                        )
            logger.info("Pool created!")
            return pool
        except Exception as ex:
            print(ex)
            logger.warning('Connection refused...', exc_info=True)
