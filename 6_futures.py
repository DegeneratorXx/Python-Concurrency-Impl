import asyncio

async def set_future_value(fut):
    print("Setting future value after 1 second...")
    await asyncio.sleep(1)
    fut.set_result("Hello from the future!")

async def main():
    loop = asyncio.get_running_loop()
    
    fut = loop.create_future()  # create an empty future
    
    # Start a coroutine that sets the future's value
    asyncio.create_task(set_future_value(fut))
    
    print("Waiting for future result...")
    result = await fut  # Wait for the future to have a value
    print(f"Got future result: {result}")

asyncio.run(main())
