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
    tasklist=[]
    async with asyncio.TaskGroup() as tg:
        for i in range(2):
            task=tg.create_task(fetch(1,i))
            tasklist.append(task)
    results=[]
    for t in tasklist:
        results.append(t.result())

    for res in results:
        print(f"recieved results: {res}") 


start=time.perf_counter()
asyncio.run(main())
total = time.perf_counter()-start
print(f"total time taken:{total}")