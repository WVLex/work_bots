import asyncio
import datetime

import aiogram.utils.json
from aiogram import types, Dispatcher

from statisctic_bot.create_bot import bot
from statisctic_bot.config.texts import msg_text
from statisctic_bot.db.db import Users


async def command_start(message: types.Message):
    temporary_message = await bot.send_message(message.from_user.id, 'Прошу подождать...')
    await bot.send_chat_action(message.from_user.id, 'typing')
    users = Users()
    text = msg_text(users.sneba_users, users.astro_users, users.yasna_users, users.audio_users, users.bagriy_users,
                    users.new_makbot_users, users.meditation_users)
    await bot.delete_message(message.from_user.id, temporary_message.message_id)
    await bot.send_message(message.from_user.id, text, parse_mode=types.ParseMode.MARKDOWN)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands='start')


