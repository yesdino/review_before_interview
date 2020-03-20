## 3 @staticmethod和@classmethod

Python其实有3个方法,即
**静态方法** (staticmethod),
**类方法** (classmethod)和
**实例方法**。

如下:

```python
def foo(x):
    print "executing foo(%s)"%(x)

class A(object):
    def foo(self,x):    # 实例方法 self传递实例
        print "executing foo(%s,%s)"%(self,x)

    @classmethod        # 类方法 cls传递类
    def class_foo(cls, x):
        print "executing class_foo(%s,%s)"%(cls, x)

    @staticmethod       # 静态方法 不用实例化可以用类名调用
    def static_foo(x):
        print "executing static_foo(%s)"%x

a = A()
```
这里先理解下函数参数里面的 self 和 cls. 这个 self 和 cls 是对类或者实例的绑定 , 

对于一般的函数来说我们可以这么调用 `foo(x)`, 这个函数就是最常用的 , 它的工作跟任何东西 ( 类 , 实例) 无关。

### 实例方法
对于实例方法 , 我们知道在类里每次定义方法的时候都需要绑定这个实例 self, 就是 `foo(self, x)`, 为什么要这么做呢 ? 
**因为实例方法的调用离不开实例** , 我们需要把实例自己传给函数 , 调用的时候
    ```py
    a.foo(x)    # 其实是 foo(a, x)
    ```

### 类方法
类方法一样 , 只不过它 **传递的是类** 而不是实例 , `A.class_ foo(x)`. 注意这里的 self 和 cls 可以替换别的参数 , 但是 python 的约定是这俩, 还是不要改的好 .

### 静态方法
静态方法其实和普通的方法一样,不需要对谁进行绑定,
唯一的区别是调用的时候可以使用`a.static_foo(x)`或者`A.static_foo(x)`来调用. 
即，**不用实例化也可以直接用类名调用**

| 实例化：<br> `a = A()`      | 实例方法     | 类方法            | 静态方法            |
| :------ | :------- | :------------- | :-------------- |
|实例`a` | `a.foo(x)` | `a.class_foo(x)` | `a.static_foo(x)` |
|类 `A`       | 不可用      | `A.class_foo(x)` | `A.static_foo(x)` |

更多关于这个问题:
1. http://stackoverflow.com/questions/136097/what-is-the-difference-between-staticmethod-and-classmethod-in-python
2. https://realpython.com/blog/python/instance-class-and-static-methods-demystified/