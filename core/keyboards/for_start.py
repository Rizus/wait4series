from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_keyboard_button() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="/find")
    kb.button(text="/my_series")
    kb.button(text="/help")
    kb.adjust(3)
    return kb.as_markup(resize_keyboard=True)
