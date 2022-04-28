from meditation.create_bot import bot
from meditation.db import db
from meditation.keybaords import keyboards
from meditation.config import config
from aiogram import types, Dispatcher
import asyncio


# @dp.message_handler(lambda message: message.from_user.id in config.admins,
#                     commands=['massmail'])
async def mass_mailing(message: types.Message):
    if message.text == '/massmail':
        await bot.send_chat_action(message.from_user.id, 'typing')
        await bot.send_message(message.from_user.id, config.tutor)
    else:
        text = message.text[10:]
        db.append_massmail_text(text)
        await bot.send_message(message.from_user.id, 'Рассылка вскоре начнётся')
        # for i in db.get_all_tg_id():
        #     try:
        #         user = db.check_user(i)
        #         await bot.send_message(i, 'Просим не покупать медитации с предыдущего сообщения, так как там находятся неактуальные ссылки. Актуальные ссылки на платёжные системы находяться в этом сообщении.\n'
        #                                   'Забрать свои медитации до 1 апреля❤️',
        #                                reply_markup=keyboards.inline_massmail_keyboard(user['twelve_meditation_url'],
        #                                                                                user['six_meditation_url']))
        #     except Exception as error:
        #         print(error)
        #     finally:
        #         await asyncio.sleep(5)


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(mass_mailing, lambda message: message.from_user.id in config.admins,
                                commands='massmail')