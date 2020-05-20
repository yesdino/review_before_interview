import sys
from celery.result import AsyncResult
from celery_app_task import cel


id = sys.argv[1]    # 任务 ID 号执行时传入
async = AsyncResult(id=id, app=cel)

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