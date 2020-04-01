import asyncio

async def nested():
    return 42

async def main():
    # Schedule nested() to run soon concurrently with "main()".
    # nested() 日程将会在 main() 调用的同时一起运行
    task = asyncio.create_task(nested())

    # "task" can now be used to cancel "nested()", 
    # or can simply be awaited to wait until it is complete:
    ret = await task
    print(ret)


# ----------------------------------
asyncio.run(main())