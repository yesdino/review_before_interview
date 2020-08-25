# import gevent


# def f(n):
#     for i in range(n):
#         print(gevent.getcurrent(), i)

# g1 = gevent.spawn(f, 5)
# g2 = gevent.spawn(f, 5)
# g3 = gevent.spawn(f, 5)
# g1.join()
# g2.join()
# g3.join()


from gevent import monkey; monkey.patch_all()
import gevent
import time


def foo():
    print('11')
    time.sleep(3)   # 这里遇到耗时操作就直接去执行下面的 bar() 了
    print('22')

def bar():
    print('33')
    print('44')

gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar),
])