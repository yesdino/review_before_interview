python 自带的 json 库
```py
# json   ------ loads ----->  python 
# 字符串 <----- dumps ------  数据类型

dumps():    python 数据类型 -> json 字符串
loads():    json 字符串 -> python 数据类型
# -----------------------------------------------------
# 要有文件
dump() :    python 输入 -> json 格式 -> 存入磁盘文件
load() :    将磁盘文件中 json 格式数据 -> python 数据类型
```

[很有用的文章](https://www.cnblogs.com/roygood/p/10152976.html)

注意 serializers 一定要是可迭代对象，源码这样写

```py
# queryset 为待序列化对象
s.serialize(queryset, **options)
for count, obj in enumerate(queryset, start=1):
```


- 传递后台 QuerySet
```py
    import json
    from django.core import serializers

    # python 数据库数据 -> json 形式
    data = serializers.serialize("json", SomeModel.objects.all())
    data1 = serializers.serialize("json", SomeModel.objects.all(), fields=('name','id'))
    data2 = serializers.serialize("json", SomeModel.objects.filter(field = some_value))

    # 传回前台
    return HttpResponse(json.dumps(result, ensure_ascii=False))
```

- 传递后台 ValueQuerySet
```py
    import json
    from django.core.serializers.json import DjangoJSONEncoder

    result = {}
    record = models.TestRecord.objects.all().values()
    result['type'] = str(type(record))                  # QuerySet

    # 1. 作为字典成员返回 首先要在存进字典时序列化 python 数据类型 -> json【字符串】
    result['data'] = json.dumps(list(record), cls=DjangoJSONEncoder)

    # 2. 整个字典在传回前端时再次转换 python -> json
    return HttpResponse(json.dumps(result, ensure_ascii=False))
```

后面发现传回前端的日期有点问题,没有格式化，jquery格式化日期又比较麻烦,所以使用新的序列化类。
解决code:

```py
from datetime import datetime

@csrf_exempt
def serializers_test_action(requests):
    result = {}
    record = models.TestRecord.objects.all().values()    # QuerySet
    
    result['data'] = json.dumps(list(record), cls=ComplexEncoder)
    return HttpResponse(json.dumps(result, ensure_ascii=False))

# 序列化类
class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)
```



<br><br><br>

没有 DateTime 的 字典：<br>
通过 post (注意不是get,而是post回去前端要用jquery处理的) 传回前端：
```

    test_area_list = models.TestArea.objects.filter(
        IsValid=True).values('TestAreaID', 'Area', 'Floor').order_by('TestAreaID')

    context = {
        'test_area_list': list(test_area_list), 
    }
    return HttpResponse(json.dumps(context))
```
