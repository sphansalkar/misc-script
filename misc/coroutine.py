import asyncio
import time


async def task_func():
    print('in task_func')
    time.sleep(20)
    with open('/tmp/task', 'w') as fd:
        fd.write("Async Task complete ...")
    return 'the result'

'''
async def main(loop):
    print('creating task')
    task = loop.create_task(task_func())
    # return_value = await task
'''

event_loop = asyncio.get_event_loop()
task = event_loop.create_task(task_func())
event_loop.run_until_complete(task_func())
event_loop.close()

print('task completed')
