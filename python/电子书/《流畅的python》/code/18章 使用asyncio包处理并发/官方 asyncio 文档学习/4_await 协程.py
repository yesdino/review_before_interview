import asyncio

async def nested():
    return 42

async def main():       
    """
    async 协程中使用 await 调用两一个协程
    """
    # A coroutine object is created but not awaited,
    # so it *won't run at all*.
    # 一个协程对象被创建但未被 await, 是不会被运行的
    # nested()              # 如果你单纯调用 async 协程. 什么都不会打印
    
    ret = await nested()    # 而当我们 await 协程，将得到协程 return 值
    print(ret)              # will print "42".


# -------------------------------------
asyncio.run(main())