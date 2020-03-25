""" 示例16-8　coro_exc_demo.py：学习在协程中处理异常的测试代码 """

class DemoException(Exception):
    """为这次演示定义的异常类型。"""
    pass


def demo_exc_handling():
    print('-> coroutine started')
    while True:
        try:
            x = yield
        except DemoException:                           # 1 特别处理 DemoException 异常。
            print('*** DemoException handled. Continuing...')
        else:                                           # 2 如果没有异常，那么显示接收到的值。
            print('-> coroutine received: {!r}'.format(x))
    raise RuntimeError('This line should never run.')   # 3 这一行永远不会执行。因为只有未处理的异常才会中止那个无限循环，而一旦出现未处理的异常，协程会立即终止。


if __name__ == "__main__":
    exc_coro = demo_exc_handling()
    ret = next(exc_coro)
    print(ret)

    ret = exc_coro.send(11)
    print(ret)

    exc_coro.throw(DemoException)

    from inspect import getgeneratorstate   # 查看此时协程状态
    print(getgeneratorstate(exc_coro))      # GEN_SUSPENDED
    