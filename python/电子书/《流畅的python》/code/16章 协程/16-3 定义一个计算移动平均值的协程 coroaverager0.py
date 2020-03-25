""" 定义一个计算移动平均值的协程 """


"""
仅当调用方在协程上调用.close() 方法，
或者没有对协程的引用而被垃圾回收程序回收时，这个协程才会终止。
"""
def averager():
    total = 0.0
    count = 0
    average = None
    while True:                 # 永远都能访问到 yield, 永远不会出现 StopIteration
        term = yield average
        total += term
        count += 1
        average = total/count


coro_avg = averager()
ret = next(coro_avg)        # 预激协程
print(ret)                  # None

ret = coro_avg.send(10)
print(ret)                  # 10.0

ret = coro_avg.send(30)
print(ret)                  # 20.0

ret = coro_avg.send(5)
print(ret)                  # 15.0
