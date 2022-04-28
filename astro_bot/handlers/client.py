from aiogram import types, Dispatcher
from astro_bot.create_bot import bot, dp
from astro_bot.db import db
from astro_bot.config import config
from astro_bot.keyboards import client_keyboards


# @dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    user = db.check_user(message.from_user.id)
    if not user:
        db.append_user(message.from_user.id)
    db.update_subscribe(message.from_user.id, True)
    await bot.send_message(message.from_user.id, config.start_text)
    await bot.send_message(message.from_user.id, config.eighteen_one)
    await bot.send_message(message.from_user.id, config.eighteen_two)
    await bot.send_message(message.from_user.id, config.eighteen_three)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands='start')
