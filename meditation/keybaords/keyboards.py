from aiogram import types
from meditation.config import config


def inline_start_keyboard(relax_url, anxiety_url, full_url, do_url):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='Расслабиться - 3500руб', url=relax_url))
    markup.add(types.InlineKeyboardButton(text='Снять тревогу - 3500руб', url=anxiety_url))
    markup.add(types.InlineKeyboardButton(text='Наполниться - 3500руб', url=full_url))
    markup.add(types.InlineKeyboardButton(text='Действовать - 3500руб', url=do_url))
    return markup

def inline_thank_you_keyboard():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='Сказать спасибо - 500руб', url=config.base_pay_url.format('500')))
    markup.add(types.InlineKeyboardButton(text='Сказать спасибо - 1000руб', url=config.base_pay_url.format('1000')))
    markup.add(types.InlineKeyboardButton(text='Сказать спасибо - 1500руб', url=config.base_pay_url.format('1500')))
    markup.add(types.InlineKeyboardButton(text='Сказать спасибо - 2000руб', url=config.base_pay_url.format('2000')))
    return markup


def inline_massmail_keyboard(twelve_url, six_url):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='12 медитаций - 12000руб', url=twelve_url))
    markup.add(types.InlineKeyboardButton(text='6 медитаций - 7000руб', url=six_url))
    markup.add(types.InlineKeyboardButton(text='3 медитации - 3500руб', callback_data='next'))
    return markup
