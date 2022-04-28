from aiogram import Bot, Dispatcher
from yasnamak.config import config


bot = Bot(config.token)
dp = Dispatcher(bot)