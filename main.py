from config import TOKEN_API
import asyncio
from log import my_logger
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command


# Включаем логирование, чтобы не пропустить важные сообщения
logger = my_logger.get_logger(__name__)


# Объект бота
bot = Bot(TOKEN_API)
# Диспетчер
dp = Dispatcher()


# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")


# Запуск процесса поллинга новых апдейтов
async def main():
    logger.info("The bot is running")
    logger.root.setLevel(logging.INFO)
    # package1.process(msg="сообщение")
    await dp.start_polling(bot)
    logger.info("The bot has been stopped")


if __name__ == "__main__":
    asyncio.run(main())
