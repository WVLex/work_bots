import asyncio
import datetime

import aiogram.utils.json
from aiogram import types, Dispatcher

import new_makbot.keyboards.client_keyboards
from new_makbot.create_bot import bot, dp
from new_makbot.db import db
from new_makbot.config import config, texts
from new_makbot.keyboards import client_keyboards


async def command_start(message: types.Message):
    user = db.check_user(message.from_user.id)
    if not user:
        db.append_user(message.from_user.id)
    await send_card_func(message)


async def send_card(call: types.CallbackQuery):
    await send_card_func(call)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands='start')
    dp.register_callback_query_handler(send_card, text='card')


async def send_message_and_update_data(call, counter):
    await bot.send_photo(call.from_user.id, db.randomizer_for_cards())
    await bot.send_message(call.from_user.id, texts.visit_consultation[counter],
                           reply_markup=client_keyboards.inline_start())
    db.update_counter(call.from_user.id)
    db.update_date(call.from_user.id)


async def send_card_func(call):
    counter = db.get_user_counter(call.from_user.id)
    if counter < 3 and datetime.datetime.now() - db.check_user(call.from_user.id)['date'] > datetime.timedelta(days=1):
        db.zeroing_counter(call.from_user.id)
        await send_message_and_update_data(call, 0)
    elif counter < 3:
        await send_message_and_update_data(call, counter)
    else:
        if datetime.datetime.now() - db.check_user(call.from_user.id)['date'] < datetime.timedelta(days=1):
            await bot.send_message(call.from_user.id, texts.end)
        else:
            db.zeroing_counter(call.from_user.id)
            await send_message_and_update_data(call, 0)
