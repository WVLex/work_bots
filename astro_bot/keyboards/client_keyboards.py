from aiogram import types


def inline_start():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='Да', callback_data='yes'))
    markup.add(types.InlineKeyboardButton(text='Нет', callback_data='no'))
    return markup
