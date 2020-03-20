原文：
https://mp.weixin.qq.com/s/3QD4HejfiSoVDRHWfZCgQg

缓存(Cache)对于创建一个高性能的网站和提升用户体验来说是非常重要的，然而对我们这种只用得起拼多多的码农而言最重要的是学会如何使用缓存。

今天我们就来看看缓存Cache应用场景及工作原理吧，并详细介绍如何在Django中设置Cache并使用它们。


# 什么是缓存Cache

缓存是一类可以更快的读取数据的介质统称，也指其它可以加快数据读取的存储方式。<br>一般用来存储临时数据，常用介质的是读取速度很快的内存。<br>一般来说从数据库多次把所需要的数据提取出来，要比从内存或者硬盘等一次读出来付出的成本大很多。

对于中大型网站而言，使用缓存减少对数据库的访问次数是提升网站性能的关键之一。



# 为什么要使用缓存Cache

在Django中，当用户请求到达视图 view 后，view 会先从数据库提取数据放到模板中进行动态渲染，渲染后的结果就是用户看到的网页。

如果用户每次请求都从数据库提取数据并渲染，将极大降低性能，不仅服务器压力大，而且客户端也无法即时获得响应。<br>如果能将渲染后的结果放到速度更快的缓存中，每次有请求过来，先检查缓存中是否有对应的资源，<br>如果有，直接从缓存中取出来返回响应，节省取数据和渲染的时间，不仅能大大提高系统性能，还能提高用户体验。



我们来看一个实际的博客例子。每次当我们访问首页时，下面视图都会从数据库中提取文章列表，并渲染的模板里去。<br>大多数情况下，我们的博客不会更新得那么频繁，所以文章列表是不变的。<br>这样用户在一定时间内 ==<u>**多次访问**</u>首页时都从数据库重新读取<u>**同样的数据**</u>== 是一种很大的浪费。

```py
# 普通方法
from django.shortcuts import render

def index(request):
    # 读取数据库等并渲染到网页
    article_list = Article.objects.all()
    return render(request, 'index.html', {'article_list': article_list})
```

使用缓存Cache就可以帮我们解决这个问题。<br>当用户首次访问博客首页时，我们从数据库中提取文章列表，并将其存储到缓存里(常用的是内存，这取决于你的设置)。<br>当用户在单位时间内再次访问首页时, Django先检查缓存是否过期(本例是15分钟), 再检查缓存里文章列表资源是否存在，如果存在，直接从缓存中读取数据, 并渲染模板。

```py
# 使用 cache 缓存
from django.shortcuts import render
from django.views.decorators.cache import cache_page

# 秒数，这里设定缓存 15 分钟
@cache_page(60 * 15)  
def index(request):
    article_list = Article.objects.all()
    return render(request, 'index.html', {'article_list': article_list})
```

注意: 在Django中使用缓存前，我们必需先做必要的设置。



# 缓存Cache的应用场景

缓存主要适用于对页面实时性要求不高的页面。<br>存放在缓存的数据，通常是 ==<u>频繁访问的，而不会经常修改</u>== 的数据。

我们来举几个应用例子:

- **博客文章** 。假设用户一天更新一篇文章，那么可以为博客设置1天的缓存，一天后会刷新。

- **购物网站** 。商品的描述信息几乎不会变化，而商品的购买数量需要根据用户情况实时更新。<br>我们可以只选择缓存商品描述信息。

- **缓存网页片段** 。<br>比如缓存网页导航菜单和脚部(Footer)。


# Django 中使用缓存

## 1. 缓存后台 Backend 设置
Django中提供了多种缓存方式，如果要使用缓存，需要先在 settings.py 中进行配置，然后应用。<br>根据缓存介质的不同，你需要设置不同的 **缓存后台Backend**。



### Memcached 缓存

Memcached是基于 **内存** 的缓存，Django原生支持的最快最有效的缓存系统。<br>对于大多数场景，我们推荐使用 Memcached，数据缓存在服务器端。<br>使用前需要通过 pip 安装 memcached 的插件 python-memcached 和 pylibmc，可以同时支持多个服务器上面的memcached。

下面是使用 pyhon-memcached 的设置。
```py
# localhost
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

# unix soket
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'unix:/tmp/memcached.sock',
    }
}   

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': [
            '172.19.26.240:11211',
            '172.19.26.242:11211',
        ]
        # 我们也可以给缓存机器加权重，权重高的承担更多的请求，如下
        'LOCATION': [
            ('172.19.26.240:11211',5),
            ('172.19.26.242:11211',1),
        ]
    }
}
```

### 数据库缓存
```py
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'my_cache_table',
    }
```

### 文件系统缓存
```py
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',        #这个是文件夹的路径
        #'LOCATION': 'c:\foo\bar',#windows下的示例
    }
}
```

### 本地内存缓存
```py
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake'
    }
}
```

## 2. 代码中如何使用 Cache

当你做好Cache的设置后，在代码中你可以有三种方式使用Cache。

- 在视图 View 中使用
- 在路由 URLConf 中使用
- 在模板中使用



### 在视图 View 中使用 cache
```py
# view.py
from django.views.decorators.cache import cache_page

@cache_page(60 * 15)
def my_view(request):
    ...
```

### 在路由 URLConf 中使用 cache

这是小编我更喜欢的方式，这样你就不用修改负责逻辑部分的view了。
```py
# url.py
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('foo/<int:code>/', cache_page(60 * 15)(my_view)),
]
```

### 在模板中使用 cache
```py
{% load cache %}
{% cache 500 sidebar request.user.username %}
    .. sidebar for logged in user ..
{% endcache %}
```
对于大部分码农而言，我们只需要懂得如何在django中使用cache即可，而不需要详细了解django后台工作原理，<br>比如Django是如何将数据存储到选定介质的<br>以及django是如何判断缓存是否已经过期的。



## 3. Cache的高级技巧

下面我来介绍下Django中使用cache的一些高级技巧。



### cache_control 设定缓存

通常用户将会面对两种缓存： 
- 他或她自己的浏览器缓存（私有缓存）
- 他或她的提供者缓存（公共缓存）。 
公共缓存由多个用户使用，而受其它人的控制。 

这就产生了你不想遇到的敏感数据的问题，比如说你的银行账号被存储在公众缓存中。 因此，**Web 应用程序需要以某种方式告诉缓存那些数据是私有的，哪些是公共的**。



解决方案是标示出某个页面缓存应当是私有的。 

要在 Django 中完成此项工作，可使用 cache_control 视图修饰器：
```py
from django.views.decorators.cache import cache_control

# 标记为私有缓存
@cache_control(private=True)    
def my_view(request):
# ...
```
该修饰器负责在后台发送相应的 HTTP 头部。

<br>


还有一些其他方法可以控制缓存参数。 

例如, HTTP 允许应用程序执行如下操作:
- 定义页面可以被缓存的最大时间。
- 指定某个缓存是否总是检查较新版本，仅当无更新时才传递所缓存内容。



在 Django 中，可使用 cache_control 视图修饰器指定这些缓存参数。 在下例中， cache_control 告诉缓存对每次访问都重新验证缓存并在最长 3600 秒内保存所缓存版本。
```py
from django.views.decorators.cache import cache_control

# 告诉缓存对每次访问都重新验证缓存并在最长 3600 秒内保存所缓存版本
@cache_control(must_revalidate=True, max_age=3600)
def my_view(request):
# ...
```
在 cache_control() 中，任何合法的Cache-Control HTTP 指令都是有效的。下面是完整列表：
```py
public=True             # 公有
private=True            # 私有
no_cache=True           # 
no_transform=True       # 
must_revalidate=True    # 每次访问都需重新验证缓存
proxy_revalidate=True   # 
max_age=num_seconds     # 可以被缓存的最大时间
s_maxage=num_seconds    # 
```

### vary_on_headers 注意请求头部

缺省情况下，Django 的缓存系统使用所请求的路径(如`blog/article/1`)来创建其缓存键。<br>这意味着不同用户请求同样路径都会得到同样的缓存版本，不会考虑客户端`user-agent`，`cookie`和语言配置的不同。

除非你使用Vary头部通知缓存机制需要考虑请求头里的cookie和语言的不同。



要在 Django 完成这项工作，可使用便利的 vary_on_headers 视图装饰器。<br>例如下面代码告诉Django读取缓存数据时需要同时考虑`User-Agent`和`Cookie`的不同。
```py
from django.views.decorators.vary import vary_on_headers

# 读取缓存数据时需要同时考虑User-Agent和Cookie的不同
@vary_on_headers('User-Agent', 'Cookie')
def my_view(request):
    ...
```

### never_cache 禁用缓存
如果你想用头部完全禁掉缓存, 你可以使用`django.views.decorators.cache.never_cache`装饰器。

如果你不在视图中使用缓存，服务器端是肯定不会缓存的，然而用户的客户端如浏览器还是会缓存一些数据，<br>这时你可以使用never_cache禁用掉客户端的缓存。
```py
from django.views.decorators.cache import never_cache

@never_cache
def myview(request):
# ...
```