import asyncio
import collections
import aiohttp
from aiohttp import web
import tqdm
from flags2_common import main, HTTPStatus, Result, save_flag

# 默认设为较小的值，防止远程网站出错
# 例如 503 - Service Temporarily Unavailable
DEFAULT_CONCUR_REQ = 5
MAX_CONCUR_REQ = 1000

class FetchError(Exception):                    # ➊ 这个自定义的异常用于包装其他HTTP 或网络异常，并获取country_code，以便报告错误。
    def __init__(self, country_code):
        self.country_code = country_code


@asyncio.coroutine
def get_flag(base_url, cc):                     # ➋ get_flag 协程有三种返回结果：返回下载得到的图像；HTTP 响应码为404 时，抛出web.HTTPNotFound 异常；返回其他HTTP 状态码时，抛出aiohttp.HttpProcessingError异常。
    url = '{}/{cc}/{cc}.gif'.format(base_url, cc=cc.lower())
    resp = yield from aiohttp.request('GET', url)
    if resp.status == 200:
        image = yield from resp.read()
        return image
    elif resp.status == 404:
        raise web.HTTPNotFound()
    else:
        raise aiohttp.HttpProcessingError(
            code=resp.status, message=resp.reason,
            headers=resp.headers)


@asyncio.coroutine                                  # asyncio.Semaphore 类（https://docs.python.org/3/library/asyncio-sync.html#asyncio. Semaphore）
def download_one(cc, base_url, semaphore, verbose): # ➌ semaphore 参数是 asyncio.Semaphore 类的实例。Semaphore 类是同步装置，用于限制并发请求数量。
    try:
        with (yield from semaphore):                # ➍ 在yield from 表达式中把 semaphore 当成上下文管理器使用，防止阻塞整个系统：如果semaphore 计数器的值是所允许的最大值，只有这个协程会阻塞。
            image = yield from get_flag(base_url, cc) # ➎ 退出这个with 语句后，semaphore 计数器的值会递减，解除阻塞可能在等待同一个 semaphore 对象的其他协程实例。
    except web.HTTPNotFound:                        # ➏ 如果没找到国旗，相应地设置Result 的状态。
        status = HTTPStatus.not_found
        msg = 'not found'
    except Exception as exc:
        raise FetchError(cc) from exc               # ➐ 其他异常当作FetchError 抛出， 传入国家代码， 并使用“PEP 3134 — Exception Chaining and Embedded Tracebacks”（https://www.python.org/dev/peps/pep-3134/）引入的raise X from Y 句法链接原来的异常。
    else:
        save_flag(image, cc.lower() + '.gif')       # ➑ 这个函数的作用是把国旗文件保存到硬盘中。
        status = HTTPStatus.ok
        msg = 'OK'

    if verbose and msg:
        print(cc, msg)
    return Result(status, cc)


@asyncio.coroutine
def downloader_coro(cc_list, base_url, verbose, concur_req):    # ➊ 
    counter = collections.Counter()
    semaphore = asyncio.Semaphore(concur_req)                   # ➋ 
    to_do = [download_one(cc, base_url, semaphore, verbose) for cc in sorted(cc_list)] # ➌ 
    to_do_iter = asyncio.as_completed(to_do)                    # ➍ 
    if not verbose:
        to_do_iter = tqdm.tqdm(to_do_iter, total=len(cc_list))  # ➎ 
    for future in to_do_iter:                                   # ➏ 
        try:
            res = yield from future                             # ➐ 
        except FetchError as exc:                               # ➑ 
            country_code = exc.country_code                     # ➒ 
            try:
                error_msg = exc.__cause__.args[0]               # ➓ 
            except IndexError:
                error_msg = exc.__cause__.__class__.__name__
            if verbose and error_msg:
                msg = '*** Error for {}: {}'
                print(msg.format(country_code, error_msg))
            status = HTTPStatus.error
        else:
            status = res.status
        counter[status] += 1
    return counter


def download_many(cc_list, base_url, verbose, concur_req):
    loop = asyncio.get_event_loop()
    coro = downloader_coro(cc_list, base_url, verbose, concur_req)
    counts = loop.run_until_complete(coro)
    loop.close()