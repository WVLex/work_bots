from aiogram import types


def inline_pay_buton(tg_id):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='490 руб', url='https://snebaupal.ru/makbot/purchase/{}'.format(tg_id)))
    return markup
