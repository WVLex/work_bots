import asyncio
import datetime

import aiogram.utils.json
from aiogram import types, Dispatcher

import new_makbot.keyboards.client_keyboards
from new_makbot.create_bot import bot, dp
from new_makbot.db import db
from new_makbot.config import config
from new_makbot.keyboards import client_keyboards


async def command_start(message: types.Message):
    user = db.check_user(message.from_user.id)
    if not user:
        db.append_user(message.from_user.id)
    await bot.send_message(message.from_user.id, config.start_text,
                           reply_markup=client_keyboards.inline_start())


async def send_card(call: types.CallbackQuery):
    if db.get_user_counter(call.from_user.id) < 3:
        await body(call)
    else:
        if db.check_user(call.from_user.id)['date'] - datetime.datetime.now() < datetime.timedelta(days=1):
            await bot.send_message(call.from_user.id, config.more_than_three_cards)
        else:
            db.zeroing_counter(call.from_user.id)
            await body(call)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands='start')
    dp.register_callback_query_handler(send_card, text='card')


async def body(call):
    # await bot.send_photo(call.from_user.id, db.randomizer_for_cards())
    await bot.send_message(call.from_user.id, config.visit_consultation,
                           reply_markup=client_keyboards.inline_start())
    db.update_counter(call.from_user.id)
    db.update_date(call.from_user.id)