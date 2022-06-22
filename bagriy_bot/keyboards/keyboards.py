from aiogram import types


def pay_button(label):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='700руб', url='https://angelb.ru/bagriy_bot/{}'.format(label)))
    return markup