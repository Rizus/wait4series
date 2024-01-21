from aiogram import Router
from aiogram.filters import Command
from aiogram.filters.text import Text
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram import html

from configs import config_logger
from core.utils.db_connect import Request
from core.keyboards.for_start import get_keyboard_button


router = Router()
logger = config_logger.get_logger("handlers.start")


@router.message(Command("start"))
async def cmd_start(message: Message, request: Request):
    user = message.from_user
    logger.info(f"User [{user.id}: {user.full_name}] - send command \"/start\"")
    await request.add_data(message.from_user.id, message.from_user.username,
                           message.from_user.first_name, message.from_user.last_name, "NOW()::timestamp"
                           )
    await message.answer(f"Привет, {html.bold(user.first_name)}!",
                         reply_markup=get_keyboard_button(), parse_mode="HTML"
                         )


@router.message(Text(text="/find", ignore_case=True))
async def cmd_menu(message: Message):
    user = message.from_user
    logger.info(f"User [{user.id}: {user.full_name}] - send command \"/find\"")
    await message.answer("find...",
                         reply_markup=ReplyKeyboardRemove()
                         )


@router.message(Text(text="/my_series", ignore_case=True))
async def cmd_help(message: Message):
    user = message.from_user
    logger.info(f"User [{user.id}: {user.full_name}] - send command \"/my_series\"")
    await message.answer("my series...",
                         reply_markup=ReplyKeyboardRemove()
                         )

    @router.message(Text(text="/help", ignore_case=True))
    async def cmd_help(message: Message):
        user = message.from_user
        logger.info(f"User [{user.id}: {user.full_name}] - send command \"/help\"")
        await message.answer("help...",
                             reply_markup=ReplyKeyboardRemove()
                             )
