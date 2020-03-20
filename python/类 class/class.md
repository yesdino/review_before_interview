[toc]

---

# class

# 类定义
语法格式如下：
```py
class ClassName:
    <statement-1>
    ...
    <statement-N>
```


## 类属性与方法

### 属性
#### 操作属性
```python
getattr(obj, name[, default])   # 访问对象的属性。
hasattr(obj, name)              # 检查是否存在一个属性。
setattr(obj, name,value)        # 设置一个属性。如果属性不存在，会创建一个新属性。
delattr(obj, name)              # 删除属性。
```
#### 类的私有属性
`__private_attrs`：
- **==两个下划线开头==**，声明该属性为私有，不能在类的外部被使用或直接访问。
- 在类内部的方法中使用时 self.__private_attrs。

类的私有属性实例
```py
#!/usr/bin/python3
 
class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0    # 公开变量
 
    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print (self.__secretCount)
 
counter = JustCounter()
counter.count()
counter.count()
print (counter.publicCount)
print (counter.__secretCount)  # 报错，实例不能访问私有属性

# 输出：
# 1
# 2
# 2
# Traceback (most recent call last):
#   File "test.py", line 16, in <module>
#     print (counter.__secretCount)  # 报错，实例不能访问私有变量
# AttributeError: 'JustCounter' object has no attribute '__secretCount'
```

### 类的方法
在类的内部，
- 使用 def 关键字来定义一个方法
- 类方法必须包含参数 self，且为第一个参数
(self 的名字并不是规定死的，也可以使用 this，但是最好还是按照约定是用 self)
- self 代表的是类的实例

```py
#!/usr/bin/python3
 
#类定义
class people:
    name = ''                   # 定义基本属性
    age = 0
    __weight = 0                # 定义私有属性, 私有属性在类外部无法直接进行访问
    def __init__(self,n,a,w):   # 定义构造方法
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))
 
# 实例化类
p = people('runoob',10,30)
p.speak()

# 输出
# runoob 说: 我 10 岁。
```


#### 类的私有方法
`__private_method`：
- **==两个下划线开头==**，声明该方法为私有方法，
- 只能在类的内部调用 ，不能在类的外部调用。


类的私有方法实例：
```py
实例(Python 3.0+)
#!/usr/bin/python3
 
class Site:
    def __init__(self, name, url):
        self.name = name       # public
        self.__url = url       # private
 
    def who(self):
        print('name  : ', self.name)
        print('url : ', self.__url)
 
    def __foo(self):          # 私有方法
        print('这是私有方法')
 
    def foo(self):            # 公共方法
        print('这是公共方法')
        self.__foo()
 
x = Site('菜鸟教程', 'www.runoob.com')
x.who()        # 正常输出
x.foo()        # 正常输出
x.__foo()      # 报错
```


#### 类的内置方法
```py
__init__        : 构造函数，在生成对象时调用
__del__         : 析构函数，释放对象时使用
__repr__        : 打印，转换
__setitem__     : 按照索引赋值
__getitem__     : 按照索引获取值
__len__         : 获得长度
__cmp__         : 比较运算
__call__        : 函数调用
__add__         : 加运算
__sub__         : 减运算
__mul__         : 乘运算
__truediv__     : 除运算
__mod__         : 求余运算
__pow__         : 乘方
__new__                 | 生成实例所需属性 —— 创建实例时
__class__               | 实例所在的类 —— 实例.__class__
__name__                | 类名	                            
__str__                 | 实例字符串表示,可读性 —— print(类实例),如没实现，使用repr结果
__repr__                | 实例字符串表示,准确性 —— 类实例 回车 或者 print(repr(类实例))
__dict__                | 实例自定义属性 —— vars(实例.__dict__)
__doc__                 | 类的文档字符串,子类不继承 —— help(类或实例)
__module__              | 类定义所在的模块                    
__bases__               | 类的所有父类构成元素（包含了一个由所有父类组成的元组）                   
__getattribute__        | 属性访问拦截器 —— 访问实例属性时
__delattr__(s,name)     | 删除name属性 —— 调用时
__gt__(self,other)      | 判断self对象是否大于other对 —— 调用时
__setattr__(s,name,value)| 设置name属性 —— 调用时
__gt__(self,other)      | 判断self对象是否大于other对象 —— 调用时
__lt__(slef,other)      | 判断self对象是否小于other对象 —— 调用时
__ge__(slef,other)      | 判断self对象是否大于或者等于other对象 —— 调用时
__le__(slef,other)      | 判断self对象是否小于或者等于other对象 —— 调用时
__eq__(slef,other)      | 判断self对象是否等于other对象 —— 调用时
__call__(self,\*args)   | 把实例对象作为函数调用 —— 调用时
```


#### 运算符重载（重写内置方法）
Python同样支持运算符重载，我们可以对类的专有方法进行重载。

```py
#!/usr/bin/python3
 
class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b
 
   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)
   
   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)
 
v1 = Vector(2,10)
v2 = Vector(5,-2)
print (v1 + v2)

# 输出：
# Vector(7,8)
```

### 类对象

类对象支持两种操作：

#### 1. 属性引用
属性引用使用和 Python 中所有的属性引用一样的标准语法：`obj.name`。
==实际上，创建一个类之后，可以（**不用实例化**）通过类名访问其属性==。
#### 2. 实例化。
类实例化后，可以使用其属性和方法


类对象创建后，类命名空间中所有的命名都是有效属性名。所以如果类定义是这样:

```py
实例(Python 3.0+)
#!/usr/bin/python3
 
class MyClass:
    """一个简单的类实例"""
    i = 12345
    def f(self):
        return 'hello world'
 
# 实例化类
x = MyClass()
 
# 访问类的属性和方法
print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类的方法 f 输出为：", x.f())

# 以上创建了一个新的类实例并将该对象赋给局部变量 x，x 为空的对象。

# 输出：
# MyClass 类的属性 i 为： 12345
# MyClass 类的方法 f 输出为： hello world
```

- 类有一个名为 `__init__()` 的特殊方法（构造方法），该方法 **在类实例化时会自动调用** 

- 类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。
**==self==** 代表 **==类的实例==**，而非类

```py
class Test:
    def prt(self):
        print(self)
        print(self.__class__)
 
t = Test()
t.prt()

# 输出：
# <__main__.Test instance at 0x100771878>
# __main__.Test
```
从执行结果可以很明显的看出，self 代表的是类的实例，代表当前对象的地址，而 self.class 则指向类。


## --------------------------------

## 继承

### 普通继承
```py
class DerivedClassName(BaseClassName1):
    <statement-1>
    ...
    <statement-N>
```
#### 注意小括号中基类的顺序
若是基类中有相同的方法名，而在子类使用时未指定，<br>则 python **==从左至右搜索==** 即方法在子类中未找到时，从左到右查找基类中是否包含方法。

BaseClassName（示例中的基类名）必须与派生类定义在一个作用域内。
除了类，还可以用表达式，基类定义在另一个模块中时这一点非常有用:

```py
class DerivedClassName(modname.BaseClassName):
```

```py
#!/usr/bin/python3

# 父类 (基类)
class people:
    name = ''                   # 定义基本属性
    age = 0
    __weight = 0                # 定义私有属性,私有属性在类外部无法直接进行访问
    def __init__(self,n,a,w):   # 定义构造方法
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))
 
# 单继承示例
class student(people):
    grade = ''
    def __init__(self, n, a, w, g):
        people.__init__(self, n, a, w)  # 调用父类的构用函数
        self.grade = g
    
    def speak(self):    # 【覆写】父类的方法
        print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))
 
 
s = student('ken',10,60,3)
s.speak()

# 输出
# ken 说: 我 10 岁了，我在读 3 年级
```

### 多继承
```py
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    ...
    <statement-N>
```
#### 注意小括号中继承父类的顺序
若是父类中有相同的方法名，而在子类使用时未指定，<br>python从左至右搜索 即方法在子类中未找到时，**==从左到右查找==** 父类中是否包含方法。

```py
#!/usr/bin/python3
 
# 父类
class people:
    name = ''
    age = 0
    __weight = 0
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))
 
# 单继承示例
class student(people):
    grade = ''
    def __init__(self,n,a,w,g):
        people.__init__(self,n,a,w) # 调用父类的构函
        self.grade = g
    
    def speak(self):                # 覆写父类的方法
        print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))
 
#另一个类
class speaker():
    topic = ''
    name = ''
    def __init__(self,n,t):
        self.name = n
        self.topic = t
    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))
 
# 多重继承
class sample(speaker, student):
    a =''
    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)
 
test = sample("Tim",25,80,4,"Python")

# 方法名同，调用的是在括号中排【前地父类】的方法
test.speak()   

# 输出：
# 我叫 Tim，我是一个演说家，我演讲的主题是 Python
```

### 方法重写（覆写）
如果你的父类方法的功能不能满足你的需求，你可以在子类重写你父类的方法，

```py
#!/usr/bin/python3
 
class Parent:               # 父类
   def myMethod(self):
      print ('调用父类方法')
 
class Child(Parent):        # 子类
   def myMethod(self):
      print ('调用子类方法')
```

#### super() 函数
调用父类(超类)的一个方法。

```py
c = Child()                 # 子类实例

c.myMethod()                # 子类调用重写方法
super(Child,c).myMethod()   # ！用子类对象调用父类已被覆盖的方法

# 输出：
# 调用子类方法
# 调用父类方法
```

更多文档：

[Python 子类继承父类构造函数说明](http://www.runoob.com/w3cnote/python-extends-init.html)

---