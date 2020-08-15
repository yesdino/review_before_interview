"""
要真正运行一个协程，asyncio 提供了三种主要机制
"""

import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep (delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')     # 等待一个协程
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")


# ------------------------------------
asyncio.run(main())         # asyncio.run() 函数用来运行最高层级的入口点
# started at 17:13:52
# hello
# world
# finished at 17:13:55