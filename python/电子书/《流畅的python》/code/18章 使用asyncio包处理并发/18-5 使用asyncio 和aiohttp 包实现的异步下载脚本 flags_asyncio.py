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
    to_do = [download_one(cc) for cc in sorted(cc_list)] # ➒ 调用 download_one 函数获取各个国旗，然后构建一个生成器对象列表。
    wait_coro = asyncio.wait(to_do)                 # ➓ 虽然函数的名称是 wait，但它不是阻塞型函数。wait 是一个协程，等传给它的所有协程运行完毕后结束（这是wait 函数的默认行为；参见这个示例后面的说明）。
    res, _ = loop.run_until_complete(wait_coro)     # 11 执行事件循环，直到 wait_coro 运行结束；事件循环运行的过程中，这个脚本会在这里阻塞。我们忽略run_until_complete 方法返回的第二个元素。下文说明原因。
    loop.close()                                    # 12 关闭事件循环。
    return len(res)


if __name__ == '__main__':
    main(download_many)