# Python 对象协议


[出处：91 个建议 63：熟悉 Python 对象协议]()


因为 Python 是一门动态语言，Duck Typing 的概念遍布其中，所以其中的 Concept 并不以类型的约束为载体，而另外使用称为协议的概念。

在 Python 中就是 <u>**我需要调用你某个方法，你正好就有这个方法**</u>。
比如：在字符串格式化中，如果有占位符 %s，那么按照字符串转换的协议，Python 会自动地调用相应对象的 `__str__()` 方法。

## 分类

### ①、类型转换协议

除了 `__str__()` 外，还有其他的方法，
比如 
- `__repr__()`、
- `__init__()`、
- `__long__()`、
- `__float__()`、
- `__nonzero__()` 等，统称类型转换协议。

除了类型转换协议之外，还要许多其他协议。

### ②、比较大小的协议

==这个协议依赖于 `__cmp__()`==，与 C 语言库函数 cmp 类似，
<u>当两者相等时，返回 0，当 `self < other` 时返回负值，反之返回正值。</u>

因为这种复杂性，所以 Python 又有 
- `__eq__()` 等于、
- `__ne__()` 不等于、
- `__lt__()` 小于、
- `__gt__()` 大于 
等方法来实现比较大小的判定。

这也就是 Python 对 `==`、`!=`、`<` 和 `>` 等操作符的进行重载的支撑机制。

### ③、数值类型相关的协议

这一类的函数比较多。基本上，只要实现了那么几个方法，基本上就能够模拟数值类型了。
不过还需要提到一个 Python 中特有的概念：**反运算（？？）**。
类似 `__radd__()` 的方法，所有的数值运算符和位运算符都是支持的，规则也是一律在前面加上前缀 r 即可。


### ④、容器(序列)类型协议

==下面方法需要配合 <u>**类中的某个可用索引访问的容器属性**</u> 使用==


容器的协议是非常浅显的，既然为容器，那么必然要有协议查询内含多少对象，
在 Python 中，要支持内置函数 `len()`，通过 `__len__()` 来完成。


- `__getitem__()` 读、<a href="#__getitem__">查看使用示例</a>

- `__setitem__()` 写、（使用示例与上面类似）

- `__delitem__()` 删除  
也很好理解。
<br>

- `__iter__()` 实现了迭代器协议，
- `__reversed__()` 则提供对内置函数 `reversed()` 的支持。

容器类型中最有特色的是对成员关系的判断符 in 和 not in 的支持，这个方法叫 

- `__contains__()`，只要支持这个函数就能够使用 in 和 not in 运算符了。

### ⑤、可调用对象协议

所谓可调用对象，即类似函数对象，
- `__call__()` ：<u>让类实例表现得像函数一样</u>，这样就可以让每一个函数调用都有所不同。

```python
class Functor(object):

    def __init__(self, context):
        self._context = context

    def __call__(self):
        print("do something with {}".format(self._context))

lai_functor = Functor("lai")
yong_functor = Functor("yong")
lai_functor()   # 调用对象，执行 __call__() 协议内定义动作
yong_functor()
```

### ⑥、可哈希对象协议

- `__hash__()` ：对象需要生成 hashCode 时调用协议内的定义

通过此方法来支持 `hash()` 这个内置函数的，这在创建自己的类型时非常有用，
因为<u>只有支持可哈希协议的类型才能作为 dict 的键类型</u>（不过只要继承自 object 的新式类就默认支持了）
<u></u>

### ⑦、属性操作协议和描述符协议

当操作类的属性时调用下列方法
- **`__getattr__()`**：
如果属性查找在实例以及对应的类中（通过`__dict__`)失败， 那么会调用到类的`__getattr__`函数。<a href="#__getattr__">查看使用示例</a>
<br>

- **`__setattr__()`**
对已存在的属性进行赋值。<a href="#__setattr__">查看使用示例</a>
<br>

- **`__delattr__()`**
删除属性方法应该很少用到，这里不多做了解


### ⑧、还有上下文管理器协议，也就是对 with 语句的支持**

这个协议通过 
- `__enter__()` 
- `__exit__()` 两个方法来实现对资源的清理，<u>确保资源无论在什么情况下都会正常清理。</u>

协议不像 C++、Java 等语言中的接口，它更像是声明，没有语言上的约束力。

---

## 使用示例


### `__getattr__()`
<a id="__getattr__"></a>

[出处](https://www.cnblogs.com/monogem/p/9765199.html)

**`__getattr__`函数的作用：**

如果属性查找（attribute lookup）在实例以及对应的类中（通过`__dict__`)失败， 那么会调用到类的`__getattr__`函数；

如果没有定义这个函数，那么抛出 **`AttributeError`** 异常。
由此可见，__getattr__一定是作用于属性查找的最后一步
- 例 1
```py
class A(object):
    def __init__(self, a, b):
        self.a1 = a
        self.b1 = b
        print('init')

    def mydefault(self, *args):
        print('args:' + str(args[0]))

    def __getattr__(self, attr_name):
        print("not exist func:", attr_name)
        return self.mydefault


a1 = A(10, 20)
a1.fn1(33)
a1.fn2('hello')     # 自己运行一遍吧
```
输出：
```
init
not exist func: fn1
args:33
not exist func: fn2
args:hello
```

- 例 2：经典示例。使用 `__getattr__()`虚拟 字典对象

```py
class ObjectDict(dict):
    def __init__(self, *args, **kwargs):
        super(ObjectDict, self).__init__(*args, **kwargs)

    def __getattr__(self, attr_name):
        value = self[attr_name]         # 
        if isinstance(value, dict):
            value = ObjectDict(value)
        return value


if __name__ == '__main__':
    od = ObjectDict(asf={'a': 1}, d=True)
    print(od.asf)       # {'a': 1}
    print(od.asf.a)     # 1
    print(od.d)         # True
```
<br>

### `__setattr__()`
<a id="__setattr__"></a>


[出处](https://www.cnblogs.com/huchong/p/8287799.html#_label2)


这个需要注意，==**会拦截所有属性的的赋值语句。**==
如果定义了这个方法，
`self.attr = value` 就会变成 `self.__setattr__("attr", value)`

**需要非常注意的是：**
当在`__setattr__`方法内对属性进行赋值时，不可使用 `self.attr = value` 
因为他会再次调用 `self.__setattr__("attr", value)`
则会形成 ==**无穷递归循环**==，最后导致**堆栈溢出异常**。

**正确做法：**
应该通过 **<u>对属性字典做索引运算来赋值</u>** 任何实例属性，也就是使用
```py
self.__dict__['name'] = value
```

如果类自定义了`__setattr__`方法，当通过实例获取属性尝试赋值时，就会调用`__setattr__`。
==常规的对实例属性赋值，被赋值的属性和值会存入 **实例属性字典__dict__** 中。==

#### 实例属性字典 **`__dict__`**
```py
class ClassA(object):

    def __init__(self, classname):
        self.classname = classname

insA = ClassA('ClassA')
print(insA.__dict__)    # {'classname': 'ClassA'}

insA.tag = 'insA'    
print(insA.__dict__)    # {'tag': 'insA', 'classname': 'ClassA'}
```
<br>

如果类自定义了`__setattr__`, 对实例属性的赋值就会调用它。

类定义中的`self.attr`也同样，所以在`__setattr__`下还有`self.attr`的赋值操作就会出现无线递归的调用`__setattr__`的情况。

<u>**自己实现`__setattr__`有很大风险，一般情况都还是继承object类的`__setattr__`方法。**</u>
<u></u>


```py
class ClassA(object):
    def __init__(self, classname):
        self.classname = classname  # 这里 调用__setattr__

    def __setattr__(self, name, value):
        # self.name = value         # 如果这里这样写会出现无限递归的情况
        print('call __setattr__')

insA = ClassA('ClassA') # call __setattr__
print(insA.__dict__)    # {}

insA.tag = 'insA'       # call __setattr__
print(insA.__dict__)    # {}
```
<br>

### `__getitem__()`
<a id="__getitem__"></a>

[出处](https://www.cnblogs.com/dengyg200891/p/4946096.html)

如果类把某个属性定义为序列，可以使用`__getitem__()`输出序列属性中的某个元素.
```py
class FruitShop():
     def __getitem__(self, i):
         return self.fruits[i]  # 遍历 FruitShop 实例时，遍历的是 self.fruits 序列

if __name__ == "__main__":
    shop = FruitShop()
    shop.fruits = ["apple", "banana"]
    print(shop[1])          # banana
    print("----")
    for item in shop:       # 遍历的是 self.fruits 序列
        print(item)
```
输出：
```
banana
----
apple
banana
```


<br>




