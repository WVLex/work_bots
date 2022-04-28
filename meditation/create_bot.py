from aiogram import Bot, Dispatcher
from meditation.config import config


bot = Bot(config.meditation_token)
dp = Dispatcher(bot)