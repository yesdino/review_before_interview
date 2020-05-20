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


# 四、Celery 执行异步任务

## 基本使用

创建项目 celerytest

- **①、创建 celery 任务** ：创建py文件 `celery_app_task.py`

```python
import celery
import time

# broker = 'redis://127.0.0.1:6379/2' 不加密码
backend = 'redis://:123456@127.0.0.1:6379/1'
broker  = 'redis://:123456@127.0.0.1:6379/2'
cel     = celery.Celery('test',backend=backend,broker=broker)

@cel.task
def add(x, y):
    return x+y
```


- **②、添加任务**： 创建py文件 `add_task.py`

```python
from celery_app_task import add

result = add.delay(4,5)
print(result.id)
```


- **③、执行任务**：

1） 创建py文件 `run.py`：

```python
from celery_app_task import cel

if __name__ == '__main__':
    cel.worker_main()
    # cel.worker_main(argv=['--loglevel=info')
```
2） 或者使用命令执行：`celery worker -A celery_app_task -l info`
注：windows下：`celery worker -A celery_app_task -l info -P eventlet`（eventlet 此模块需要另外安装）
<br>

- **④、查看任务执行结果**：创建py文件 `result.py`

```python
from celery.result import AsyncResult
from celery_app_task import cel

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

- **⑤、顺序执行上述文件**

执行 `add_task.py`，添加任务，并获取任务ID

执行 `run.py` ，或者执行命令：`celery worker -A celery_app_task -l info`

执行 `result.py`,检查任务状态并获取结果

<br>


## 多任务结构








<u></u>

<br>

```python

```