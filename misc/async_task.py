import asyncio
import time

async def task_func():
    print('in task_func')
    print('task completed')

async def main(loop):
    print('creating task')
    task = loop.create_task(task_func())
    print('Continue ....')
    # return_value = await task

event_loop = asyncio.get_event_loop()
try:
    while True:
        time.sleep(5)
        event_loop.run_until_complete(main(event_loop))
        print ("After run_until_complete ...")
finally:
    event_loop.close()
