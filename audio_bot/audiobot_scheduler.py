import asyncio
import datetime

from audio_bot.create_bot import bot
from audio_bot.config import texts
from audio_bot.db import db
from audio_bot.keyboards import client_keyboards
from create_scheduler import scheduler_audiobot


async def send_messages(tg_id):
    await bot.send_message(tg_id, texts.first_message,
                           reply_markup=client_keyboards.first_button())


async def update_audio_bot():
    while True:
        data = db.get_users_with_pay_vlaue()
        if data:
            for i in data:
                scheduler_audiobot.add_job(send_messages,
                                  "date",
                                  run_date=datetime.datetime.now() + datetime.timedelta(minutes=9),
                                  args=(i[0],),
                                  timezone='Europe/Moscow')
                db.update_value(i[0], 'pay', False)
        await asyncio.sleep(60)
