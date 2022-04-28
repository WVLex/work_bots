from meditation.create_bot import dp
from meditation.handlers import client, admin
# import logging
# logging.basicConfig(level=logging.DEBUG)


client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
