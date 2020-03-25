from coroaverager1 import averager


coro_avg = averager()
ret = coro_avg.send(40)
print(ret)                  # 40.0

ret = coro_avg.send(50)
print(ret)                  # 45.0

ret = coro_avg.send('spam') # 协程内部运算不支持 string
print(ret)
