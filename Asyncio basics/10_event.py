import asyncio

async def waiter(event):
    print("waiting for the event to be set")
    await event.wait()
    print("event setted lets gooo..")

async def setter(event):
    print("setting up the event")
    event.set()
    print("setting up complete")

async def main():

    event =asyncio.Event()
    await asyncio.gather(waiter(event),setter(event))

asyncio.run(main())
