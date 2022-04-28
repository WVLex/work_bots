from aiogram import Bot, Dispatcher
from astro_bot.config import config


bot = Bot(config.token)
dp = Dispatcher(bot)

