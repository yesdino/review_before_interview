[toc]

---

# python 2。3 差异

## python3 新增特性

| 差异 <a id="dif_top"><a> |python3 | python2
| :--- |:---|:---
| print | 成为一个函数 print() | print 只是一个关键字
| <a href="#1">编码问题</a>  | 3 中不再有 Unicode 对象，str 默认就是 unicode | 
|<a href="#2">除法</a>   |  单斜杠`/`能整除得到小数，双斜杠`//`能整除得到整数  | 只能得到整数的商
| <a href="#3">类型注解</a>  | 可以给变量加类型提示（zhuyi注意只是提示,要进行类型检查需要借助 IDE 工具  |
| <a href="#4">优化 `super()`函数</a>  |   |
|  <a href="#5">解包操作</a> |   |
|  关键字参数 （这个我会了，不写了 |   |
| <a href="#6">Chained exceptions. Python3 重新抛出异常信息不会丢失栈信息</a>  |   |
| <a href="#7">一切返回迭代器<br> `range, zip, map, dict.values ...` </a>  |   |

## python3 新增内置库
| 差异 <a id="ku_top"><a> |python3 | python2
| :--- |:---|:---
| yield from 链接子生成器  |   |
|  asyncio 内置库， asyic/await 原生协程支持异步编程 |   |
| 新内置库 `enum, mock, asyncio, ipaddess, concurrent.futrues 等`  |   |
|   |   |


- **<a href="#dif_top">编码问题 <a id="1"><a>**



```py
# python3:
s = '中文'       # 不用加 u 前缀
print(typr(s))  # str， str默认就是unicode

def 大写(s):return s.upper()    # 甚至可以用中文作为函数名
print(大写('abc'))

# -----------------------------
# python2:
s = u'中文'     # 要加 u 前缀
print(typr(s))  # unicode
```


- **<a href="#dif_top">除法 <a id="2"><a>**

```py
# python3:
5/2     # 2.5
5//2    # 2

# python2:
5/2     # 2
```



- **<a href="#dif_top">类型注解 <a id="3"><a>**
```py
# python3:
# 参数 name 是 str 类型，返回一个 str 类型
def hello(name: str) -> str:
    return 'hello'+name
```




- **<a href="#dif_top">优化 `super()`函数 <a id="4"><a>**

```py
# 父类：
class Base(object):
    def hello(self):
        print('hello')

# python3:
Class C1(Base):
    def hello(self):
        return super().hello()  # 引用父类

# python2:
Class C2(Base):
    def hello(self):
        return super(C, self).hello()  # 引用父类
```



- **<a href="#dif_top">解包操作 <a id="5"><a>**

```py
# python3:
a, b, *c = range(10)
print(a)    # 0
print(b)    # 1
print(c)    # [2, 3, 4, 5, 6, 7, 8, 9]

a, b, *_ = range(5)    # 提取序列中前面两个元素，其他的舍弃

```


- **<a href="#dif_top">Chained exceptions. Python3 重新抛出异常信息不会丢失栈信息 <a id="6"><a>**


```py
# python3:


# python2:

```


- **<a href="#dif_top">一切返回迭代器 `range, zip, map, dict.values ...` <a id="7"><a>**

```py
# python3:
range(10)   # 输出: range(0, 10) 迭代器，懒加载, 即不一次性全部加载出来，你要哪一个才给你哪一个，优化性能

# python2:
range(10)   # 生成: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 列表，占内存
```
