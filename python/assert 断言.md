assert 表断言

后面跟的表达式一定要为真 否则 raise 引发异常

> 在没完善一个程序之前，我们不知道程序在哪里会出错，与其让它在运行最崩溃，不如在出现错误条件时就崩溃

可以自定义异常提示
```py
assert len(lists) >=5, '列表元素个数小于5'
assert 2==1, '2不等于1'
```