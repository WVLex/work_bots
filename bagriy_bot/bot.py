from aiogram.utils import executor
from bagriy_bot.create_bot import dp
import logging
logging.basicConfig()
logging.getLogger('apscheduler').setLevel(logging.DEBUG)


from bagriy_bot.handlers import client


client.register_handlers_client(dp)

# executor.start_polling(dp)