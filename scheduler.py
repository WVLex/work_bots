from astro_bot.astro_bot_scheduler import update_astro_bot
from meditation.massmailing import check_updates
# from bagriy_bot.bagriy_scheduler import bagriy_bot as bagriy_bot_job
# from yasnamak.yasnamak_scheduler import yasnamak_updater as yasnamak_bot_job
from audio_bot.audiobot_scheduler import update_audio_bot
from create_scheduler import scheduler_astrobot, scheduler_audiobot
import asyncio
import logging

logging.basicConfig()
logging.getLogger('apscheduler').setLevel(logging.DEBUG)
scheduler_astrobot.start()
scheduler_audiobot.start()


event_loop = asyncio.get_event_loop()
task_list = [
    event_loop.create_task(update_astro_bot()),
    event_loop.create_task(check_updates()),
    event_loop.create_task(update_audio_bot()),
    # event_loop.create_task(yasnamak_bot_job()),
]
tasks = asyncio.wait(task_list)
event_loop.run_forever()
    # event_loop.create_task(bagriy_bot_job()),
