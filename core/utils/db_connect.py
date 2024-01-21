import asyncpg

from configs import config_logger

logger = config_logger.get_logger("utils.db_connect")


class Request:
    def __init__(self, connector: asyncpg.pool.Pool):
        self.connector = connector

    async def add_data(self, user_id, username, first_name, last_name, date_created):
        query = f"INSERT INTO users (user_id, username, first_name, last_name, date_created, date_updated)" \
                f"VALUES ({user_id}, '{username}', '{first_name}', '{last_name}', {date_created}, NULL) " \
                f"ON CONFLICT (user_id) DO UPDATE SET username = '{username}'," \
                f"first_name = '{first_name}', last_name = '{last_name}', date_updated = {date_created}"
        logger.debug(query)
        await self.connector.execute(query)
