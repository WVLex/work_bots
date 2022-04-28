from aiogram import types
import telegram
import config


def inline_main_keyboard():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='Взять карту', callback_data='send_card'))
    return markup


def inline_main_keyboard_for_updater():
    keyboard = [[telegram.InlineKeyboardButton(text='Взять карту', callback_data='send_card')]]
    markup = telegram.InlineKeyboardMarkup(keyboard)
    return markup


def inline_request_feedback_keyboard():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='Да', callback_data='feedback_yes'))
    markup.add(types.InlineKeyboardButton(text='Нет', callback_data='feedback_no'))
    return markup


def inline_request_subscribe_keyboard():
    btn1 = types.InlineKeyboardButton(text='Да', callback_data='subscribe_yes')
    btn2 = types.InlineKeyboardButton(text='Нет', callback_data='subscribe_no')
    markup = types.InlineKeyboardMarkup().add(btn1, btn2)
    return markup


def inline_request_subscribe_keyboard_for_updater():
    keyboard = [[telegram.InlineKeyboardButton(text='Да', callback_data='subscribe_yes'),
                 telegram.InlineKeyboardButton(text='Нет', callback_data='subscribe_no')]]
    markup = telegram.InlineKeyboardMarkup(keyboard)
    return markup


def inline_check_spelling_of_text():
    btn1 = types.InlineKeyboardButton(text='Да, отправляй', callback_data="spelling_check_ok")
    btn2 = types.InlineKeyboardButton(text='Нет', callback_data="spelling_check_bad")
    markup = types.InlineKeyboardMarkup().add(btn1, btn2)
    return markup


def inline_pay_button(url):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='Оплатить', url=url))
    return markup


def inline_thank_you_keyboard():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='Сказать спасибо - 500руб', url=config.base_pay_url.format('500')))
    markup.add(types.InlineKeyboardButton(text='Сказать спасибо - 1000руб', url=config.base_pay_url.format('1000')))
    markup.add(types.InlineKeyboardButton(text='Сказать спасибо - 1500руб', url=config.base_pay_url.format('1500')))
    markup.add(types.InlineKeyboardButton(text='Сказать спасибо - 2000руб', url=config.base_pay_url.format('2000')))
    return markup
