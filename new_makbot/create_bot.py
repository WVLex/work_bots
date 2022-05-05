from aiogram import Bot, Dispatcher
from new_makbot.config import config


bot = Bot(config.token)
dp = Dispatcher(bot)


