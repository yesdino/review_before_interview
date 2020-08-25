
**`is`** : 是否指向同一地址空间 `id()` 可以看变量的地址空间
**`==`** : 数值是否相等

结果：
==**只有【数值】和【字符串】的情况下，a is b 才为 True，
当a和b是 tuple，list，dict 或 set 型时，a is b为 False**==

```py
a = 1           # a和b为数值类型
b = 1
print(a is b)   # True
print(id(a))    # 14318944
print(id(b))    # 14318944


# -----------------------------------------
a = 'cheesezh'  # a和b为字符串类型
b = 'cheesezh'
print(a is b)   # True
print(id(a))    # 42111872
print(id(b))    # 42111872

# -----------------------------------------
a = (1,2,3)     #a和b为 元组 类型
b = (1,2,3)     
print(a is b)   # False
print(id(a))    # 15001280
print(id(b))    # 14790408

# -----------------------------------------
a = [1,2,3]     # a和b为 list 类型
b = [1,2,3]
print(a is b)   # False
print(id(a))    # 42091624
print(id(b))    # 42082016

# -----------------------------------------
a = {'cheese':1, 'zh':2}  # a和b为 dict 类型
b = {'cheese':1, 'zh':2}
print(a is b)   # False
print(id(a))    # 42101616
print(id(b))    # 42098736

# -----------------------------------------
a = set([1,2,3])# a和b为 set 类型
b = set([1,2,3])
print(a is b)   # False
print(id(a))    # 14819976
print(id(b))    # 14822256
```