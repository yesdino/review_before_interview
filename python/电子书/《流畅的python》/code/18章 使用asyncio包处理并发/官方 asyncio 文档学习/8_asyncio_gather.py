import asyncio

async def factorial(name, number):
    f = 1
    for i in range(1, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(2)
        f *= i
    print(f"-----Task {name}: factorial({number}) = {f}")
    print(f"========================================")

async def main():
    # Schedule three calls *concurrently*:
    await asyncio.gather(
        factorial("A", 1),
        factorial("B", 2),
        factorial("C", 3),
    )

asyncio.run(main())

