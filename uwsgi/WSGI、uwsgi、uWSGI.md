[toc]

---

[出处](https://www.cnblogs.com/jayxuan/p/10785062.html)

## WSGI ：网络通信 **接口**

web服务器网管接口，是 ==**接口**==。
用于接收用户请求并将请求进行初次封装，然后交给 web 框架；



### 什么是 CGI

[出处](https://www.jianshu.com/p/65807220b44a)

先说一下 **`CGI`** （通用网关接口，**C**ommon **G**ateway **I**nterface ），
<u>**定义客户端与 Web 服务器的交流方式的一个程序**</u>。

例如正常情况下客户端发来一个请求，根据 HTTP 协议 Web 服务器将请求内容解析出来，进过计算后，再将加 us 安出来的内容封装好，
例如服务器返回一个 HTML 页面，并且根据 HTTP 协议构建返回内容的响应格式。
涉及到 <u>TCP 连接<u>、 </u>HTTP 原始请求</u> 和 <u>相应格式</u> 的这些，
以上的工作需要一个程序来完成，而这个程序便是 CGI 。

### 什么是 WSGI

- **那什么是 WSGI 呢？**

> 维基上的解释为， Web 服务器网关接口 ( Python **W**eb **S**erver **G**ateway **I**nterface ， WSGI ) ，
是**为 Python 语言定义的 Web 服务器和 Web 应用程序或框架之间的一种简单而通用的==接口==**。

从语义上理解，貌似 <u>WSGI 就是 Python 为了解决 **Web 服务器端与客户端之间的==通信问题==** 而产生的</u>，
并且 WSGI 是基于现存的 CGI 标准而设计的，同样是一种程序（或者 Web 组件的接口规范？）。

WSGI 区分为两部分：
1）一种为 “服务器” 或 “网关” ，
2）一种为 “应用程序” 或 “应用框架”。

所谓的 **WSGI 中间件** 同时实现了 API 的两方，即在 WSGI 服务器和 WSGI 应用之间起调解作用：
1）从 WSGI 服务器的角度来说，中间件扮演应用程序，
2）从应用程序的角度来说，中间件扮演服务器。

**中间件** 具有的功能：

- 重写环境变量后，根据目标 URL ，将请求消息路由到不同的应用对象。
- 允许在一个进程中同时运行多个应用程序或应用框架
- 负载均衡和远程处理，通过在网络上转发请求和相应消息。
- 进行内容后处理，例如应用 XSLT 样式表。（以上 from 维基）

看了这么多，总结一下，其实可以说 WSGI 就是基于 Python 的以 CGI 为标准做一些扩展。

<br>

### 什么是 ASGI

异步网关协议接口，一个介于网络协议服务和 Python 应用之间的标准接口，能够处理多种通用的协议类型，包括 HTTP ， HTTP2 和 WebSocket 。

目前的常用的 WSGI 主要是针对 HTTP 风格的请求响应模型做的设计，然而越来越多的不遵循这种模式的协议逐渐成为 Web 变成的标准之一，例如 WebSocket 。

ASGI 尝试保持在一个简单的应用接口的前提下，
提供允许数据能够在任意的时候、被任意应用进程发送和接受的抽象。
并且同样描述了一个新的，兼容 HTTP 请求响应以及 WebSocket 数据帧的序列格式。
允许这些协议能通过网络或本地 socket 进行传输，以及让不同的协议被分配到不同的进程中。

<br>


### WSGI 和 ASGI 的区别在哪

以上， WSGI 是基于 HTTP 协议模式的，不支持 WebSocket ，
而 **<u>ASGI 的诞生则是为了解决 Python 常用的 WSGI 不支持当前 Web 开发中的一些新的协议标准</u>**。
同时， ASGI 对于 WSGI 原有的模式的支持和 WebSocket 的扩展，即 <u>ASGI 是 WSGI 的扩展</u>。




---

## uwsgi：服务器通信 **协议**
是一个 <u>uWSGI服务器自有的 ==**协议**==</u>，它用于 <u>**定义传输信息的类型**</u>。
每一个uwsgi packet（数据信息包）前 4byte为传输信息类型描述，
用于 <u>与 nginx 等代理服务器通信</u>；

即 <u>**==uwsgi 是与 nginx 等代理服务器通信的协议==**</u>

![出处](https://img2018.cnblogs.com/blog/1484492/201904/1484492-20190428174210592-265891904.png)


---

## uWSGI：**服务器**
uWSGI是一个 ==**web服务器**==，它实现了WSGI协议、uwsgi协议、HTTP等协议。
是一个服务器，是可以在 linux 上安装的，是可以提供服务的

与之相对的异步 web服务器就是 **Daphne**