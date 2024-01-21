from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def get_bot_commands(bot: Bot):
    commands = [
        BotCommand(command="find", description="Найти сериал"),
        BotCommand(command="my_series", description="Мои сериалы"),
        BotCommand(command="help", description="Помощь"),
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
