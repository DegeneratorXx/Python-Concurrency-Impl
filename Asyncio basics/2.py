import asyncio

async def fetch(delay,id):
    print()
    print(f"fetching for id:{id}")
    await asyncio.sleep(1)
    print("fetching completed !!")
    print()
    return {f"data fetched for {id}"}

async def main():
    print("start of main coroutine")
    task1= fetch(1,"a")
    task2= fetch(1,"b")
    
    print("now startig the fetching below!")
    res1= await task1
    print(f"Done, results: {res1}")
    res2= await task2
    print(f"Done, results: {res2}")
    print("end of main coroutine")

# Here task completion took 2 sec as both objects are awaited at diff time
# if we want them to occur asynchronously we need to run them simultaneously

asyncio.run(main())    