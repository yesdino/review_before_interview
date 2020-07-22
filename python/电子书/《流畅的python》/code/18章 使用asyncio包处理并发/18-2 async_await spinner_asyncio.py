#!/usr/bin/env python3

# spinner_asyncio.py

# credits: Example by Luciano Ramalho inspired by
# Michele Simionato's multiprocessing example in the python-list:
# https://mail.python.org/pipermail/python-list/2009-February/538048.html

# BEGIN SPINNER_ASYNCIO
import asyncio
import itertools


async def spin(msg):                        # 1) 
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        print(status, flush=True, end='\r')
        try:
            await asyncio.sleep(.2)         # 2) IO 休眠不会阻塞事件循环
        except asyncio.CancelledError:      # 3) 是外层调用 cancel() 发出了取消请求，因此退出循环。
            break
    print(' ' * len(status), end='\r')


async def slow_function():                  # 4) slow_function 函数是协程，在用休眠假装进行 I/O 操作时，使用 await 驱动，挂起后继续执行事件循环。
    # 假设是耗时很长的 IO function
    await asyncio.sleep(3)                  # 5) await 表达式挂起状态，把控制权交给主循环，在休眠结束后恢复这个协程。
    return 42


async def supervisor():                     # 6) supervisor 函数也是协程，因此可以使用 await 驱动 slow_function 函数。
    spinner = asyncio.create_task(spin('thinking!'))  # 7) 创建任务，并开始执行（你可以理解为类似线程）
    print('spinner object:', spinner)       # 8) 
    result = await slow_function()          # 9) 驱动 slow_function() 函数。当 slow_function() 挂起时事件循环继续运行，因为 slow_function 函数最后使用 await asyncio.sleep(3) 表达式把控制权交回给了主循环。结束后，获取返回值 42。
    spinner.cancel()                        # 10) 效果：耗时很长的 IO function 结束了，光标不转了。返回结果。就是模仿 loading 的效果
    return result


def main():
    result = asyncio.run(supervisor())      # 11) 
    print('Answer:', result)


if __name__ == '__main__':
    main()
# END SPINNER_ASYNCIO