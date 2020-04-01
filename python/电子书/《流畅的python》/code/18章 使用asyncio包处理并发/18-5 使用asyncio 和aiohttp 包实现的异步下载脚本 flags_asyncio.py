import asyncio
import aiohttp                                      # ➊ 必须安装 aiohttp 包，它不在标准库中。
from flags import BASE_URL, save_flag, show, main   # ➋ 重用 flags 模块（见示例17-2）中的一些函数。


"""
看官方给出的写 asyncio task 教程吧
https://docs.python.org/zh-cn/3/library/asyncio-task.html
"""


@asyncio.coroutine                                  # ➌ 协程应该使用 @asyncio.coroutine 装饰。
def get_flag(cc):
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
    resp = yield from aiohttp.request('GET', url)   # ➍ 阻塞的操作通过协程实现，客户代码通过 yield from 把职责委托给协程，以便异步运行协程。
    image = yield from resp.read()                  # ➎ 读取响应内容是一项单独的异步操作。
    return image


@asyncio.coroutine
def download_one(cc):                               # ➏ download_one 函数也必须是协程，因为用到了yield from。
    image = yield from get_flag(cc)                 # ➐ 与依序下载版 download_one 函数唯一的区别是这一行中的 yield from；函数定义体中的其他代码与之前完全一样。
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc


def download_many(cc_list):
    loop = asyncio.get_event_loop()                 # ➑ 获取事件循环底层实现的引用。
    to_do = [download_one(cc) for cc in sorted(cc_list)] # ➒ 调用 download_one 函数获取各个国旗，然后构建一个协程对象列表。
    wait_coro = asyncio.wait(to_do)                 # ➓ 虽然函数的名称是 wait，但它不是阻塞型函数。wait 是一个协程，等传给它的所有协程运行完毕后结束（这是wait 函数的默认行为；参见这个示例后面的说明）。
    res, _ = loop.run_until_complete(wait_coro)     # 11 执行事件循环，直到 wait_coro 运行结束；事件循环运行的过程中，这个脚本会在这里阻塞。我们忽略run_until_complete 方法返回的第二个元素。下文说明原因。
    loop.close()                                    # 12 关闭事件循环。
    return len(res)


if __name__ == '__main__':
    main(download_many)
    """
    在 flags_asyncio.py 脚本中，
    在 download_many 函数中调用 loop.run_until_complete 方法时，事件循环驱动各个 download_one 协程，
    运行到第一个 yield from 表达式处，那个表达式又驱动各个 get_flag 协程，
    运行到第一个 yield from 表达式处，调用 aiohttp.request(...) 函数。
    这些调用都不会阻塞，因此【在零点几秒内所有请求全部开始】。

    asyncio 的基础设施获得第一个响应后，事件循环把响应发给等待结果的 get_flag 协程。
    得到响应后， get_flag 向前执行到下一个 yield from 表达式处，调用 resp.read() 方法，然后把控制权还给主循环。
    其他响应会陆续返回（因为请求几乎同时发出）。
    get_flag 内所有协程都获得结果后，委派生成器 download_one 恢复，保存图像文件。

    因为异步操作是交叉执行的，所以并发下载多张图像所需的总时间比依序下载少得多。我
    使用 asyncio 包发起了 600 个 HTTP 请求，获得所有结果的时间比依序下载快 70 倍。
    """