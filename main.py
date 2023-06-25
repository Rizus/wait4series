import asyncio
from configs import config_logger
import logging
from aiogram import Bot, Dispatcher, types
from configs.config_reader import config
from handlers import questions, different_types
# from my_package1 import package1

# Включаем логирование, чтобы не пропустить важные сообщения
logger = config_logger.get_logger(__name__)


async def main():
    # Объект бота
    bot = Bot(token=config.bot_token.get_secret_value(), parse_mode="HTML")
    # Диспетчер
    dp = Dispatcher()
    logger.info("The bot is running")
    logger.root.setLevel(logging.INFO)
    dp.include_routers(questions.router, different_types.router)

    # Альтернативный вариант регистрации роутеров по одному на строку
    # dp.include_router(questions.router)
    # dp.include_router(different_types.router)

    # Запускаем бота и пропускаем все накопленные входящие
    # Да, этот метод можно вызвать даже если у вас поллинг
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

    # package1.process(msg="сообщение")

    logger.info("The bot has been stopped")


if __name__ == "__main__":
    asyncio.run(main())
