# 目录

[toc]

---

[出处](https://www.cnblogs.com/angelyan/p/10531635.html)

# 一、什么是 Celery

- 一个简单、灵活且可靠的，处理大量消息的 ==分布式 **<u>系统</u>**==
- 专注于 <u>**实时**</u> 处理的 异步任务队列
- 同时也支持 <u>任务调度</u>


## Celery 架构

<img style="width:400px" src="https://img2018.cnblogs.com/blog/1449147/201903/1449147-20190314171017451-2049862911.png"></img>


Celery的架构由三部分组成：
- 1、**消息中间件** (message broker)
- 2、**任务执行单元** (worker)
- 3、**任务执行结果存储** (task result store)



### 消息中间件
Celery 本身不提供消息服务，但是可以方便的和第三方提供的消息中间件集成。
包括: **`RabbitMQ`**, **`Redis`** 等等


### 任务执行单元 & 任务执行结果存储
Task result store 用来存储 Worker 执行的任务的结果。
Celery 支持以 不同方式 **存储任务的结果**。包括: **`AMQP`**, **`redis`** 等

<br>

## 版本支持情况

python 3.6版本支持celery 4.2.1

```python
Celery version 4.0 runs on
        Python ❨2.7, 3.4, 3.5❩
        PyPy ❨5.4, 5.5❩
    This is the last version to support Python 2.7, and from the next version (Celery 5.x) Python 3.5 or newer is required.

    If you’re running an older version of Python, you need to be running an older version of Celery:

        Python 2.6: Celery series 3.1 or earlier.
        Python 2.5: Celery series 3.0 or earlier.
        Python 2.4 was Celery series 2.2 or earlier.

    Celery is a project with minimal funding, so we don’t support Microsoft Windows. Please don’t open any issues related to that platform.
```
<br>


# 二、Celery 使用场景

## 异步任务

将 **<u>耗时</u>** 操作任务提交给Celery去异步执行，比如发送短信/邮件、消息推送、音视频处理等等

## 定时任务

定时执行某件事情，比如每天数据统


<br>

# 三、Celery 安装配置

```python
pip install celery
```

消息中间件： **`RabbitMQ`** 或 **`Redis`**

<br>

定义 Celery ：
```python
app=Celery('任务名'，backend='xxx',broker='xxx')
```

<br>


# 四、Celery 执行**异步任务**

## **基本使用（单任务）**

创建项目 celerytest


### 1、创建 celery，装饰任务
创建 `celery_app_task.py`：

```python
import celery
import time

# broker = 'redis://127.0.0.1:6379/2' 不加密码
backend = 'redis://:123456@127.0.0.1:6379/1'
broker  = 'redis://:123456@127.0.0.1:6379/2'

# 创建 APP
cel = celery.Celery('test',backend=backend,broker=broker)

@cel.task
def add_task(x, y):
    return x+y
```

### 2、添加装饰后的任务到 celery
创建文件 `add_task.py`：

```python
from celery_app_task import add_task

result = add_task.delay(4,5)     # 括号内传递 add_task() 参数
print(result.id)
```
注意打印出来的 ID 号需要传递给 `result.py`

### 3、celery 执行任务

1） 创建文件 `run.py`：

```python
from celery_app_task import cel

if __name__ == '__main__':
    cel.worker_main()
    # cel.worker_main(argv=['--loglevel=info')
```
2） 或者使用命令执行：`celery worker -A celery_app_task -l info`
注：windows下：`celery worker -A celery_app_task -l info -P eventlet`（eventlet 此模块需要另外安装）
<br>

### 4、查看任务执行结果
创建文件 `result.py`：

```python
from celery.result import AsyncResult
from celery_app_task import cel

# id 号为上面 result.id 的返回值
async = AsyncResult(id="e919d97d-2938-4d0f-9265-fd8237dc2aa3", app=cel)

if async.successful():
    result = async.get()
    print(result)
    # result.forget() # 将结果删除
elif async.failed():
    print('执行失败')
elif async.status == 'PENDING':
    print('任务等待中被执行')
elif async.status == 'RETRY':
    print('任务异常后正在重试')
elif async.status == 'STARTED':
    print('任务已经开始被执行')
```


<br>


## **多任务**

结构
```python
pro_cel
    ├── celery_task# celery相关文件夹
    │   ├── celery.py   # celery连接和配置相关文件,必须叫这个名字
    │   ├── tasks1.py   # 所有任务函数
    │   └── tasks2.py   # 所有任务函数
    ├── check_result.py # 检查结果
    └── send_task.py    # 触发任务
```

### 1、定义 celery，装饰任务

- **celery.py**

celery连接和配置相关文件,必须叫这个名字 

```python
from celery import Celery

cel_name = 'celery_demo'
broker  = 'redis://127.0.0.1:6379/1'
backend = 'redis://127.0.0.1:6379/2'

# task_lis 包含以下两个任务文件，去相应的 py 文件中找任务，对多个任务做分类
task_lis = [
    'celery_task.tasks1',
    'celery_task.tasks2'
]

# 定义 Celery
cel = Celery(cel_name, broker=broker, backend=backend, include=task_lis)  
cel.conf.timezone = 'Asia/Shanghai' # 时区
cel.conf.enable_utc = False         # 是否使用 UTC
```

- **tasks1.py**
```python
import time
from celery_task.celery import cel

@cel.task
def task1(res):
    time.sleep(5)
    return "task1任务结果: %s"%res
```

- **tasks2.py**
```python
import time
from celery_task.celery import cel

@cel.task
def task2(res):
    time.sleep(5)
    return "task2任务结果: %s"%res
```

### 2、在 celery 添加 将要执行的任务
- **send_task.py**
```python
from celery_task.tasks1 import task1
from celery_task.tasks2 import task2

# 用 delay() 告知 celery 去执行 task1 任务，并传入一个参数
result = task1.delay('第一个的执行')
print(result.id)                    # 此任务的 ID 号

result = task2.delay('第二个的执行')
print(result.id)
```


### 3、开启 work 执行任务：
linux: `celery worker -A celery_task -l info`
win  : `celery worker -A celery_task -l info -P eventlet`


### 4、检查任务执行结果
- **check_result.py** 
```python
import sys
from celery.result import AsyncResult
from celery_task.celery import cel

id = sys.argv[1]    # 任务 ID 号执行时传入
async = AsyncResult(id=id, app=cel)

if async.successful():
    result = async.get()
    print(result)
    # result.forget() # 将结果删除,执行完成，结果不会自动删除
    # async.revoke(terminate=True)  # 无论现在是什么时候，都要终止
    # async.revoke(terminate=False) # 如果任务还没有开始执行呢，那么就可以终止。
elif async.failed():
    print('执行失败')
elif async.status == 'PENDING':
    print('任务等待中被执行')
elif async.status == 'RETRY':
    print('任务异常后正在重试')
elif async.status == 'STARTED':
    print('任务已经开始被执行')
```


<br>

# 五、Celery执行**定时任务**

## 方式 ①
add_task.py：使用 `apply_async` 在 celery 添加 将要执行的任务并设定时间
```python
from celery_app_task import add
from datetime import datetime
from datetime import timedelta

# 方式一
# v1 = datetime(2019, 2, 13, 18, 19, 56)
# print(v1)
# v2 = datetime.utcfromtimestamp(v1.timestamp())将当前时间转成utc格式
# print(v2)
# result = add_task.apply_async(args=[1, 3], eta=v2)
# print(result.id)

# 方式二
ctime = datetime.now()
utc_ctime = datetime.utcfromtimestamp(ctime.timestamp()) # 默认用 utc 时间,需要转成 utc 时间格式
time_delay = timedelta(seconds=10)
task_time = utc_ctime + time_delay  # 设定的时间

# 使用 apply_async 并设定时间
result = add_task.apply_async(args=[4, 3], eta=task_time)
print(result.id)
```
启动 work 执行：`celery worker -A celery_app_task -l info`


## 方式 ②

多任务结构中 celery.py 修改如下
```python
from datetime import timedelta
from celery import Celery
from celery.schedules import crontab

cel_neme = 'tasks'
broker  = 'redis://127.0.0.1:6379/1'
backend = 'redis://127.0.0.1:6379/2'
# task_lis 包含以下两个任务文件，去相应的 py 文件中找任务，对多个任务做分类
task_lis = [
    'celery_task.tasks1',
    'celery_task.tasks2'
]

cel = Celery(cel_neme, broker=broker, backend=backend, include=task_lis) # Celery 实例
cel.conf.timezone = 'Asia/Shanghai'
cel.conf.enable_utc = False
cel.conf.beat_schedule = {
    # 1. 间隔时间执行
    'add-every-10-seconds': {                       # 名字随意命名
        'task': 'celery_task.tasks1.test_celery',   # 执行 tasks1 下的 test_celery 函数
        # 'schedule': 1.0,
        # 'schedule': crontab(minute="*/1"),
        'schedule': timedelta(seconds=2),           # 每隔2秒执行一次
        'args': ('test',)                           # 任务传递的参数
    },
    # 2. 特定时间执行
    # 'add-every-12-seconds': {
    #     'task': 'celery_task.tasks1.test_celery',
    #     每年4月11号，8点42分执行
    #     'schedule': crontab(minute=42, hour=8, day_of_month=11, month_of_year=4),
    #     'schedule': crontab(minute=42, hour=8, day_of_month=11, month_of_year=4),
    #     'args': (16, 16)
    # },
}
```
启动一个 beat：`celery beat -A celery_task -l info` （注意：同一个目录下只能开启一个 beat ）






<u></u>

<br>

```python

```