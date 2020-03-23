# 目录

[toc]

---

[出处](https://www.liaoxuefeng.com/wiki/1016959663602400/1017502538658208)


在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数.

例如，可以把成绩随便改：

```python
s = Student()
s.score = 9999
```
这显然不合逻辑。
为了限制score的范围，可以通过一个`set_score()`方法来设置成绩，再通过一个`get_score()`来获取成绩，
这样，在`set_score()`方法里，就可以检查参数：

```python
class Student(object):

    def get_score(self):
         return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
```
现在，对任意的 Student 实例进行操作，就不能随心所欲地设置 score 了：

```python
s = Student()
s.set_score(60)     # ok!
s.get_score()       # 60
s.set_score(9999)   # ValueError: score must between 0 ~ 100!
```

但是，上面的调用方法又略显复杂，没有直接用属性这么直接简单。

## @property 的使用

有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？
对于追求完美的Python程序员来说，这是必须要做到的！

还记得装饰器（decorator）可以给函数动态加上功能吗？
对于类的方法，装饰器一样起作用。
Python内置的`@property`装饰器就是负责 <u>**把一个方法变成属性**</u> 调用的。

`@property` 的实现比较复杂，我们先考察如何使用。
把一个 `getter` 方法变成属性，只需要加上 `@property` 就可以了。
此时， <u>==**`@property` 本身又创建了另一个装饰器 `@score.setter`**== </u>，负责把一个 `setter` 方法变成属性赋值，
于是，我们就拥有一个可控的属性操作：

```python
class Student(object):

    @property           # 把 score 方法变成 score 属性给用户调用
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


s = Student()
s.score = 60        # OK，实际转化为 s.set_score(60)
print(s.score)      # OK，实际转化为 s.get_score()
s.score = 9999      # ValueError: score must between 0 ~ 100!
```
注意到这个神奇的 @property ，
我们在对实例属性操作的时候，就知道该属性很可能不是直接暴露的，而是通过 `getter` 和 `setter` 方法来实现的。 
还可以定义只读属性，**<u>只定义 `getter` 方法，不定义 `setter` 方法就是一个只读属性</u>**：
```python
class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth
```
`birth` 是可读写属性，而 `age` 就是一个只读属性，因为 `age` 可以根据 `birth` 和当前时间计算出来。

<br>


**小结**

`@property` 广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，
这样，程序运行时就减少了出错的可能性。




