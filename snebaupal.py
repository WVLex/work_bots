import json
from flask import Flask, request, Response, redirect
from aiogram import Bot, Dispatcher, types

# Скрипты
# import db
# import config
from meditation.config import config as meditation_config
from meditation.db import db as meditation_db

# Astro-bot
from astro_bot.bot import dp as astro_dp
# Meditation-bot
from meditation.main import dp as meditation_dp
# bagriy_bot
# from bagriy_bot.create_bot import dp as bagriy_bot_dp
# from bagriy_bot.config import texts as bagriy_bot_texts
# from bagriy_bot.config import config as bagriy_bot_config
# from bagriy_bot.db import db as bagriy_bot_db
# Audio_bot
from audio_bot.bot import dp as audio_bot_dp
from audio_bot.config import texts as audio_bot_texts
from audio_bot.config import config as audio_bot_config
from audio_bot.keyboards import client_keyboards as audio_bot_client_keyboards

relax_text = "Расслабиться - https://t.me/+ZE45RiJoC5ExYTM6"
anxiety_text = "Снять тревогу - https://t.me/+WpYG6uUFryRiN2Q6"
full_text = "Наполниться - https://t.me/+TRkD5Mz8ApljMGQy"
doit_text = "Действовать - https://t.me/+duXKPActP5E4OWVi"
twelve_text = 'Осознанные медитации - https://t.me/+kJZ1UhGT368yM2My'
six_text = 'половинка - https://t.me/+A6epkGVd7qdjZmUy'
quickpay_twelve_url = 'https://yoomoney.ru/quickpay/confirm.xml?' \
                      'receiver=4100117596986931&' \
                      'label={}&' \
                      'quickpay-form=shop&' \
                      'targets=12+осознанных+медитаций&' \
                      'paymentType=SB&' \
                      'sum=12000'
quickpay_six_url = 'https://yoomoney.ru/quickpay/confirm.xml?' \
                   'receiver=4100117596986931&' \
                   'label={}&' \
                   'quickpay-form=shop&' \
                   'targets=6+осознанных+медитаций&' \
                   'paymentType=SB&' \
                   'sum=7000'


app = Flask(__name__)




@app.route("/", methods=['GET', 'POST'])
async def hello_world():
    if request.method == 'POST':
        try:
            data = make_dict(request.get_data(as_text=True))
            label = data['label']
            if label[:4] != 'book':
                bot = Bot(meditation_config.meditation_token)
                tg_id = meditation_db.get_tg_id_from_label(label)
                if label[:4] == 'relx':
                    await bot.send_message(tg_id, "Держи❤️\n" + relax_text)
                elif label[:4] == 'anxi':
                    await bot.send_message(tg_id, "Держи❤️\n" + anxiety_text)
                elif label[:4] == 'full':
                    await bot.send_message(tg_id, "Держи❤️\n" + full_text)
                elif label[:4] == 'doit':
                    await bot.send_message(tg_id, "Держи❤️\n" + doit_text)
                elif label[:4] == 'twlv':
                    await bot.send_message(tg_id, "Держи❤️\n" + twelve_text)
                elif label[:4] == 'sixx':
                    await bot.send_message(tg_id, "Держи❤️\n" + six_text)
                meditation_db.change_pay_value(tg_id, True)
                del bot
            else:
                await audio_bot_dp.bot.send_audio(int(label[4:]),
                                                  audio='CQACAgIAAxkBAAPKYmvCW80pMHT6c1AQ8nphPau0xBEAAkkfAAI9DmBLPghcRsjVqbMkBA',
                                                  title='Часть 2',
                                                  performer='Ясна Токарик',
                                                  protect_content=True)
                await audio_bot_dp.bot.send_message(int(label[4:]), audio_bot_texts.second_audio_text,
                                                    reply_markup=audio_bot_client_keyboards.get_audio())
        except Exception as error:
            print('Неверная обработка POST. Ошибка {}'.format(error))

        return 'Okes', 200
    else:
        return 'Hello world meditation GET', 200


# # Bagriy_bot
# @app.route('/bagriy_bot/<label>', methods=['GET', 'POST'])
# async def bagriy_bot(label=None):
#     if request.method == 'POST':
#         bot = bagriy_bot_dp.bot
#         tg_id = label
#         bagriy_bot_db.update_value(tg_id, 'pay', True)
#         await bot.send_message(tg_id, bagriy_bot_texts.success_pay_text)
#         return 'ok', 200
#     elif request.method == 'GET':
#         return redirect(bagriy_bot_config.url + bagriy_bot_config.label.format(label=label))



# Astro_bot
@app.route('/5212521293:AAHJmvtFdPKLEFOqQfM53R_Vc5Y5jag-EPQ', methods=['POST'])
async def astro_bot():
    update = json.loads(request.stream.read().decode('utf-8'))
    update = types.Update.to_object(update)
    Bot.set_current(astro_dp.bot)
    Dispatcher.set_current(astro_dp)
    await astro_dp.process_update(update)
    return Response('Ok', 200)


# Meditation_bot
@app.route('/5267243589:AAF6vGBHEqWuvwR93g3uQflQtXPBW8rH6aA', methods=["POST"])
async def meditation_bot():
    update = json.loads(request.stream.read().decode('utf-8'))
    update = types.Update.to_object(update)
    Bot.set_current(meditation_dp.bot)
    Dispatcher.set_current(meditation_dp)
    await meditation_dp.process_update(update)
    return Response('OK', 200)


# Audio_bot
@app.route('/5352391646:AAERyJaOA3wUg1Bd6GvtWh_eeNX4In3dxkk', methods=["POST"])
async def audio_bot():
    update = json.loads(request.stream.read().decode('utf-8'))
    update = types.Update.to_object(update)
    Bot.set_current(audio_bot_dp.bot)
    Dispatcher.set_current(audio_bot_dp)
    await audio_bot_dp.process_update(update)
    return Response('OK', 200)


@app.route('/audio_bot/<label>', methods=['GET'])
async def audio_bot_pay(label=None):
    return redirect(audio_bot_config.pay_url.format(label))


@app.route('/audio_bot/lava', methods=['GET'])
async def audio_bot_pay_lava(label=None):
    return redirect(audio_bot_config.pay_url.format(label))


@app.route('/meditation/twelve/<label>', methods=['GET'])
async def twelve(label=None):
    return Response('<h1>Акция окончена</h1>', 200)


@app.route('/meditation/half/<label>', methods=['GET'])
async def half(label=None):
    return Response('<h1>Акция окончена</h1>', 200)


# @app.route('/meditation/<label>')
# def meditation_pay(label=None):
#     return render_template('buttons.html', label=label), 200


def make_dict(data):
    data = data.split('&')
    new_dict = {i.split('=')[0]: i.split('=')[1] for i in data}
    return new_dict
#
# app.run(debug=True)