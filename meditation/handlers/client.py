from meditation.create_bot import bot
from meditation.db import db
from meditation.keybaords import keyboards
from meditation.config import config
from aiogram import types, Dispatcher


# @dp.message_handler(commands=['start'])
async def start_text(message: types.Message):
    user = db.check_user(message.from_user.id)
    if not user:
        db.append_user(message.from_user.id)
    if not db.check_user(message.from_user.id)['relax_url']:
        db.get_pay_urls(message.from_user.id)
        # asyncio.create_task(db.urls_timer(message.from_user.id))
    user = db.check_user(message.from_user.id)
    await bot.send_message(message.from_user.id, config.start_text,
                           reply_markup=keyboards.inline_massmail_keyboard(user['twelve_meditation_url'],
                                                                           user['six_meditation_url'])
                           )


async def old_meditations(call: types.CallbackQuery):
    user = db.check_user(call.from_user.id)
    await bot.send_message(call.from_user.id, 'Забрать свои медитации',
                           reply_markup=keyboards.inline_start_keyboard(user['relax_url'],
                                                                        user['anxiety_url'],
                                                                        user['full_url'],
                                                                        user['doit_url'],
                                                                        ))



def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_text, commands='start')
    dp.register_callback_query_handler(old_meditations, text='next')