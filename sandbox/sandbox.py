from aiogram.utils.deep_linking import get_start_link
import asyncio

async def kek():
    await asyncio.sleep(1)
    print('aaa')
    link = await get_start_link('get', encode=True)
    print(link)

event_loop = asyncio.get_event_loop()
task_list = [event_loop.create_task(kek()), ]
tasks = asyncio.wait(task_list)
event_loop.run_forever()