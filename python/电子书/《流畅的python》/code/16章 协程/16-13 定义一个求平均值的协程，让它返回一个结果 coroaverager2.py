from collections import namedtuple

Result = namedtuple('Result', 'count average')

def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break                   # 1 为了返回值，协程必须正常终止；因此，这一版 averager 中有个条件判断，以便退出累计循环。
        total += term
        count += 1
        average = total/count
    return Result(count, average)   # 2 返回一个namedtuple，包含count 和average 两个字段。在Python 3.3 之前，如果生成器返回值，解释器会报句法错误。

    
if __name__ == "__main__":
    coro_avg = averager()
    next(coro_avg)
    ret = coro_avg.send(10)         # 1 这一版不产出值。
    print(ret)

    ret = coro_avg.send(30)
    print(ret)

    ret = coro_avg.send(6.5)
    print(ret)

    # ret = coro_avg.send(None)     # 2 发送None 会终止循环，导致协程结束，返回结果。 StopIteration: Result(count=3, average=15.5)
    try:
        coro_avg.send(None)
    except StopIteration as exc:
        result = exc.value
    print(result)                   # Result(count=3, average=15.5)
