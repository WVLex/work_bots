from yasnamak.create_bot import dp
from yasnamak.handlers import client, admin
from aiogram import executor
# import logging
# logging.basicConfig(level=logging.DEBUG)


client.register_handlers_client(dp)
# admin.register_handlers_admin(dp)

executor.start_polling(dp)
