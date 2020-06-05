from celery_app_task import add
from datetime import datetime
from datetime import timedelta

# 方式一
# v1 = datetime(2019, 2, 13, 18, 19, 56)
# print(v1)
# v2 = datetime.utcfromtimestamp(v1.timestamp())将当前时间转成utc格式
# print(v2)
# result = add.apply_async(args=[1, 3], eta=v2)
# print(result.id)

# 方式二
ctime = datetime.now()
utc_ctime = datetime.utcfromtimestamp(ctime.timestamp()) # 默认用 utc 时间,需要转成 utc 时间格式
time_delay = timedelta(seconds=10)
task_time = utc_ctime + time_delay  # 设定的时间

# 使用 apply_async 并设定时间
result = add.apply_async(args=[4, 6], eta=task_time)
print(result.id)