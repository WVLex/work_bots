from aiogram import types
from audio_bot.config import config


def pay_button(tg_id):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='Оплатить', url='https://snebaupal.ru/audio_bot/book' + tg_id))
    return markup


def first_button():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='Да! Дальше🌟', callback_data='next'))
    return markup

def get_audio():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='Ещё часть', callback_data='audio'))
    return markup