import asyncpg


class Request:
    def __init__(self, connector: asyncpg.pool.Pool):
        self.connector = connector

    async def add_data(self, user_id, username, first_name, last_name):
        query = f"INSERT INTO users (user_id, username, first_name, last_name) VALUES ({user_id}, '{username}'," \
                f"'{first_name}', '{last_name}') ON CONFLICT (user_id) DO UPDATE SET username = '{username}'," \
                f"first_name = '{first_name}',last_name = '{last_name}'"
        await self.connector.execute(query)
