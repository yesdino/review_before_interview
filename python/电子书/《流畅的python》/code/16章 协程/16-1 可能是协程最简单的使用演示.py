def simple_coroutine():     
    print('-> coroutine started')
    x = yield 
    print('-> coroutine received:', x)
    
    
my_coro = simple_coroutine()
ret = next(my_coro)       # -> coroutine started  首先要调用next(...) 函数，因为生成器还没启动
print(ret)
my_coro.send(42)