from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from lexicon.lexicon import LEXICON


def create_pagination_keyboard(*buttons: str) -> InlineKeyboardMarkup:
    pagination_kb: InlineKeyboardMarkup = InlineKeyboardMarkup()
    pagination_kb.row(*[InlineKeyboardButton(
        LEXICON[bttn] if bttn in LEXICON else bttn,
        callback_data=bttn) for bttn in buttons])
    return pagination_kb