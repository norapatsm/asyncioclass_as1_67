from random import random
import asyncio

# coroutine 
async def cook(food_name):
    time_cook = 1 + random()
    print(f'Microwave ({food_name}) : Cooking {time_cook} seconds')
    await asyncio.sleep(time_cook)
    print(f'Microwave ({food_name}) : Finished cooking')
    return food_name, time_cook

# main coroutine
async def main():
    tasks = [asyncio.create_task(cook('Rice')), 
             asyncio.create_task(cook('Noodle')), 
             asyncio.create_task(cook('Curry'))]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    for task in done:
        food_name, time_cook = task.result()
        print(f'Completed task: 1\n - {food_name} is completed in {time_cook} seconds')
    print(f'Uncompleted task: {len(pending)}')

# begin asyncio program
asyncio.run(main())
