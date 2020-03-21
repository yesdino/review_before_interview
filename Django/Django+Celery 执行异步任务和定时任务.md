
[toc]

---


[source](https://mp.weixin.qq.com/s/yQlFs-6Fc237Qot3-64Qlg)

<!-- # 如何使用Django+Celery执行异步任务和定时任务 -->
Python Web与Django开发  前天
文章转载自公众号  运维咖啡吧 [运维咖啡吧](https://mp.weixin.qq.com/s/yQlFs-6Fc237Qot3-64Qlg##) ， 作者 37丫37

原生 Celery ，非 djcelery 模块，所有演示均基于 Django2.0 

celery 是一个基于 python 开发的简单、灵活且可靠的分布式任务队列框架，支持使用任务队列的方式在分布式的机器 / 进程 / 线程上执行任务调度。采用典型的生产者 - 消费者模型，主要由三部分组成： 

- 消息队列 **broker** ： 
broker 实际上就是一个 MQ 队列服务，可以使用 Redis、RabbitMQ 等作为 broker
- 处理任务的消费者 **workers** ： 
broker 通知 worker 队列中有任务， worker 去队列中取出任务执行，每一个 worker 就是一个进程
- 存储结果的 **backend** ：
执行结果存储在 backend ，默认也会存储在 broker 使用的 MQ 队列服务中，也可以单独配置用何种服务做 backend

![img](https://mmbiz.qpic.cn/mmbiz_png/s0ib4cHvBPB8bhibBIQG2RN8jvYSD8sLF2q8aVsQ0exzamCBfoj23TmKSibG1kPuDHwy0QDphCS07ko0RZPMPx3cw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)


## 一、异步任务 (要花费很久的任务)


我的异步使用场景为项目上线：
前端 web 上有个上线按钮，点击按钮后**发请**求给后端，后端执行上线过程要5分钟，后端在接收到请求后把任务放入队列异 ==步执== 行，同时马上返回给前端一个任务执行中的结果。
若果没有异步执行会怎么样呢？
同步的情况就是执行过程中前端一直在等后端返回结果，页面转呀转的就转超时了。


### 异步任务配置

- 1、安装 RabbitMQ ，
这里我们使用 RabbitMQ 作为 broker ，安装完成后默认启动了，也不需要其他任何配置
    ```
    # apt-get install rabbitmq-server
    ```

- 2、安装celery
    ```
    # pip3 install celery
    ```

- 3、安装 celery
celery 用在 django 项目中， django 项目目录结构 ( 简化 ) 如下
    ```
    website/
    |-- deploy
    |   |-- admin.py
    |   |-- apps.py
    |   |-- __init__.py
    |   |-- models.py
    |   |-- tasks.py
    |   |-- tests.py
    |   |-- urls.py
    |   `-- views.py
    |-- manage.py
    |-- README
    `-- website
        |-- celery.py
        |-- __init__.py
        |-- settings.py
        |-- urls.py
        `-- wsgi.py
    ```
    
- 4、创建 `website/celery.py` 主文件

    ```py
    from __future__ import absolute_import, unicode_literals
    import os
    from celery import Celery, platforms

    # set the default Django settings module for the 'celery' program.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')

    app = Celery('website')

    # Using a string here means the worker don't have to serialize
    # the configuration object to child processes.
    # - namespace='CELERY' means all celery-related configuration keys
    #   should have a `CELERY_` prefix.
    app.config_from_object('django.conf:settings', namespace='CELERY')

    # Load task modules from all registered Django app configs.
    app.autodiscover_tasks()

    # 允许root 用户运行celery
    platforms.C_FORCE_ROOT = True

    @app.task(bind=True)
    def debug_task(self):
        print('Request: {0!r}'.format(self.request))
    ```
    
- 5、在 `website/__init__.py` 文件中增加如下内容，确保 django 启动的时候这个 app 能够被加载到

    ```py
    from __future__ import absolute_import

    # This will make sure the app is always imported when
    # Django starts so that shared_task will use this app.
    from .celery import app as celery_app

    __all__ = ['celery_app']
    ```
    
- 6、各应用创建 `tasks.py` 文件，这里为 `deploy/tasks.py`

    ```py
    from __future__ import absolute_import
    from celery import shared_task

    @shared_task
    def add(x, y):
        return x + y
    ```
    <u>注意 tasks.py 必须建在各 app 的根目录下，且只能叫 tasks.py ，不能随意命名</u>
    <br>
- 7、views.py 中引用使用这个tasks异步处理
    - 使用函数名` .delay()` 即可使函数异步执行 
    - 可以通过 `result.ready()` 来判断任务是否完成处理 
    - 如果任务抛出一个异常，使用 `result.get(timeout=1)` 可以重新抛出异常 
    - 如果任务抛出一个异常，使用 `result.traceback` 可以获取原始的回溯信息

    ```py
    from deploy.tasks import add

    def post(request):
        result = add.delay(2, 3)
    ```
    
- 8、启动celery
    ```
    # celery -A website worker -l info
    ```
    
- 9、这样在调用post这个方法时，里边的add就可以异步处理了

---

## 二、定时任务
定时任务的使用场景就很普遍了，比如我需要定时发送报告给老板



### 定时任务配置

- 1、`website/celery.py` 文件添加如下配置以支持定时任务 **crontab**
    ```py
    from celery.schedules import crontab

    app.conf.update(
        CELERYBEAT_SCHEDULE = {
            'sum-task': {
                'task': 'deploy.tasks.add',
                'schedule':  timedelta(seconds=20),
                'args': (5, 6)
            }
            'send-report': {
                'task': 'deploy.tasks.report',
                'schedule': crontab(hour=4, minute=30, day_of_week=1),
            }
        }
    )
    ```
    - 定义了两个 **task** ： 
        - 名字为 `'sum-task'` 的 task ，<u>每 20 秒</u> 执行一次 `add` 函数，并传了两个参数 5 和 6 
        - 名字为 `'send-report'` 的 task ，<u>每周一早上 4:30</u> 执行 `report` 函数
    - **timedelta** 是 datetime 中的一个对象，需要`from datetime import timedelta`引入，有如下几个参数
        ```
        days：天
        seconds：秒
        microseconds：微妙
        milliseconds：毫秒
        minutes：分
        hours：小时
        ```
    - **crontab** 的参数有：
        ```
        month_of_year：月份
        day_of_month：日期
        day_of_week：周
        hour：小时
        minute：分钟
        ```

- 2、`deploy/tasks.py`文件添加`report`方法：
    ```py
    @shared_task
    def report():
        return 5
    ```

- 3、启动 celery beat, 
celery 启动了一个 beat 进程一直在不断的判断是否有任务需要执行
    ```
    # celery -A website beat -l info
    ```
    
---

## Tips
1. 如果你同时使用了异步任务和计划任务，有一种更简单的启动方式 `celery -A website worker -b -l info` ，可同时启动 worker 和 beat <br><br>

2. 如果使用的不是 rabbitmq 做队列那么需要在主配置文件中 `website/celery.py` 配置 broker 和 backend ，如下：

    ```py
    # redis做MQ配置
    app = Celery('website', backend='redis', broker='redis://localhost')
    # rabbitmq做MQ配置
    app = Celery('website', backend='amqp', broker='amqp://admin:admin@localhost')
    ```

3. celery 不能用 root 用户启动的话需要在主配置文件中添加 `platforms.C_FORCE_ROOT = True` <br><br>

4. celery 在长时间运行后可能出现内存泄漏，需要添加配置 `CELERYD_MAX_TASKS_PER_CHILD = 10` ，表示每个 worker 执行了多少个任务就死掉


---
参考文章：

http://docs.celeryproject.org/en/latest/

https://github.com/pylixm/celery-examples

https://pylixm.cc/posts/2015-12-03-Django-celery.html







<br><br><br><br><br><br><br><br><br><br><br><br><br>

```py

```

<u></u>

<br><br><br><br><br><br><br><br><br><br>