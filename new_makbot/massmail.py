import asyncio
from aiogram import Bot
from new_makbot.config import config
from new_makbot.db import db
from new_makbot.keyboards import client_keyboards
from new_makbot.config import texts
bot = Bot(config.token)


async def mass_mailing():
    for i in db.get_all_users():
        try:
            await bot.send_message(i[0], texts.massmailing_text,
                                   reply_markup=client_keyboards.inline_pay_button(i[0]))
            print('Отправил сообщение пользователю с id', i)
        except Exception as error:
            print(error)
        finally:
            await asyncio.sleep(5)
    print('END!')


event_loop = asyncio.get_event_loop()
tasks = [event_loop.create_task(mass_mailing())]
asyncio.wait(tasks)
event_loop.run_forever()