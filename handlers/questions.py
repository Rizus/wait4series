from aiogram import Router
from aiogram.filters import Command
from aiogram.filters.text import Text
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram import html

from keyboards.for_questions import get_keyboard_button

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    user = message.from_user
    await message.answer(f"Привет, {html.bold(user.first_name)}!",
                         reply_markup=get_keyboard_button(), parse_mode="HTML"
                         )


@router.message(Text(text="/menu", ignore_case=True))
async def answer_yes(message: Message):
    await message.answer("menu...",
                         reply_markup=ReplyKeyboardRemove()
                         )


@router.message(Text(text="/help", ignore_case=True))
async def answer_no(message: Message):
    await message.answer("help...",
                         reply_markup=ReplyKeyboardRemove()
                         )
