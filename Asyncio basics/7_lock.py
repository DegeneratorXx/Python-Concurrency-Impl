import asyncio
shared_resource=0

lock=asyncio.Lock()

async def updateResource():
    global shared_resource
    async with lock:
        print()
        print(f"resource before updation: {shared_resource}")
        shared_resource+=1
        await asyncio.sleep(1)
        print(f"after updation: {shared_resource}")
        print()

async def main():
    await asyncio.gather(updateResource(),
                         updateResource(),
                         updateResource(),
                         updateResource())

asyncio.run(main())
