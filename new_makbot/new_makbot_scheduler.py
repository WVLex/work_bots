import datetime
import apscheduler
import random
from create_scheduler import scheduler_new_makbot
from new_makbot.create_bot import bot
from new_makbot.db import db
from new_makbot.config import texts
from new_makbot.keyboards import client_keyboards


async def send_message():
    data = db.get_all_users()
    for i in [i for i in data if i[4] is True]:
        if datetime.datetime.now() - i[3] <= datetime.timedelta(days=13):
            await bot.send_message(i[0], texts.today_card)
            await bot.send_photo(i[0], db.randomizer_for_cards())

    for i in data:
        try:
            if datetime.datetime.now() - i[5] > datetime.timedelta(days=7):
                await bot.send_message(i[0], texts.massmailing_text,
                                       reply_markup=client_keyboards.inline_pay_button(i[0]))
                db.update_value(i[0], 'start_date', None)
        except Exception as e:
            print(e)


async def new_mak_bot():
    scheduler_new_makbot.add_job(send_message, "cron", hour='6', minute='30', timezone='Europe/Moscow')
