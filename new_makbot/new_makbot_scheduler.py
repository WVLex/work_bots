import datetime
import apscheduler
import random
from create_scheduler import scheduler_new_makbot
from new_makbot.create_bot import bot
from new_makbot.db import db
from new_makbot.config import texts


async def send_message():
    data = db.get_all_users()
    for i in [i for i in data if i[4] is True]:
        if datetime.datetime.now() - i[3] <= datetime.timedelta(days=13):
            await bot.send_message(i[0], texts.today_card)
            await bot.send_photo(i[0], db.randomizer_for_cards())


async def new_mak_bot():
    scheduler_new_makbot.add_job(send_message, "cron", hour='6', minute='30', timezone='Europe/Moscow')


