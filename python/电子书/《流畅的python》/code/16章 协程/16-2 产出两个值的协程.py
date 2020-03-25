from inspect import getgeneratorstate


def simple_coro2(a):
    print('-> Started: a =', a)
    b = yield a                     # yield 右边：产出，外界能得到的返回值； yield 左边：接收，接收到外界 send 的值；顺序：先右边再左边，先出去再回来
    print('-> Received: b =', b)
    c = yield a + b
    print('-> Received: c =', c)
   

my_coro2 = simple_coro2(14)
a = next(my_coro2)          # '-> Started: a = 14' 之后悬停在 yield 语句那行：产出返回 a 的值，并且暂停，等待下面 send 为 b 赋值
print(a)                    # yield a 出来的 14
# -------------------------------------------------------------------------
a_b = my_coro2.send(28)     # '-> Received: b = 28' 之后悬停在 yield 语句那行：产出返回 a + b 的值，并且暂停，等待下面 send 为 c 赋值
print(a_b)                  # yield a + b 出来的 42
# print(getgeneratorstate(my_coro2))  # GEN_SUSPENDED
# -------------------------------------------------------------------------
my_coro2.send(99)           # '-> Received: c = 99' 之后由于下面没有 yield 语句接收 99 了所以出现 StopIteration Error