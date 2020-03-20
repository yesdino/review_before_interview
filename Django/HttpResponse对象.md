[toc]

---

[原文](https://www.cnblogs.com/huwei934/p/6978641.html)

# 分类 
## HttpResponse对象

- 在 django.http 模块中定义了 HttpResponse 对象的 API
- HttpRequest 对象由 Django 自动创建，HttpResponse 对象由程序员创建
- 不调用模板，直接返回数据
```py
#coding=utf-8
from django.http import HttpResponse

def index(request):
    str = '<h1>hello world</h1>'
    return HttpResponse(str)
```
- 调用模板
```py
from django.http import HttpResponse
from django.template import RequestContext, loader

def index(request):
    t1 = loader.get_template('polls/index.html')
    context = RequestContext(request, {'h1': 'hello'})
    return HttpResponse(t1.render(context))
```
### 属性
- **content**: 表示返回的内容，字符串类型
- **charset**: 表示 response 采用的<u>编码字符集</u>，字符串类型
- **status_code**: 响应的 HTTP 响应状态码
- **content-type**: 指定输出的 MIME 类型

### 方法
- `init()` : 使用页内容实例化 HttpResponse 对象
- `write(content)`: 以文件的方式写
- `flush()`: 以<u>**文件**</u>的方式输出缓存区
- `set_cookie(key, value='', max_age=None, expires=None)`: 设置Cookie
    - `key`, `value` 都是字符串类型
    - `max_age` 是一个整数，表示在指定秒数后过期
    - `expires` 是一个 datetime 或 timedelta 对象，会话将在这个指定的日期/时间过期，注意datetime 和 timedelta 值只有在使用PickleSerializer 时才可序列化
    - `max_age` 与 expires 二选一
    - 如果不指定过期时间，则两个星期后过期

```py
from django.http import HttpResponse
from datetime import *

def index(request):
    response = HttpResponse()
    if request.COOKIES.has_key('h1'):
        response.write('<h1>' + request.COOKIES['h1'] + '</h1>')
    response.set_cookie('h1', '你好', 120)  # 缓存
    # response.set_cookie('h1', '你好', None, datetime(2016, 10, 31))
    return response
```
- delete_cookie(key): 删除指定的key的Cookie，如果key不存在则什么也不发生

## 子类 HttpResponseRedirect

### 重定向，服务器端跳转
- 构造函数的第一个参数用来指定重定向的地址
```py
# 在 views1.py 中
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    return HttpResponseRedirect('js/')

def index2(request,id):
    return HttpResponse(id)
```
```py
# urls.py 中增加一个url对象
url(r'^([0-9]+)/$', views1.index2, name='index2'),
```
请求地址栏如图: 
请求地址栏

请求结果的地址栏如图: 
请求地址栏

### **反向解析**（推荐使用 返回 url.py
```py
from django.core.urlresolvers import reverse

def index(request):
    # 应该是去到 url 那里
    return HttpResponseRedirect(reverse('booktest:index2', args=(1,)))
```

## 子类 JsonResponse
- ==**返回json数据**==，一般用于异步请求
- _init _(data)
- 帮助用户创建 <u>JSON 编码的响应</u>
- 参数 data 是字典对象
- JsonResponse 的**默认** Content-Type 为 `application/json`

```py
from django.http import JsonResponse

def index2(requeset):
    return JsonResponse({'list': 'abc'})
```

# 应用：简写函数 

## render
结合一个给定的模板和一个给定的上下文字典，并返回一个渲染后的HttpResponse对象
```py
render(request, template_name[, context])

# 【参数
# request       : 该 request 用于生成 response
# template_name : 要使用的模板的完整名称
# context       : 添加到模板上下文的一个字典，视图将在渲染模板之前调用它
```

```py
from django.shortcuts import render

def index(request):
    return render(request, 'booktest/index.html', {'h1': 'hello'})
```

## 重定向

- redirect(to)
- 为传递进来的参数返回HttpResponseRedirect
- to 推荐使用**反向解析**

```py
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

def index(request):
    return redirect(reverse('booktest:index2'))
```

## 得到对象或返回404
- 通过模型管理器或查询集调用get()方法，
- 如果没找到对象，不引发模型的 DoesNotExist 异常，而是引发 <u>Http404</u> 异常
- 如果找到多个对象将引发 <u>MultipleObjectsReturned</u> 异常
```py
get_object_or_404(klass, args, *kwargs)

# 【参数：
# klass     : 获取对象的模型类、Manager 对象或 QuerySet 对象
# **kwargs  : 查询的参数，格式应该可以被 get() 和 filter() 接受
```
```py
from django.shortcuts import *

def detail(request, id):
    try:
        book = get_object_or_404(BookInfo, pk=id)
    except BookInfo.MultipleObjectsReturned:
        book = None
    return render(request, 'booktest/detail.html', {'book': book})
```
将 settings.py 中的 DEBUG 改为 False
将请求地址输入2和100查看效果

## 得到列表或返回404
```py
get_list_or_404(klass, args, *kwargs)

# 【参数：
# klass     : 获取列表的一个 Model、Manager 或 QuerySet 实例
# **kwargs  : 查寻的参数，格式应该可以被 get() 和 filter() 接受
```
```py
from django.shortcuts import *

def index(request):
    # list = get_list_or_404(BookInfo, pk__lt=1)
    list = get_list_or_404(BookInfo, pk__lt=6)
    return render(request, 'booktest/index.html', {'list': list})
```

将 settings.py 中的 DEBUG 改为 False