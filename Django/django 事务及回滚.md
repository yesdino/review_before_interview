[toc]

---



[source](https://www.cnblogs.com/thomson-fred/p/10198528.html)

# Django数据库--事务及事务回滚
数据库的读写操作中，**==事务==** 在保证数据的安全性和一致性方面起着关键的作用。
而 **==回滚==** 正是这里面的核心操作。

Django的ORM在事务方面也提供了不少的API。
- 有事务出错的整体回滚操作，
- 也有基于保存点的部分回滚。

本文将讨论Django中的这两种机制的运行原理。

# transaction

Django利用 **`django.db.transaction`** 模块中的API对数据库进行事务的管理

> Django provides a straightforward API in the django.db.transaction module to manage the autocommit state of each database connection.



 

## 主要函数：

这些函数使接受一个 **using** 参数表示所要操作的数据库。
如果未提供，则 Django 使用 "default" 数据库。

- 1、判断事务是否自动提交
```py
get_autocommit(using=None)   
```


- 2、设置自动提交事务
```py
set_autocommit(autocommit, using=None) 
```
 
- 3、事务提交后马上执行任务，
```py
set_autocommit(autocommit, using=None) 
```

例如：celery任务
```py
with transation.atomic:
    #do something and commit the transaction
    transaction.on_commit(lambda: some_celery_task.delay('arg1'))
```


## 怎么使用？在哪里使用？

事务是一系列的数据库操作，在数据的安全性和减少网络请求方面都有很大的优势。
关于数据库事务的文章有很多，我这里就不展开讨论了。

那么 ORM 中有哪些相关的 API 呢？ 

### Atomic 类
trasation 模块中最重要的是一个 **`Atomic`** 类， Atomic 是一个 **<u>上下文管理器</u>**。
可以使用 `@transaction.atomic` 或者 `with transaction.atomic` 的方式来调用。 

为了设置保存点，即 **断点** 进行事务的执行和回滚，可以嵌套使用 with transaction.atomic ，
例如官网的例子（伪代码）：

```py
with transaction.atomic():      # Outer atomic, start a new transaction
    transaction.on_commit(foo)  # 事务提交后马上执行 foo 函数

    try:
        with transaction.atomic():      # Inner atomic block, create a savepoint
            transaction.on_commit(bar)  # 事务提交后马上执行 bar 函数
            raise SomeError()           # Raising an exception - abort the savepoint
    except SomeError:
          pass
```
- <u>第一个 with transaction.atomic() 创建事务，</u>
- <u>第二个 with transaction.atomic() ==创建保存点==。</u>
虽然错误 raiseSomeError 是从‘内部’的保存点发出来的，但只会影响到‘外部’的保存点，
即 <u>只会回滚前面的数据库操作。</u>

<br>

下面还会讨论另一种创建保存点的方法。
<br>
 
在使用 transaction.atomic 前需要注意的问题： 

- 1、数据库的自动提交默认为开启，如果要将它关闭，必须很小心。
一旦使用了 transaction ，即关闭了自动提交。 
- 2、如果数据库之前的使用的是自动提交，那么在切换为非自动提交之前，必须确保当前没有活动的事务，通常可以手动执行 `commit()` 或者 `rollback()` 函数来把未提交的事务提交或者回滚。
 


# 一、整体回滚

所有的数据库更新操作都会在一个事务中执行。
如果事务中任何一个环节出现错误，都会回滚整个事务。

- 案例 1（伪代码）：
```py
from django.db import transaction

# open a transaction
@transaction.atomic                #装饰器格式
def func_views(request):
    do_something()    
    a = A()              # 实例化数据库模型
    try:
        a.save()
    except DatabaseError:
        pass
```

此方案整个 view 都会在事务之中，所有对数据库的操作都是原子性的。
<br>

 

- 案例 2（伪代码）：
```py
from django.db import transaction

def func_views(request):
    try:
        with transaction.atomic():      # 上下文格式，可以在 python 代码的任何位置使用
            a = A()
            a.save()
            # raise DatabaseError       # 测试用，检测是否能捕捉错误
    except DatabaseError:               # 自动回滚，不需要任何操作
            pass
```

此方案比较灵活，事务可以在代码中的任意地方开启，对于事务开启前的数据库操作是必定会执行的，事务开启后的数据库操作一旦出现错误就会回滚。

<br>
 
需要注意的是：

- 1、python 代码中 <u>对 Models 的修改</u> 和 <u>对数据库的修改</u> 的区别，
数据库层面的修改不会影响 Models 实例变量。

如果在代码中修改一个变量，例如：
```py
try:
    with transaction.atomic():     
        a = A()
        a.attribute = True   # A 表的某一个属性（即数据库的某一列）
        a.save()
        raise  DatabaseError    
except DatabaseError:   
        pass
```

```py
print(a.attribute)
# 输出结果：True
```
 
即使数据库回滚了，但是 a 实例的变量 `a.attribute` 还是会保存在 Models 实例中。
如果需要修改，就需要在 `except DatabaseError` 后面进行。

<br>

- 2、transaction 不需要在代码中手动 commit 和 rollback 的。
因为只有当一个 transaction 正常退出的时候，才会对数据库层面进行操作。
除非我们手动调用 transaction.commit 和 transaction.rollback


实际案例（此实例用伪代码2的格式）：

models.py
```py
# 数据表
class Author(models.Model):
    name = models.CharField(max_length=30,null=False)
    age = models.IntegerField()
    email = models.URLField(null=True)

class Count(models.Model):
    name = models.CharField(max_length=30)
    article_amount = models.IntegerField()
```


views.py
```py
from django.shortcuts import render
from django.http import HttpResponse
from index.models import Author, Count
from django.db import transaction,IntegrityError

def add_author_views(request):
    author_name = u'renyingying'
    author = Author(name=author_name, age=24, email='renyingying@qqq.com')
    # author.save()

    count = Count(name=author_name, article_amount=1)
    count.save()

    try:
        with transaction.atomic():
            author.save()
            raise DatabaseError # 报出错误，检测事务是否能捕捉错误
    except DatabaseError:       # 自动回滚，不需要任何操作
            pass
```

事务外的数据库操作正常执行，而事务内的数据库操作则会回滚。

author 表
![author](https://img2018.cnblogs.com/blog/1337214/201812/1337214-20181230105952042-1194027544.png)
 
count 表
![count](https://img2018.cnblogs.com/blog/1337214/201812/1337214-20181230110013554-1553755386.png)


将 raise DatabaseError 这一行代码注释掉，author 才会有数据
![1](https://img2018.cnblogs.com/blog/1337214/201812/1337214-20181230110048665-1492335063.png)


 

# 二、断点回滚（保存点Savepoint回滚）

保存点是事务中的标记，从原理实现上来说是一个 <u>类似存储结构的类</u> 。
可以回滚部分事务，而不是完整事务，同时会保存部分事务。

python 后端程序可以使用保存点。

一旦打开事务 atomic() ，就会构建一系列等待提交或回滚的数据库操作。
通常，如果发出回滚命令，则会回滚整个事务。
保存点则提供了执行细粒度回滚的功能，而不是将执行的完全回滚 transaction.rollback() 。 

## 工作原理
savepoint 通过对返回 sid 后面的将要执行的数据库操作进行计数，并保存在内置的列表中。
当对数据库数据库进行操作时遇到错误而中断，根据 sid 寻找之前的保存点并回滚数据，并将这个操作从列表中删除。

## 相关 API

1. 创建一个新的保存点。这表示处于正常状态的事务的一个点。返回保存点ID（sid）。
在一个事务中可以创建多个保存点。
```py
savepoint(using = None)
```

2. 发布保存点 sid，从创建保存点开始执行的数据库操作将成为可能回滚事务的一部分
```py
savepoint_commit(sid，using = None)
```

3. 将事务回滚到保存点 sid
```py
savepoint_rollback(sid，using = None)
```

4. 重置用于生成唯一保存点 ID 的计数器
```py
clean_savepoints(using = None)
```

值得注意的是：
这些函数中的每一个都接受一个 using 参数，该参数是数据库的名称。如果 using 未提供参数，则使用 "default" 默认数据库。

案例：（models.py 上文的案例一样）

views.py
```py
from django.db import transaction

# open a transaction
@transaction.atomic
def add_author_views(request):
    # 自动提交方式
    # Author.objects.create(name=u'wangbaoqiang',age=33,email='wangbaoqiang@qqq.com')

    author_name = u'linghuchong'
    author = Author(name=author_name,age=26,email='linghuchong@qqq.com')
    author.save()
    # transaction now contains author.save()

    sid = transaction.savepoint()

    try:
        count = Count(name=author_name, article_amount=1)
        count.save()
        # transaction now contains author.save() and count.save()
        transaction.savepoint_commit(sid)
        # open transaction still contains author.save() and count.save()
    except IntegrityError:
        transaction.savepoint_rollback(sid)
        # open transaction now contains only count.save()
        # 保存author操作回滚后，事务只剩下一个操作 

   transaction.clean_savepoints()  # 清除保存点
```

注意：
希望当遇到错误得到回滚的事务一定要放在 try 里面。
（如果放在 try 外面，虽然不会报错，但是是不会执行的）

如上面的例子，如果在给 Count 表执行插入数据发生错误，就会 断点 ’ 回滚到 Count 表插入数据前， Author 表插入的数据不变。

 

结果显示：


author 表
![author2](https://img2018.cnblogs.com/blog/1337214/201812/1337214-20181230013422941-245972208.png)
 
count 表
![count2](https://img2018.cnblogs.com/blog/1337214/201812/1337214-20181230013441529-712124630.png)



