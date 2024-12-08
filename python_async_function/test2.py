import asyncio


async def another_task():
    for i in range(3):
        print(f"Task running: {i}")
        await asyncio.sleep(1)


async def fn():
    print("one")
    await asyncio.sleep(1)
    await fn2()
    print('four')
    await asyncio.sleep(1)
    print('five')
    await asyncio.sleep(1)


async def fn2():
    await asyncio.sleep(1)
    print("two")
    await asyncio.sleep(1)
    print("three")


async def main():
    await asyncio.gather(fn(), another_task())


# Run the main coroutine
asyncio.run(main())
