import asyncio

shared_resource = 0

# Comment or uncomment this to see the effect
# lock = asyncio.Lock()

async def updateResource():
    global shared_resource
    # async with lock:
    print()
    print(f"resource before updation: {shared_resource}")
    
    # Simulate async context switch (lets other coroutines run)
    await asyncio.sleep(0)
    
    shared_resource += 1
    print(f"after updation: {shared_resource}")
    print()

async def main():
    await asyncio.gather(
        updateResource(),
        updateResource(),
        updateResource(),
        updateResource()
    )

asyncio.run(main())
