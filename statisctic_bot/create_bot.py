from aiogram import Bot, Dispatcher
from statisctic_bot.config import config


bot = Bot(config.token)
dp = Dispatcher(bot)


