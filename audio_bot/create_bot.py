from aiogram import Bot, Dispatcher
from audio_bot.config import config


bot = Bot(config.token)
dp = Dispatcher(bot)


