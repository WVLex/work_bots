import datetime
# astro_bot
from astro_bot.db import db
from astro_bot.config.config import token as astro_bot_token
from astro_bot.config import texts
from create_scheduler import scheduler_astrobot
from aiogram import Bot
from aiogram import types
from aiogram.utils.markdown import bold
import asyncio


async def send_messages(forecast_id):
    bot = Bot(astro_bot_token)
    subscribers, not_subscribers = db.get_all_subscribers()
    forecast = db.get_forecast(forecast_id)
    date = forecast[1].find('\n')
    for tg_id in subscribers:
        try:
            await bot.send_message(tg_id, bold(forecast[1][:date]) + forecast[1][date:],
                                   parse_mode=types.ParseMode.MARKDOWN)
            await asyncio.sleep(5)
        except Exception as e:
            print(e)
    for tg_id in not_subscribers:
        try:
            await bot.send_message(tg_id, texts.eighteen_one)
            await bot.send_message(tg_id, texts.eighteen_two)
            await bot.send_message(tg_id, texts.eighteen_three)
            db.update_subscribe(tg_id, True)
            await asyncio.sleep(5)
        except Exception as e:
            print(e)
    db.delete_from_forecasts(forecast_id)


async def update_astro_bot():
    while True:
        data = set(db.get_all_data())
        jobs_data = scheduler_astrobot.get_jobs()
        jobs_data = {i.id for i in jobs_data}
        to_delete = jobs_data - data
        to_add = data - jobs_data
        for i in to_delete:
            scheduler_astrobot.remove_job(i)
        for i in data:
            if i[0] in {i[0] for i in to_add} and i[2] > datetime.datetime.now():
                scheduler_astrobot.add_job(send_messages,
                                  "date",
                                  id=str(i[0]),
                                  run_date=i[2],
                                  args=(str(i[0]), ),
                                  timezone='Europe/Moscow')
        await asyncio.sleep(60)
