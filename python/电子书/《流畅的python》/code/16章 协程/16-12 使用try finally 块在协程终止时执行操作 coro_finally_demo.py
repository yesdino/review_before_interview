class DemoException(Exception):
    """为这次演示定义的异常类型。"""
    pass


def demo_finally():
    print('-> coroutine started')
    # 如果不管协程如何结束都想做些清理工作，要把协程定义体中相关的代码放入try/finally 块中
    try:
        while True:
            try:
                x = yield
            except DemoException:
                print('*** DemoException handled. Continuing...')
            else:
                print('-> coroutine received: {!r}'.format(x))
    finally:
        print('-> coroutine ending')