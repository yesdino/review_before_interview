[toc]

---

[原文链接](https://blog.csdn.net/kan2016/article/details/82855158)

# 一、ORM 介绍
## 1.什么是 ORM
ORM 全拼 Object-Relation Mapping.

中文意为 **对象-关系映射**.
 
在 MVC/MVT 设计模式中的 Model 模块中都包括 ORM


## 2.ORM 优点
- （1）只需要面向对象编程, 不需要面向数据库编写代码.

对数据库的操作都转化成对类属性和方法的操作.
不用编写各种数据库的sql语句.
- （2）实现了数据模型与数据库的解耦, 屏蔽了不同数据库操作上的差异.

不在关注用的是mysql、oracle...等.
<u>通过简单的配置就可以轻松更换数据库，而不需要修改代码.</u>

## 3.ORM 缺点
相比较直接使用SQL语句操作数据库, <u>操作数据库过程中有性能损失</u>.
根据对象的操作转换成SQL语句,根据查询的结果转化成对象, <u>在映射过程中有性能损失</u>.

## 4.ORM 和数据库关系
在 Django 中 model 是你数据的单一、明确的信息来源。
它包含了你存储的数据的重要字段和行为。
通常，==**一个模型（model）映射到一个数据库 table 表。**==

基本情况：

每个模型(model)都是一个Python类，它是`django.db.models.Model`的子类。
模型的每个属性都代表一个数据库字段。
综上所述，Django为您提供了一个自动生成的数据库访问API。

![img](https://img-blog.csdn.net/20180926162113369?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2thbjIwMTY=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

---

# 二、ORM 用法
## 1.字段类型
**`属性名 = models.字段类型`**，定义属性时需要指定字段类型, 通过字段类型的参数指定选项

**字段属性名规则**
- 不允许使用 <u>python 的保留关键字</u>
- 不允许使用 <u>mysql 的保留关键字</u>
- 不允许使用<u>连续的下划线</u>，因为 Django 的查询- 语法就是连续的下划线

<br>

- **`AutoField`** ：自动增长的IntegerField, 不指定时Django会自动创建属性名为id的自动增长属性

- **`BooleanField`** ：布尔字段，值为True或False

- **`NullBooleanField`** ：支持 Null、True、False 三种值

- **`CharField`**`(max_length=20)` ：字符串参数 max_length 表示最大字符个数
- **`TextFiled`** ：大文本字段，一般超过4000个字符时使用

- **`IntegerField`** ：整数

- **`DecimalField`**`(max_digits=None, decimal_places=None)` ：可以指定精度的十进制浮点数。参数 max_digits 表示总位数
参数 decimal_places 表示小数位数
FloatField（） ：浮点数 

- **`DateField`**`[auto_now=False, auto_now_add=False])` ：
日期参数 auto_now 表示每次保存对象时，自动设置该字段为当前时间，用于"最后一次修改"的时间戳，它总是使用当前日期，默认为false。
参数 auto_now_add 表示当对象第一次被创建时自动设置当前时间，用于创建的时间戳，它总是使用当前日期，默认为 false。
参数 auto_now_add 和 auto_now 是**相互排斥**的，组合将会发生错误。
- **`TimeField`** ：参数和 DateField 一样

- **`DateTimeField`** ：日期时间，参数同 DateField

- **`FileField`** ：上传文件字段，以二进制的形式

- **`ImageField`** ：继承于FileField，对上传的内容进行校验，确保是有效的图片

## 2.字段选项
- **`null`** ：如果为True，表示==允许为**空**==，默认值是False

- **`blank`** ：如果为True，则该字段==允许为**空白**==，默认值是False    
对比 ：<u>`null` 是**数据库**范畴的概念，`blank` 是**表单**验证范畴的</u>
- **`db_column`** ：字段在数据库中的名称。
如果未指定，则使用属性的名称（只限于数据库表中的名字，操作数据库还是类属性的名字）

- **`db_index`** ：是否为此字段专门创建索引。
若值为True, 则在表中会为此字段创建索引，默认值是False（为了优化查询速度 ）

- **`default`** ：字段默认值，这可以是值或可调用对象。
如果可调用，则每次创建新对象时都会调用它。

- **`primary_key`** ：是否将此字段作为模型主键。
若为True，则该字段会成为模型的主键字段，默认值是False，一般作为 AutoField 的选项使用

- **`unique`** ：此字段是否只能是否唯一值不能重复。
如果为True, 这个字段在表中必须有唯一值，这个值不能重复，默认值是False

关系型字段类型：关联表中使用

<u>注意 ：Django会自动为表创建主键字段</u>

如果使用选项设置某属性为主键字段后，Django不会再创建自动增长的主键字段

默认创建的主键字段为 id，可以使用 pk 代替，pk 全拼为primary key
```py
class PeopleInfo(models.Model):
    name = models.CharField(max_length=20)        # 人物姓名
    gender = models.BooleanField(default=True)    # 人物性别
    description = models.CharField(max_length=20) # 人物描述
    isDelete = models.BooleanField(default=False) # 逻辑删除
    book = models.ForeignKey(BookInfo)            #【外键】约束，人物属于哪本书
    pub_date = models.DateField(null=True)        # 日期
    readcount = models.IntegerField(default=0)    # 阅读量
    commentcount = models.IntegerField(default=0) # 评论量
    isDelete = models.BooleanField(default=False) # 逻辑删除
 
    # 元类信息 : 修改表名
    class Meta:
        db_table = 'peopleinfo'
```

## 3.关系字段类型
关系型数据库的关系包括三种类型 ：
- **`ForeignKey`** ：一对多，将字段定义在多的一端中
- **`ManyToManyField`** ：多对多，将字段定义在任意一端中
- **`OneToOneField`** ：一对一，将字段定义在任意一端中
可以维护递归的关联关系，使用self指定


## 4.元选项 ：
作用 ：<u>修改数据库表的默认的名称</u>

==数据库表的默认名称为 : `应用名_模型名`==
```
例 ：APP Book 应用中定义 BookInfo class 模型类 
Book_bookinfo
```
在模型类中定义元类`Meta`，<u>用于设置元信息</u>，使用`db_table`自定义表的名字

```py
# 书籍信息模型
class BookInfo(models.Model):
    name = models.CharField(max_length=20) # 图书名称

    class Meta:     # 元信息类
        db_table = 'bookinfo' #自定义表的名字
```

## 5.模型成员

### objects : 管理器对象

- 是 Manager 类型的对象，定义在`from django.db import models`中

- 用于 model 模型对象<u>和数据库交互</u>
- 是默认自动生成的属性，但是可以自定义管理器对象
- 自定义管理器对象后，Django 不再生成默认管理器对象 objects

#### 自定义管理器对象

为模型类`UserInfo`自定义管理器对象`Users`

```py
# 用户信息模型
class UserInfo(models.Model):
    name = models.CharField(max_length=20) # 名称
    pub_date = models.DateField(null=True) # 日期
    readcount = models.IntegerField(default=0) # 阅读量
    commentcount = models.IntegerField(default=0) # 评论量
    isDelete = models.BooleanField(default=False) #【逻辑删除】

    #元类信息 : 修改表名
    class Meta:
        db_table = 'Userinfo'

    # 自定义管理器对象
    Users = models.Manager()
```
==自定义管理器对象后，查询数据时直接使用 Users 查询,不再用默认的 objects==

```py
# 书籍列表信息视图
def userList(request):
    # 查询数据库用户信息 : 默认管理器对象--objects
    # UserInfos = UserInfo.objects.all()

    # 查询数据库用户信息 : 自定义管理器对象--Users
    UserInfos = UserInfo.Users.all()

    # 构造上下文
    context = {'Userlist':UserInfos}

    return render(request, 'User/Userlist.html', context)
```


### Manager ：管理器类

- 定义在`from django.db import models`中

- 管理器是 Django 的模型进行数据库操作的接口，==Django应用的每个模型都拥有至少一个管理器==
- Django 模型支持自定义管理器类，继承自 `models.Manager`


#### 自定义管理器类

自定义管理器类主要用于两种情况
- 1.<u>修改原始查询集</u>，重写`get_queryset()`方法
    - 如，查询时，如果需要默认过滤掉某些数据，需要修改原始查询集
- 2.<u>新增管理器方法</u>，如创建模型对象方法
    - 如，当模型属性很多，多数字段为默认值，每次只需要给少数属性赋值时，可以新增模型初始化方法

##### 1.修改原始查询集

把 peopleinfo 表中的 isDelete 字段修改为 True(updata peopleinfo set isDelete=1 where id=4), 但是<u>逻辑删除字段为True 的那条记录依然会被查询出来</u>，这里的解决办法是自定义管理器类，重写 get_queryset() 方法

```py
from django.db import models

# 自定义管理器类
class PeopleInfoManager(models.Manager):
    # 自定义管理器类场景一：重写get_queryset()方法
    def get_queryset(self):
        # 调用父类的成员语法为：super(子类型, self).成员
        # 默认只查询逻辑删除字段为False的记录
        return super(PeopleInfoManager, self).get_queryset().filter(isDelete=False)
```

##### 2.新增管理器方法

新增管理器初始化模型对象方法：只有name属性需要赋值，其他的字段都是默认值

```py
# models.py -- 自定义管理器类
class UserInfoManager(models.Manager):
    # 1.修改原始查询集 重写get_queryset()方法
    def get_queryset(self):
        # 默认只查询逻辑删除字段为False的记录
        return super(UserInfoManager, self).get_queryset().filter(isDelete=False)

    # 2.新增管理器方法 初始化模型对象方法
    def create(self, name):
        user = UserInfo()
        user.name = name
        user.pub_date = '1989-11-11'
        user.readcount = 0
        user.commentcount = 0
        user.isDelete = False
        return user
```

```py
# view.py -- User列表信息视图
def UserList(request):
    # 初始化模型对象：自定义管理器类后
    UserInfos = [
        UserInfo.user.create('小明'),
        UserInfo.user.create('小杰'),
    ]
    # 构造上下文
    context = {'Userlist': UserInfos}
    return render(request, 'User/userlist.html', context)
```
 