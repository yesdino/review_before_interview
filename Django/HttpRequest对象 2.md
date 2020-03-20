[toc]

---


[原文](https://www.cnblogs.com/weihengblog/p/9016052.html)

Django中通过使用请求和响应对象来传递系统的状态。

当请求一个页面的时候，Django就创建一个HttpRequest对象，
它包含了关于请求的元数据对象，
然后Django加载适当的视图，并将HttpRequest作为视图函数的第一个参数，
每个视图负责返回一个HttpResponse对象。

# HttpRequest对象
class HttpRequest [源代码](https://docs.djangoproject.com/en/2.0/_modules/django/http/request/#HttpRequest)

## 常用属性

### path_info
HttpRequest.path_info     
返回用户访问url，不包括域名

### method
HttpRequest.method        
请求中使用的HTTP方法的字符串表示，全大写表示。

### GET
HttpRequest.GET             
包含所有 HTTP GET 参数的类字典对象

### POST
HttpRequest.POST           
包含所有 HTTP POST 参数的类字典对象

### body
HttpRequest.body
请求体，byte类型 request.POST 的数据就是从body里面提取到的

## 其他属性
属性：
django将请求报文中的请求行、头部信息、内容主体封装成    HttpRequest 类中的属性。
除了特殊说明的之外，其他均为 ==**只读**== 的。

0、 **HttpRequest.scheme**
   表示请求方案的字符串（通常为http或https）

1、 **HttpRequest.body**
一个字符串，代表请求报文的主体。在处理非 HTTP 形式的报文时非常有用，例如：二进制图片、XML,Json等。

但是，如果要处理表单数据的时候，推荐还是使用 HttpRequest.POST 。

另外，我们还可以用 python 的类文件方法去操作它，详情参考 HttpRequest.read() 。

 

2、**HttpRequest.path**

一个字符串，表示请求的路径组件（不含域名）。

例如："/music/bands/the_beatles/"



3、**HttpRequest.method**

一个字符串，表示请求使用的HTTP 方法。必须使用大写。

例如："GET"、"POST"

 

4、**HttpRequest.encoding**

一个字符串，表示提交的数据的编码方式（如果为 None 则表示使用 DEFAULT_CHARSET 的设置，默认为 'utf-8'）。
   这个属性是可写的，你可以修改它来修改访问表单数据使用的编码。
   接下来对属性的任何访问（例如从 GET 或 POST 中读取数据）将使用新的 encoding 值。
   如果你知道表单数据的编码不是 DEFAULT_CHARSET ，则使用它。

 

5、**HttpRequest.GET**

一个类似于字典的对象，包含 HTTP GET 的所有参数。详情请参考 QueryDict 对象。

 

6、**HttpRequest.POST**

一个类似于字典的对象，如果请求中包含表单数据，则将这些数据封装成 QueryDict 对象。

POST 请求可以带有空的 POST 字典 —— 如果通过 HTTP POST 方法发送一个表单，但是表单中没有任何的数据，QueryDict 对象依然会被创建。
   因此，不应该使用 if request.POST  来检查使用的是否是POST 方法；应该使用 if request.method == "POST" 

另外：如果使用 POST 上传文件的话，文件信息将包含在 FILES 属性中。

 7、**HttpRequest.COOKIES**

一个标准的Python 字典，包含所有的cookie。键和值都为字符串。

 

8、**HttpRequest.FILES**

一个类似于字典的对象，包含所有的上传文件信息。
   FILES 中的每个键为<input type="file" name="" /> 中的name，值则为对应的数据。

注意，FILES 只有在请求的方法为POST 且提交的<form> 带有enctype="multipart/form-data" 的情况下才会
   包含数据。否则，FILES 将为一个空的类似于字典的对象。

 

9、**HttpRequest.META**

 一个标准的Python 字典，包含所有的HTTP 首部。具体的头部信息取决于客户端和服务器，下面是一些示例：

    CONTENT_LENGTH      —— 请求的正文的长度（是一个字符串）。
    CONTENT_TYPE        —— 请求的正文的 MIME 类型。
    HTTP_ACCEPT         —— 响应可接收的 Content-Type。
    HTTP_ACCEPT_ENCODING —— 响应可接收的编码。
    HTTP_ACCEPT_LANGUAGE —— 响应可接收的语言。
    HTTP_HOST           —— 客服端发送的 HTTP Host 头部。
    HTTP_REFERER        —— Referring 页面。
    HTTP_USER_AGENT     —— 客户端的 user-agent 字符串。
    QUERY_STRING        —— 单个字符串形式的查询字符串（未解析过的形式）。
    REMOTE_ADDR         —— 客户端的 IP 地址。
    REMOTE_HOST         —— 客户端的主机名。
    REMOTE_USER         —— 服务器认证后的用户。
    REQUEST_METHOD      —— 一个字符串，例如"GET" 或"POST"。
    SERVER_NAME         —— 服务器的主机名。
    SERVER_PORT         —— 服务器的端口（是一个字符串）。

 从上面可以看到，除 CONTENT_LENGTH 和 CONTENT_TYPE 之外，请求中的任何 HTTP 首部转换为 META 的键时，
    都会将所有字母大写并将连接符替换为下划线最后加上 HTTP_  前缀。
    所以，一个叫做 X-Bender 的头部将转换成 META 中的 HTTP_X_BENDER 键。

 
10、**HttpRequest.user**

一个 `AUTH_USER_MODEL` 类型的对象，表示当前登录的用户。

如果用户当前没有登录，user 将设置为 `django.contrib.auth.models.AnonymousUser` 的一个实例。你可以通过 `is_authenticated()` 区分它们。
```py
# user 只有当Django 启用 AuthenticationMiddleware 中间件时才可用。

if request.user.is_authenticated():
    # Do something for logged-in users.
else:
    # Do something for anonymous users.
```


-------------------------------------------------------------------------------------

```py
匿名用户
class models.AnonymousUser
```

`django.contrib.auth.models.AnonymousUser` 类实现了`django.contrib.auth.models.User` 接口，但具有下面几个不同点：

```py
id 永远为 None。
username 永远为空字符串。
get_username() 永远返回空字符串。
is_staff 和 is_superuser 永远为 False。
is_active 永远为 False。
groups 和 user_permissions 永远为空。
is_anonymous() 返回True 而不是False。
is_authenticated() 返回 False 而不是 True。
set_password()、check_password()、save() 和 delete() 引发 NotImplementedError。
```

New in Django 1.8:
新增 AnonymousUser.get_username() 以更好地模拟 django.contrib.auth.models.User。

 

11、**HttpRequest.session**

 一个既可读又可写的类似于字典的对象，表示当前的会话。只有当Django 启用会话的支持时才可用。
    完整的细节参见会话的文档。


# 上传下载示例
<u>file 为页面上 type=files 类型 input 的 name 属性值</u>
```py
def upload(request):
    """
    保存上传文件前，数据需要存放在某个位置。默认当上传文件小于2.5M时，django会将上传文件的全部内容读进内存。从内存读取一次，写磁盘一次。
    但当上传文件很大时，django会把上传文件写到临时文件中，然后存放到系统临时文件夹中。
    :param request: 
    :return: 
    """
    if request.method == "POST":
        # 从请求的 FILES 中获取上传文件的文件名，
        # file 为页面上 type=files 类型 input 的 name 属性值
        filename = request.FILES["file"].name
        with open(filename, "wb") as f: # 在项目目录下新建一个文件
            for chunk in request.FILES["file"].chunks(): # 从上传的文件对象中一点一点读
                f.write(chunk)          # 写入本地文件
        return HttpResponse("上传OK")
```

# HttpRequest 方法

## get_host
`HttpRequest.get_host()`

根据从`HTTP_X_FORWARDED_HOST`（如果打开 USE_X_FORWARDED_HOST，默认为False）和 `HTTP_HOST` 头部信息返回请求的原始主机。

如果这两个头部没有提供相应的值，则使用 `SERVER_NAME` 和`SERVER_PORT` ，在PEP 3333 中有详细描述。

`USE_X_FORWARDED_HOST` ：一个布尔值，用于指定是否优先使用 X-Forwarded-Host 首部，仅在代理设置了该首部的情况下，才可以被使用。

例如："127.0.0.1:8000"

注意：
当主机位于多个代理后面时，get_host() 方法将会失败。
除非使用中间件重写代理的首部。

 
## get_full_path
`HttpRequest.get_full_path()`

返回 path，如果可以将加上查询字符串。

例如："/music/bands/the_beatles/?print=true"

 

## get_signed_cookie
返回签名过的Cookie 对应的值
```py
HttpRequest.get_signed_cookie(key, default=RAISE_ERROR, salt='', max_age=None)

# 【可选参数：
# salt    : 可以用来对安全密钥强力攻击提供额外的保护。
# max_age : 参数用于检查 Cookie 对应的时间戳以确保 Cookie 的时间不会超过 max_age 秒。
```

- 如果签名不再合法则返回`django.core.signing.BadSignature`。
- 如果提供 default 参数，将不会引发异常并返回 default 的值。

```py
>>> request.get_signed_cookie('name')
'Tony'

>>> request.get_signed_cookie('name', salt='name-salt')
'Tony' # 假设在设置cookie的时候使用的是相同的salt

>>> request.get_signed_cookie('non-existing-cookie')
...
KeyError: 'non-existing-cookie'    # 没有相应的键时触发异常

>>> request.get_signed_cookie('non-existing-cookie', False)
False

>>> request.get_signed_cookie('cookie-that-was-tampered-with')
...
BadSignature: ...    

>>> request.get_signed_cookie('name', max_age=60)
...
SignatureExpired: Signature age 1677.3839159 > 60 seconds

>>> request.get_signed_cookie('name', False, max_age=60)
False
```         


## is_secure
`HttpRequest.is_secure()`

如果请求时是安全的，则返回True；
即请求通是过 ==HTTPS== 发起的。

 

## is_ajax
`HttpRequest.is_ajax()`

如果请求是通过 ==XMLHttpRequest== 发起的，则返回True，

方法是检查 `HTTP_X_REQUESTED_WITH` 相应的首部是否是字符串`'XMLHttpRequest'`。

大部分现代的 JavaScript 库都会发送这个头部。
<u>如果你编写自己的 XMLHttpRequest 调用（在浏览器端），你必须手工设置这个值来让 is_ajax() 可以工作。</u>

<br>
如果一个响应需要根据请求是否是通过AJAX 发起的，并且你正在使用某种形式的缓存例如Django 的 cache middleware ， 

你应该使用 `vary_on_headers('HTTP_X_REQUESTED_WITH')` 装饰你的视图以让响应能够正确地 **缓存**。
