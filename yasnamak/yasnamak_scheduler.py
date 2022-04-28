import asyncio
import datetime

from yasnamak.create_bot import bot
from yasnamak.db import db
from yasnamak.keyboards import keyboards
from yasnamak.config import config
from create_scheduler import scheduler_yasnamak


# Рассылка в рандомный день
async def send_message():
    today = db.get_today_subscribers_list()
    newsletter = db.get_current_everyday_newsletter_time()
    for tg_id in newsletter:
        data = db.randomizer_for_cards_and_poems()
        try:
            await bot.send_message(tg_id, config.first_msg_subscribe)
            await bot.send_photo(tg_id, db.get_photo(data['card_number']))
            await bot.send_message(tg_id, data['poem'])
            await bot.send_message(tg_id, config.end_msg_subscribe)
            if tg_id in today:
                right_msg = await bot.send_message(tg_id, config.weekly_subscribe,
                                                   reply_markup=keyboards.inline_request_subscribe_keyboard())
                db.update_message_id_to_edit(tg_id, right_msg.message_id)
        except Exception as e:
            print(e)
        finally:
            db.update_everyday_newsletter_time(tg_id)
    del newsletter


async def yasnamak_updater():
    scheduler_yasnamak.add_job(send_message, 'cron',
                               hour='0,3,6,9,12,15,18,21')