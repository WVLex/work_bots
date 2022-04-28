from aiogram import types
from aiogram import Dispatcher
import asyncio

from yasnamak.create_bot import bot
from yasnamak.db import db
from yasnamak.config import config
from yasnamak.keyboards import keyboards


async def start(message: types.Message):
    if not db.check_user(message.from_user.id):  # Проверка существования пользователя
        db.append_user(message.from_user.id)
    user = db.check_user(message.from_user.id)

    if user['pay'] is not False:
        data = db.randomizer_for_cards_and_poems()
        photo_id = db.get_photo(data['card_number'])

        await bot.send_chat_action(message.from_user.id, 'typing')
        await bot.send_message(message.from_user.id, config.first_msg_subscribe)
        await bot.send_photo(message.from_user.id, photo_id)

        await bot.send_chat_action(message.from_user.id, 'typing')
        await bot.send_message(message.from_user.id, data['poem'])
        if user['pay'] is None:
            db.change_pay_value(message.from_user.id, False)

        await bot.send_chat_action(message.from_user.id, 'typing')
        my_message = await bot.send_message(message.from_user.id, config.request_feedback,
                                            reply_markup=keyboards.inline_request_feedback_keyboard(),
                                            parse_mode='Markdown')
        db.update_message_id_to_edit(message.from_user.id, my_message.message_id)

    if user['pay'] is False:
        await bot.send_chat_action(message.from_user.id, 'typing')
        await bot.send_message(message.from_user.id, config.if_pay_false)


async def subscribe(message: types.Message):
    await bot.send_chat_action(message.from_user.id, 'typing')
    right_message = await bot.send_message(message.from_user.id, config.request_subscribe,
                                           reply_markup=keyboards.inline_request_subscribe_keyboard())
    db.update_message_id_to_edit(message.from_user.id, right_message.message_id)
    del right_message


# async def pay(message):
#     url, label = db.get_pay_url_and_label(message.from_user.id)
#     db.update_label(message.from_user.id, label)
#     await bot.send_chat_action(message.from_user.id, 'typing')
#     await bot.send_message(message.from_user.id, config.pay_message,
#                            reply_markup=keyboards.inline_pay_button(url))
#     del url
#     del label


async def feedback(call: types.CallbackQuery):
    message_id = db.check_user(call.from_user.id)['message_id_to_edit']

    await bot.send_chat_action(call.from_user.id, 'typing')
    await bot.edit_message_reply_markup(call.from_user.id, message_id, reply_markup=None)
    del message_id

    if call.data == 'feedback_yes':
        await bot.send_chat_action(call.from_user.id, 'typing')
        await bot.send_message(call.from_user.id, config.if_feedback_yes)

    else:
        await bot.send_chat_action(call.from_user.id, 'typing')
        await bot.send_message(call.from_user.id, config.if_feedback_no)

    await bot.send_chat_action(call.from_user.id, 'typing')
    message = await bot.send_message(call.from_user.id, config.request_subscribe,
                                     reply_markup=keyboards.inline_request_subscribe_keyboard(),
                                     parse_mode='Markdown')
    db.update_message_id_to_edit(call.from_user.id, message.message_id)
    del message


async def send_card(call: types.CallbackQuery):
    if db.check_user(call.from_user.id)['pay'] is True:
        data = db.randomizer_for_cards_and_poems()
        photo_id = db.get_photo(data['card_number'])
        await bot.send_chat_action(call.from_user.id, 'typing')
        await bot.send_message(call.from_user.id, config.first_msg_subscribe)
        await bot.send_photo(call.from_user.id, photo_id)
        await bot.send_chat_action(call.from_user.id, 'typing')
        await bot.send_message(call.from_user.id, data['poem'],
                               reply_markup=keyboards.inline_main_keyboard())
    else:
        await bot.send_chat_action(call.from_user.id, 'typing')
        await bot.send_message(call.from_user.id, config.if_pay_false)


async def subscribe_yes(call: types.CallbackQuery):
    db.update_time_to_send_message(call.from_user.id)
    db.update_everyday_newsletter_time(call.from_user.id)
    message_id = db.check_user(call.from_user.id)['message_id_to_edit']
    await bot.delete_message(call.from_user.id, message_id)
    await bot.send_chat_action(call.from_user.id, 'typing')
    await bot.send_message(call.from_user.id, config.success_subscribe)


async def subscribe_no(call: types.CallbackQuery):
    await bot.send_chat_action(call.from_user.id, 'typing')
    await bot.send_message(call.from_user.id, config.user_cancel_subscribe)
    db.set_none_in_time_to_send_message(call.from_user.id)
    db.delete_everyday_newsletter_time(call.from_user.id)
    message_id = db.check_user(call.from_user.id)['message_id_to_edit']
    await bot.edit_message_reply_markup(call.from_user.id, message_id)
    del message_id


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start, commands='start')
    dp.register_message_handler(subscribe, commands='subscribe')

    # Отработка обратной связи
    dp.register_callback_query_handler(feedback, text=['feedback_yes', 'feedback_no'])

    # Отправка карты
    dp.register_callback_query_handler(send_card, text='send_card')

    # Отработка запроса о подписке
    dp.register_callback_query_handler(subscribe_yes, text='subscribe_yes')
    dp.register_callback_query_handler(subscribe_no, text='subscribe_no')
