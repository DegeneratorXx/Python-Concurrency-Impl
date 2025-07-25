import asyncio


async def access_resource(semaphore,id):
    async with semaphore:
        print(f"Accessing resource with id: {id}")

        await asyncio.sleep(1)
        print(f"Releasing resource with id:{id}")

async def main():
    semaphore= asyncio.Semaphore(2) # allowing 2 coroutines to enter at a time
    await asyncio.gather(*(access_resource(semaphore,i) for i in range(5)))

asyncio.run(main())