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



# semaphores are like locks but we can set how many coroutines can access resource at a time
# Generally used for Throttle our program so that it doesnt get overloaded !

# sample o/p 
# Accessing resource with id: 0
# Accessing resource with id: 1
# Releasing resource with id:0
# Releasing resource with id:1
# Accessing resource with id: 2
# Accessing resource with id: 3
# Releasing resource with id:2
# Releasing resource with id:3
# Accessing resource with id: 4
# Releasing resource with id:4