[参照]("http://www.runoob.com/python/python-object.html" "Python 面向对象")


可能需要看一下的：[Python 内置函数]("http://www.runoob.com/python/python-built-in-functions.html" "Python 内置函数")
# ①声明 定义
#### self
* self 代表类的实例，<u>self 在定义类的<b>方法 def </b>时是必须有的</u>，虽然在调用时不必传入相应的参数
* self 不是 python 关键字，我们把他换成其他命名也是可以正常执行的，即<b><u>系统会识别第一个参数为自身类的示例，指向自身</u></b>
```python
class Test:
    def prt(self):
        print(self)
        print(self.__class__)
 
t = Test()  # 通过直接用类名来实例化
t.prt()

# 输出
# <__main__.Test instance at 0x10d066878>
# __main__.Test
```


---
#### 内置属性 ，即在实例化这个类的同时，这个类就天生自带的属性
```python
>>> class Peopre(object):
...     pass
... 
>>> dir(Peopre)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
```

<!-- 表格使用
| 左对齐标题 | 右对齐标题 | 居中对齐标题 |
| :------| ------: | :------: |
| 内容 | 内容 | 内容 | 
-->

---
|常用内置属性(不全的)	        |说明 —— 触发方式|
| :------                     | :------                              
|```__init__```	            | 构造初始化函数 —— 创建实例后，赋值时使用,在```__new__```后
|```__new__```	               | 生成实例所需属性 —— 创建实例时
|```__class__```	            | 实例所在的类 —— 实例.```__class__```
|```__name__```	            | 类名	                            
|```__str__```	               | 实例字符串表示,可读性 —— print(类实例),如没实现，使用repr结果
|```__repr__```	            | 实例字符串表示,准确性 —— 类实例 回车 或者 print(repr(类实例))
|```__del__```	               | 析构(删除示例对象) —— del删除实例时
|```__dict__```	            | 实例自定义属性 —— ```vars(实例.__dict__)```
|```__doc__```	               | 类的文档字符串,子类不继承 —— help(类或实例)
|```__module__```	            | 类定义所在的模块                    
|```__bases__ ```	            | 类的所有父类构成元素（包含了一个由所有父类组成的元组）                   
|```__getattribute__```	      | 属性访问拦截器 —— 访问实例属性时
|```__delattr__(s,name)```    | 删除name属性 —— 调用时
|```__gt__(self,other)```	   | 判断self对象是否大于other对 —— 调用时
|```__setattr__(s,name,value)```|	设置name属性 —— 调用时
|```__gt__(self,other)```	   | 判断self对象是否大于other对象 —— 调用时
|```__lt__(slef,other)```	   | 判断self对象是否小于other对象 —— 调用时
|```__ge__(slef,other)```	   | 判断self对象是否大于或者等于other对象 —— 调用时
|```__le__(slef,other)```	   | 判断self对象是否小于或者等于other对象 —— 调用时
|```__eq__(slef,other)```	   | 判断self对象是否等于other对象 —— 调用时
|```__call__(self,\*args)```  | 把实例对象作为函数调用 —— 调用时



---
# ② 实例化
* #### ==在 Python 中并没有这个 new 关键字创建实例对象，使用类的名称直接实例化==，
* #### 通过 ```__init__()``` 方法接收参数，当创建了这个类的实例时就会调用该方法，其被称为类的构造函数或初始化方法
* #### 只要不是私有属性和方法，都可以在外部去改变，即增加属性，删除属性等
```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
class Employee:
   empCount = 0     # 所有员工的基类
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary
    
emp1 = Employee("Zara", 2000)       # 创建 Employee 类的第一个对象

# 外部改变属性
emp1.age = 7  # 添加一个 'age' 属性
emp1.age = 8  # 修改 'age' 属性
del emp1.age  # 删除 'age' 属性
```

### 操作属性
```python
getattr(obj, name[, default])   : 访问对象的属性。
hasattr(obj, name)              : 检查是否存在一个属性。
setattr(obj, name,value)        : 设置一个属性。如果属性不存在，会创建一个新属性。
delattr(obj, name)              : 删除属性。
```