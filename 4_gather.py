import asyncio
import time

async def fetch(delay,id):
    print()
    print(f"fetching for id:{id}")
    await asyncio.sleep(1)
    print("fetching completed !!")
    print()
    return {f"data fetched for {id}"}

async def main():
    #gather runs all of the passed coroutines concurrently and gathers all the results of them in a list
    results = await asyncio.gather(fetch(1,1),fetch(1,2))
    # disadvantages of gather--
    # no error handling
    # doesnt stop the process if one of the coroutine fails
    for res in results:
        print(res)


start = time.perf_counter()
asyncio.run(main())
total = round(time.perf_counter()-start,2)
print(f"total time taken: {total} seconds")