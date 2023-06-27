import asyncio
import logging
from configs import config_logger
from configs.config_db_connection import create_pool
# from configs.config_db_connection import create_pool
from configs.config_reader import config
from aiogram import Bot, Dispatcher
from aiogram import html
from core.handlers import start
from core.middlewares.db_middleware import DbSession
# from core.middlewares.db_middleware import DbSession
from core.utils.commands import get_bot_commands


# Включаем логирование, чтобы не пропустить важные сообщения
logger = config_logger.get_logger(__name__)


async def send_start_bot_message(bot: Bot):
    await bot.send_message(config.ADMIN_ID, text=html.italic("The bot is running!"))


async def send_stop_bot_message(bot: Bot):
    await bot.send_message(config.ADMIN_ID, text=html.italic("The bot has been stopped!"))


async def bot_start():
    pool_connect = await create_pool()
    # Объект бота
    bot = Bot(token=config.BOT_TOKEN.get_secret_value(), parse_mode="HTML")
    # pool_connect = await create_pool()
    # Диспетчер
    dp = Dispatcher()

    logger.info("The bot is running")
    logger.root.setLevel(logging.INFO)

    dp.message.middleware.register(DbSession(pool_connect))
    dp.startup.register(send_start_bot_message)
    dp.shutdown.register(send_stop_bot_message)

    dp.include_router(start.router)

    # Запускаем бота и пропускаем все накопленные входящие
    await bot.delete_webhook(drop_pending_updates=True)
    await get_bot_commands(bot)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
        logger.info("The bot has been stopped")

    # package1.process(msg="сообщение")


if __name__ == "__main__":
    asyncio.run(bot_start())
