# from aiogram.utils import executor
from astro_bot.create_bot import dp
import logging
logging.basicConfig()
logging.getLogger('apscheduler').setLevel(logging.DEBUG)


from astro_bot.handlers import admin, client


admin.register_handlers_admin(dp)
client.register_handlers_client(dp)

# executor.start_polling(dp)