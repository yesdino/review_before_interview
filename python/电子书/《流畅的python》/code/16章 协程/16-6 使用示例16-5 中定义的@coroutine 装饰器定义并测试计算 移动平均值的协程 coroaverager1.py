""" 使用示例16-5 中定义的@coroutine 装饰器定义并测试计算 移动平均值的协程 """
from functools import wraps


def coroutine(func):
    """装饰器：向前执行到第一个`yield`表达式，预激`func`"""
    @wraps(func)
    def primer(*args,**kwargs):     # 1 把被装饰的生成器函数替换成这里的 primer 函数；调用 primer 函数时，返回预激后的生成器。
        gen = func(*args,**kwargs)  # 2 调用被装饰的函数，获取生成器对象。
        next(gen)                   # 3 预激生成器。
        return gen                  # 4 返回生成器。
    return primer


@coroutine                      # 5
def averager():                 # 6 函数的定义体与示例16-3 完全一样。
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count


if __name__ == "__main__":
    coro_avg = averager()
    # ret = next(coro_avg)        # 不用预激了直接使用协程

    ret = coro_avg.send(10)
    print(ret)                  # 10.0

    ret = coro_avg.send(30)
    print(ret)                  # 20.0

    ret = coro_avg.send(5)
    print(ret)                  # 15.0