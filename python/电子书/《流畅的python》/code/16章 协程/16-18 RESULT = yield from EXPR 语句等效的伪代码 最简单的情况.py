"""
简化的伪代码，等效于委派生成器中的 RESULT = yield from EXPR 语句
（这里针对的是最简单的情况：不支持.throw(...) 和.close() 方法，而且只处理StopIteration 异常）

_i（迭代器）    ：子生成器
_y（产出的值）  ：子生成器产出的值
_r（结果）      ：最终的结果（即子生成器运行结束后yield from 表达式的值）
_s（发送的值）  ：调用方发给委派生成器的值，这个值会转发给子生成器
_e（异常）      ：异常对象（在这段简化的伪代码中始终是StopIteration 实例）
"""

_i = iter(EXPR)                     # ➊ EXPR 可以是任何可迭代的对象，因为获取迭代器_i（这是子生成器）使用的是 iter() 函数。
try:
    _y = next(_i)                   # ➋ 预激子生成器；结果保存在_y 中，作为产出的第一个值。
except StopIteration as _e:
    _r = _e.value                   # ➌ 如果抛出StopIteration 异常，获取异常对象的value 属性，赋值给_r——这是最简单情况下的返回值（RESULT）。
else:
    while 1:                        # ➍ 运行这个循环时，委派生成器会阻塞，只作为调用方和子生成器之间的通道。
        _s = yield _y               # ➎ 产出子生成器当前产出的元素；等待调用方发送_s 中保存的值。注意，这个代码清单中只有这一个yield 表达式。
        try:
            _y = _i.send(_s)        # ➏ 尝试让子生成器向前执行，转发调用方发送的_s。
        except StopIteration as _e: # ➐ 如果子生成器抛出StopIteration 异常，获取value 属性的值，赋值给_r，然后退出循环，让委派生成器恢复运行。
            _r = _e.value
            break
RESULT = _r                         # ➑ 返回的结果（RESULT）是_r，即整个yield from 表达式的值。