import datetime
import apscheduler
import random
from create_scheduler import scheduler_bagriybot
from bagriy_bot.create_bot import bot
from bagriy_bot.db import db
from bagriy_bot.config import texts as bot_texts
from bagriy_bot.keyboards import keyboards


async def send_message():
    send_text, send_pay = db.get_group_of_users()
    texts = db.get_texts()
    for i in send_text:
        try:
            await bot.send_message(i[0], texts[random.randint(1, 28)])
        except Exception as e:
            print(e)
    for i in send_pay:
        try:
            await bot.send_message(i[0], texts[random.randint(1, 28)])
            await bot.send_message(i[0], bot_texts.pay_text,
                                   reply_markup=keyboards.pay_button(str(i[0])))
        except Exception as e:
            print(e)
        db.update_value(i[0], 'pay', False)


async def bagriy_bot():
    scheduler_bagriybot.add_job(send_message, "cron", hour='6')


