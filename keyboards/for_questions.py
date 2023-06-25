from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_keyboard_button() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="/menu")
    kb.button(text="/help")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
