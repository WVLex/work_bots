from aiogram import Bot, Dispatcher
from bagriy_bot.config import config


bot = Bot(config.token)
dp = Dispatcher(bot)
