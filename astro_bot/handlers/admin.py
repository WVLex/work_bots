import datetime
import re
from aiogram import types, Dispatcher
from aiogram.dispatcher import filters
from aiogram.utils.markdown import bold
from astro_bot.create_bot import bot
from astro_bot.db import db
from astro_bot.config import config
from astro_bot.keyboards import admin_keyboards


# @dp.message_handler(commands=['/admin'])
async def admin_panel(message: types.Message):
    user = db.check_admin(message.from_user.id)
    if not user:
        db.append_admin(message.from_user.id)
    db.update_state(message.from_user.id, None)
    await bot.send_message(message.from_user.id, config.admin_text,
                           reply_markup=admin_keyboards.inline_admin_panel())


""" add functional"""


# @dp.callback_query_handler(text='add', state=None)
async def send_forecast(call: types.CallbackQuery):
    db.update_state(call.from_user.id, 0)
    await bot.send_message(call.from_user.id, config.send_forecast,
                           reply_markup=admin_keyboards.inline_exit_to_admin_panel())


# @dp.message_handler(state=FSMAdmin.forecast)
async def send_date(message: types.Message):
    db.update_forecast(message.from_user.id, message.text)
    db.update_state(message.from_user.id, 1)
    await bot.send_message(message.from_user.id, config.send_date,
                           reply_markup=admin_keyboards.inline_exit_to_admin_panel())


# dp.message_handler(state=FSMAdmin.date)
async def save_to_database(message: types.Message):
    if not re.fullmatch('^\d\d.\d\d.\d\d\d\d \d\d:\d\d$', message.text):
        await bot.send_message(message.from_user.id, config.date_format_error)
        return
    if datetime.datetime.now() > (db.parse_date(message.text) + datetime.timedelta(minutes=2)):
        await bot.send_message(message.from_user.id, config.date_time_error)
        return

    db.append_forecast(db.check_admin(message.from_user.id)['forecast'], message.text)
    db.update_state(message.from_user.id, None)
    await bot.send_message(message.from_user.id, config.success_append_forecast,
                           reply_markup=admin_keyboards.inline_admin_panel())


# @dp.callback_query_handler(text='exit', state='*')
async def exit_from_state(call: types.CallbackQuery):
    db.update_state(call.from_user.id, None)
    await bot.send_message(call.from_user.id, config.admin_text,
                           reply_markup=admin_keyboards.inline_admin_panel())


""" view functional"""


async def view_forecasts(call: types.CallbackQuery):
    data = db.get_all_forecasts()
    if data:
        str_data = [(a, c.strftime('%d.%m.%Y %H:%M')) for a, b, c in data]
        text = ''
        for index, i in enumerate(str_data):
            text += '\n————{}————\n'.format(index + 1) + 'Будет отправлено в ' + i[1]
        await bot.send_message(call.from_user.id, text,
                               reply_markup=admin_keyboards.inline_view_forecasts(data))
    else:
        await bot.send_message(call.from_user.id, config.empty_forecasts)


async def view_current_forecast(call: types.CallbackQuery):
    item = call.data.split('_')[1]
    forecast = db.get_forecast(item)
    date = forecast[1].find('\n')
    await bot.send_message(call.from_user.id, bold(forecast[1][:date]) + forecast[1][date:],
                           parse_mode=types.ParseMode.MARKDOWN,
                           reply_markup=admin_keyboards.inline_exit_to_admin_panel())


""" delete functional"""


async def delete_forecasts(call: types.CallbackQuery):
    data = db.get_all_forecasts()
    if data:
        str_data = [(a, c.strftime('%d.%m.%Y %H:%M')) for a, b, c in data]
        text = ''
        for index, i in enumerate(str_data):
            text += '\n————{}————\n'.format(index + 1) + 'Будет отправлено: ' + i[1]
        await bot.send_message(call.from_user.id, text + '\n\n Выберите прогноз, который необходимо удалить',
                               reply_markup=admin_keyboards.inline_delete_forecasts(data))
    else:
        await bot.send_message(call.from_user.id, config.empty_forecasts)


async def delete_from_callback(call: types.CallbackQuery):
    item = call.data.split('_')[1]
    db.delete_from_forecasts(item)
    await bot.send_message(call.from_user.id, config.success_del,
                           reply_markup=admin_keyboards.inline_admin_panel())


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(admin_panel, lambda message: message.from_user.id in config.admins,
                                commands='admin')

    # add
    dp.register_callback_query_handler(send_forecast, text='add')
    dp.register_callback_query_handler(exit_from_state, text='exit')
    dp.register_message_handler(send_date, lambda message: db.check_admin(message.from_user.id)["state"] == 0)
    dp.register_message_handler(save_to_database, lambda message: db.check_admin(message.from_user.id)["state"] == 1)

    # view
    dp.register_callback_query_handler(view_forecasts, text='view')
    dp.register_callback_query_handler(view_current_forecast, filters.Regexp("^view_[+]?\d+$"))

    # delete
    dp.register_callback_query_handler(delete_forecasts, text='del')
    dp.register_callback_query_handler(delete_from_callback, filters.Regexp("^item_[+]?\d+$"))
