from aiogram.utils import executor

from new_makbot.create_bot import dp
# import logging
# logging.basicConfig()
# logging.getLogger('apscheduler').setLevel(logging.DEBUG)


from new_makbot.handlers import client


client.register_handlers_client(dp)
# executor.start_polling(dp)

