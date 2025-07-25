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
    task1= asyncio.create_task(fetch(1,1))
    task2= asyncio.create_task(fetch(1,2))
    task3= asyncio.create_task(fetch(1,3))

    res1 = await task1
    res2 = await task2
    res3 = await task3

    print(res1)
    print(res3)
    print(res2)

# create_task make our tasks to run simultaneously !!!
# here whole process will take only 1 sec


start = time.perf_counter()
asyncio.run(main())    
total= round(time.perf_counter()-start,2)
print(f"task completed in {total} seconds")