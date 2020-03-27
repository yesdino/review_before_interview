
"""
简单地调用一个协程并不会将其加入执行日程
"""

import asyncio

async def main():       # asyncio 语法：函数前面加上 async 就表示这是个协程
    print('hello')
    await asyncio.sleep(1)  # await 表异步执行，交给 asyncio 控制
    print('world')


# ----------------------------------------------------------
asyncio.run(main())
# hello
# world

# ----------------------------------------------------------
# main()              # 简单地调用一个协程并不会将其加入执行日程
# <coroutine object main at 0x1053bb7c8>