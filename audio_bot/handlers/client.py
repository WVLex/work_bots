import datetime

from aiogram import types, Dispatcher

from audio_bot.create_bot import bot
from audio_bot.db import db
from audio_bot.config import texts
from audio_bot.keyboards import client_keyboards


async def start(message: types.Message):
    if not db.check_user(message.from_user.id):
        db.append_user(message.from_user.id)
        await bot.send_audio(message.from_user.id,
                             audio='CQACAgIAAxkBAAPIYmvCLYrxhmmt3Fd85hgooaXmUhUAAkMfAAI9DmBL0lCk2i-zq3QkBA',
                             protect_content=True,
                             title='Часть 1')
        db.update_value(message.from_user.id, 'pay', True)
        db.update_value(message.from_user.id, 'date_start', datetime.datetime.now())


async def pay_message(call: types.CallbackQuery):
    await bot.send_message(call.from_user.id, texts.pay_message,
                           reply_markup=client_keyboards.pay_button(str(call.from_user.id)))


async def send_audio(call: types.CallbackQuery):
    user = db.check_user(call.from_user.id)
    if user['counter'] <= 7:
        await bot.send_audio(call.from_user.id, audio=db.get_audio_id(user['counter']),
                             reply_markup=client_keyboards.get_audio(),
                             protect_content=True,
                             title='Часть {}'.format(user['counter']),
                             performer='Ясна Токарик'
                             )
        db.update_value(call.from_user.id, 'counter', int(user['counter']) + 1)
    else:
        await bot.send_audio(call.from_user.id, audio=db.get_audio_id(user['counter']),
                             protect_content=True,
                             title='Часть {}'.format(user['counter']),
                             performer='Ясна Токарик'
                             )


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start, commands='start')
    dp.register_callback_query_handler(pay_message, text='next')
    dp.register_callback_query_handler(send_audio, text='audio')
