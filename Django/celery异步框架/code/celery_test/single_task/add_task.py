from celery_app_task import add

result = add.delay(4,5)
print(result.id)    # 将返回任务 id