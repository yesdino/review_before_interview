import celery
import time

# broker='redis://127.0.0.1:6379/1' 不加密码
# broker='redis:pswd//127.0.0.1:6379/2' 加密码
backend = 'redis://127.0.0.1:6379/1'
broker  = 'redis://127.0.0.1:6379/2'
celery_name = 'test'

cel = celery.Celery(celery_name, backend=backend, broker=broker)    # 创建 celery 实例

@cel.task
def add(x, y):   # 定义任务
    return x+y
