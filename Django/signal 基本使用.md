[toc]

---


Django中提供了“信号调度”，用于在框架执行操作时==解耦==。
通俗来讲，就是一些动作发生的时候，信号允许特定的发送者去提醒一些接受者。

## 理解 signal
### 原理
- 前置操作(触发操作) ：触发相应的事件
- 监听程序 ：执行对应的操作

### 好处
- ==**松耦合**== (不用把后续操作写在主逻辑中) 在触发事件注册中写
- ==**便于复用**== (这也是为什么 django 本身, 及第三方应用如 pinax 大量使用此技术的原因)

### 流程
1. 注册 signal
2. signal 关联 对应的listener
3. listener 等待事件 如有事件即触发后续动作 


## Django内置信号
==注意：以下触发动作一定是要走 django 系统，如果是别的服务器改了 DB 数据是不会触发的==
```py
Model signals               # (Model信号)
    pre_init                # django 的 modal 执行其构造方法前，自动触发
    post_init               # django 的 modal 执行其构造方法后，自动触发
    pre_save                # django 的 modal 对象保存前，自动触发
    post_save               # django 的 modal 对象保存后，自动触发
    pre_delete              # django 的 modal 对象删除前，自动触发
    post_delete             # django 的 modal 对象删除后，自动触发
    m2m_changed             # django 的 modal 中使用m2m字段操作第三张表(add,remove,clear) 前后，自动触发
    class_prepared          # 程序启动时，检测已注册的app中 modal 类，对于每一个类，自动触发

Management signals          # (管理信号)
    pre_migrate             # 执行 migrate 命令前，自动触发
    post_migrate            # 执行 migrate 命令后，自动触发

Request/response signals    # (请求返回信号)
    request_started         # 请求到来前，自动触发
    request_finished        # 请求结束后，自动触发
    got_request_exception   # 请求异常后，自动触发

Test signals                # (测试信号)
    setting_changed         # 使用 test 测试修改配置文件时，自动触发
    template_rendered       # 使用 test 测试渲染模板时，自动触发
 
Database Wrappers           # (数据库信号)
    connection_created      # 创建数据库连接时，自动触发
```
### 接收信号回调函数 receiver
```py
# 请注意，该函数采用 sender参数、通配符关键字参数(** kwargs);
# 所有信号处理程序必须采用这些参数。无论有无用上都必须写上这些参数
def my_callback(sender, **kwargs):
    print("Request finished!")
```

### 连接 receiver and signal
- 手动连接
```py
Signal.connect(receiver, sender=None, weak=True, dispatch_uid=None)
'''
receiver       : 接收到信号的回调函数
sender         : 指定从中接收信号的特定发送方。
weak           : Django 默认将信号处理程序存储为弱引用。因此，如果您的接收器是本地功能，它可能是垃圾收集。要防止这种情况，请在调用signal的connect()方法时传递weak = False。
dispatch_uid   : 在可能发送重复信号的情况下信号接收器的唯一标识符。
'''
```

- 使用 django.dispatch.receiver 装饰器：
  ```@receiver(signal)```    : 用于连接功能的信号或信号列表
  
```py
from django.core.signals import request_finished
from django.dispatch import receiver

@receiver(request_finished)
def my_callback(sender, **kwargs):
    print("Request finished!")
```

--------------------------------------------------------------------------
## 一、 应用示例：使用内置信号

### 1. 定义接收函数

在Django主目录下新建一个 sg.py

```py
from django.core.signals import request_finished
from django.core.signals import request_started
from django.core.signals import got_request_exception
 
from django.db.models.signals import class_prepared
from django.db.models.signals import pre_init, post_init
from django.db.models.signals import pre_save, post_save
from django.db.models.signals import pre_delete, post_delete
from django.db.models.signals import m2m_changed
from django.db.models.signals import pre_migrate, post_migrate
 
from django.test.signals import setting_changed
from django.test.signals import template_rendered
 
from django.db.backends.signals import connection_created

# ------------------------------------
# 定义接收函数
def signal_test(sender, **kwargs):
    print("test pre_init")      

# 注册接收器功能:
# 信号名称.connect(接收函数)
pre_init.connect(signal_test)   # pre_init :django 的 modal 执行其构造方法前，自动触发
```

### 2. 初始化
   
   然后在Django的相同目录的__init__.py 加入  import sg.py  跟注册mysql数据库一样，这样初始化Django程序的时候就能导入sg包

### 3. 调用

如果views.py这样写

```py
def sg(request):
    obj = models.Business(name='滴滴')
    print("obj1")
    obj.save()
 
    obj = models.Business(name='滴滴1') 
    obj.save()
 
    obj1 = models.Business(name='滴滴2')
    obj1.save()
    return HttpResponse('sg')
```
输出结果：每次在保存记录前都会先执行信号
```py
Quit the server with CTRL-BREAK.
test pre_init       # 执行接收函数
obj1
[02/Apr/2018 16:04:10] "GET /app1/sg/ HTTP/1.1" 200 2
test pre_init       # 执行接收函数
test pre_init       # 执行接收函数
```


<br>

<b>解析：为什么在obj.save()前可以触发pre_init这个信号呢？</b>
因为查看save的源码，里面留了这样一个钩子，致使可以找到这个 singal 然后触发 send，通过这个原理，我们就可以自定义信号
```py
if not neta.auto_creates:
    signal.pre_save.send(sender=origin, instance=self, raw=raw, using=using,
                        update_fields=update_fields)
```

## 二、 自定义信号


### 1. 定义

sg.py 这样写

```py

# 1. 定义信号
import django.dispatch
# providing_args: 激活时要给的参数,就算是'None'也可以
pizza_done = django.dispatch.Signal(providing_args=["toppings", "size"])

# 2. 注册信号 定义接收函数
def callback(sender, **kwargs):
    print("callback")
    print(sender,kwargs)

# 3. 连接
# 信号名称.connect(接收函数)
pizza_done.connect(callback)
```

### 2. 调用

- ##### 发送信号send、send_robust
send() 和 send_robust() 都返回 元组对 [(receiver，response),...] 的列表，
表示被叫接收函数列表及其响应值。

```py
from sg import pizza_done

# 发送信号, 模拟信号触发
pizza_done.send(sender='seven', toppings=123, size=456)

return HttpResponse('sg')
```
- 输出：
```py
[02/Apr/2018 17:43:55] "GET /app1/sg/ HTTP/1.1" 200 2
callback
seven {'signal': <django.dispatch.Signal object at 0x03391510>, 'toppings':123, 'size':456'}
```


---

## 特定senders
有些信号会多次发送，但您只对收到这些信号的**某个子集**感兴趣。
例如，考虑在保存 model 之前发送的```django.db.models.signals.pre_save```信号。
大多数情况下，您不需要知道何时保存什么 model  - 只需保存一个特定 model 。

在这些情况下，您可以注册接收仅由特定 sender 发送的信号。
对于```django.db.models.signals.pre_save```， ==sender 将是要保存的 model class==,
因此您可以指示您只需要某些 model 发送的信号：


```py
from django.db.models.signals import pre_save
from django.dispatch import receiver
from myapp.models import MyModel

# -----------------------------------
# MyModel: 数据库中的其中一张table
@receiver(pre_save, sender=MyModel)
def my_handler(sender, **kwargs):
    ...

# 只有在保存 MyModel 实例时才会调用 my_handler 函数。
```


---
## 防止重复signal
在某些情况下，将接收器连接到信号的代码可能会多次运行。这可能导致您的接收器功能被多次注册，因此对于单个信号事件被多次调用。
如果此行为存在问题（例如，在保存模型时使用信号发送电子邮件时），请将唯一标识符作为```dispatch_uid```参数传递以标识接收方函数。
此标识符通常是一个==string==，但任何 hashable 对象都可以。
最终结果是，对于每个唯一的```dispatch_uid```值，您的接收器函数将仅绑定一次信号：
```py
from django.core.signals import request_finished

request_finished.connect(my_callback, dispatch_uid="my_unique_identifier")
```


配置起作用的网址：

http://www.dongcoder.com/detail-969493.html












<br>
<br>

---
参考：
https://docs.djangoproject.com/zh-hans/2.0/topics/signals/
https://blog.csdn.net/qq_34964399/article/details/79790687