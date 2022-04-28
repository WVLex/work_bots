from aiogram import types


def inline_admin_panel():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='Просмотреть', callback_data='view'))
    markup.add(types.InlineKeyboardButton(text='Добавить', callback_data='add'))
    markup.add(types.InlineKeyboardButton(text='Удалить', callback_data='del'))
    return markup


def inline_exit_to_admin_panel():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='На главную', callback_data='exit'))
    return markup


def inline_delete_forecasts(data):
    markup = types.InlineKeyboardMarkup()
    for index, i in enumerate(data):
        markup.add(types.InlineKeyboardButton(text=str(index + 1), callback_data='item_{}'.format(i[0])))
    markup.add(types.InlineKeyboardButton(text='Назад', callback_data='exit'))
    return markup


def inline_view_forecasts(data):
    markup = types.InlineKeyboardMarkup()
    for index, i in enumerate(data):
        markup.add(types.InlineKeyboardButton(text=str(index + 1), callback_data='view_{}'.format(i[0])))
    return markup
