# example of using an asyncio queue
from random import random
import asyncio
import time 
 
# coroutine to generate work
async def producer(queue):
    print('Producer: Running')
    start_time = time.time()
    # generate work
    for i in range(10):
        # generate a value
        value = i
        # block to simulate work
        await asyncio.sleep(random())
        # add to the queue
        print(f"> Product put {value}")
        await queue.put(value)
    # send an all done signal
    await queue.put(None)
    end_time = time.time()  # Record the end time
    print(f'Producer: Done in {end_time - start_time:.2f} seconds')

# coroutine to consume work
async def consumer(queue):
    print('Consumer: Running')
    start_time = time.time()
    # consume work
    while True:
        # get a unit of work
        item = await queue.get()
        # check for stop signal
        if item is None:
            break
        # report
        print(f'\t> Consumer got {item}')
    # all done
    end_time = time.time()  # Record the end time
    print(f'Consumer: Done in {end_time - start_time:.2f} seconds')

#entry point coroutine
async def main():
    # create the shared queue
    queue = asyncio.Queue()
    # run the producer and consumers
    await asyncio.gather(producer(queue), consumer(queue))
        
# start the asyncio program
asyncio.run(main())