from aiogram.utils import executor

from statisctic_bot.create_bot import dp
import logging
logging.basicConfig(level=logging.INFO)
# logging.getLogger('apscheduler').setLevel(logging.DEBUG)


from statisctic_bot.handlers import client


client.register_handlers_client(dp)
# executor.start_polling(dp)
