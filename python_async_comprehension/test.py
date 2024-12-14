import asyncio


async def async_number_generator():
    for i in range(5):
        await asyncio.sleep(1)  # Simulate async I/O
        yield i

async def main():
    result = [num async for num in async_number_generator() if num % 2 == 0]
    print(result)

asyncio.run(main())

