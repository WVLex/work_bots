import asyncio

from meditation.db import db
from meditation.config.config import meditation_token as meditation_bot_token
from aiogram import Bot


async def send_messages(data):
    if data[1] == 'meditation_bot':
        bot = Bot(meditation_bot_token)
        users = [i[0] for i in db.get_all_data('meditation_users')]
        for i in users:
            try:
                await bot.send_message(i, data[2])
            except Exception as e:
                print(e)


async def check_updates():
    while True:
        data = db.get_all_data('massmailing')
        for i in data:
            await send_messages(i)
            db.delete_from_massmailing(i[0])
        await asyncio.sleep(60)
