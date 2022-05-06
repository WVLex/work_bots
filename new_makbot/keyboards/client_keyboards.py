from aiogram import types


def inline_start():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='Вытянуть карту', callback_data='card'))
    return markup
