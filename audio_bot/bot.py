import datetime
# import logging
from aiogram.utils import executor

from audio_bot.create_bot import dp
from audio_bot.handlers import client


client.register_handlers_client(dp)

executor.start_polling(dp)