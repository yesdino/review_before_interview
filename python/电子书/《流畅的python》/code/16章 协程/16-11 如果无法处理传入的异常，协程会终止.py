from coro_exc_demo import demo_exc_handling


if __name__ == "__main__":
    exc_coro = demo_exc_handling()
    ret = next(exc_coro)
    print(ret)

    ret = exc_coro.send(11)
    print(ret)

    exc_coro.throw(ZeroDivisionError)