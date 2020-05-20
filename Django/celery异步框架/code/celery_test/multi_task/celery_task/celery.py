'''celery连接和配置相关文件,必须叫这个名字 '''

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