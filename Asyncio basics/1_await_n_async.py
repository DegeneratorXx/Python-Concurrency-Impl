import asyncio

async def getData(delay):
    print()
    print("fetching..")
    await asyncio.sleep(delay)
    print("fetching complete")
    print()
    return {"data":"some data"}



async def main():
    print("start of main coroutine")
    task = getData(1)
    print("now starting the fetching below!")
    res= await task
    print(f"Done, results: {res}")
    print("end of main coroutine")


# coroutine only starts when it is awaited.
# await keyword can only be used inside the coroutine!
asyncio.run(main())   


