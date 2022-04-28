from aiogram import Dispatcher, types
from bagriy_bot.db import db
from bagriy_bot.create_bot import bot
from bagriy_bot.config import texts


async def start(message: types.Message):
    user = db.check_user(message.from_user.id)
    if not user:
        db.append_user(message.from_user.id)
    await bot.send_message(message.from_user.id, texts.start_text)




def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start, commands='start')
