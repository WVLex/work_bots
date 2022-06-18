from aiogram import types


def inline_start():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='Вытянуть карту', callback_data='card'))
    return markup


def inline_pay_button(tg_id):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='490 руб', url='https://snebaupal.ru/makbot/purchase/{}'.format(tg_id)))
    return markup