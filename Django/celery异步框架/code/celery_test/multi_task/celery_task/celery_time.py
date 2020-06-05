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
        'schedule': timedelta(seconds=2),           # 每隔 2 秒执行一次
        'args': ('time_task',)                           # 任务传递的参数
    },
    # 2. 特定时间执行
    # 'add-every-12-seconds': {
    #     'task': 'celery_task.tasks1.test_celery',
    #     每年4月11号，8点42分执行
    #     'schedule': crontab(minute=42, hour=8, day_of_month=11, month_of_year=4),
    #     'args': (16, 16)
    # },
}