
<!-- [03:55](https://coding.imooc.com/lesson/333.html#mid=24859) -->

websocket 协议是通过 HTTP 协议来建立 TCP 连接的

意思是说 通过 HTTP 来发送 get 请求来升级成 websocket请求

## websocket **请求头** 中的重要字段

- **`Connection`** 和 **`Upgrade`** ：表示客户端发起的是 Websocket 请求
- **`Sec-WebSocket-version`**：客户端所使用的 WebSocket 协议版本号。服务端会确认是否支持该版本号
- **`Sec-Websocket-Key`**：一个Base64编码值，由浏览器随机生成，用于升级 request
- **`Sec-Websocket-Extensions`**：客户端想要表达的协议级的扩展


## websocket **响应头** 中重要的字段
- **`HTTP/1.1 status code 101 Switching Protocols`**：切換协议，Websocket 协议通过 HTTP 协议来建立传输层的 TCP 连接
- **`Connection`** 和 **`Upgrade`**：表示服务端返回的是 WebSocket 响应
- **`Sec-Websocket-Accept`**：表示服务器接受了客户端的请求，由请求头中的 `Sec-Websocket-key` 计算得来
<!-- （[如何计算 07:12](https://coding.imooc.com/lesson/333.html#mid=24859)） -->

## websocket 连接建立的过程

<!-- [00:15](https://coding.imooc.com/lesson/333.html#mid=24860) -->
分三步
①：HTTP 发送 get 请求，通过在请求头中携带 Connection 加 Upgrade 字段指定要讲通信的协议升级为 websocket 
②：服务端返回给客户端的响应头中，HTTP 状态码为 101 `Switching Protocols`，表示协议切换成功。
这两步说明了 websocket 协议的连接过程，并不是跟 HTTP 完全独立的
③：建立 websocket 连接完成，此时已经与 HTTP 无关了。服务端客户端可双向进行通信


## websocket 协议优缺点

<!-- [01:03](https://coding.imooc.com/lesson/333.html#mid=24860) -->
优点：

- 支持双向通信，实时性更强
- 数据格式比较轻量，性能开销小，通信高效
- 支持扩展。用户可以扩展协议或者实现自定义的子协议（比如支持自定乂压缩算法等）


缺点：

- 少部分浏览器不支持，浏览器支持的程度与方式有区别
- 长连接对后端处理业务的代码稳定性要求更高，后端推送功能相对复杂
- 成熟的 HTTP 生态下有大量的组件可以复用，Websocket 较少



## websocket 应用场景

- 即时聊天通信，网站消息通知
- 在线协同编辑。如腾讯文档
- 多玩家在线游戏、视频弹幕、股票基金实施报价。

涉及实时性的大部分都需要使用 websocket 协议



# 在 django 中实现 websocket

## 使用 Ajax 轮询

<!-- [link 0:23](https://coding.imooc.com/lesson/333.html#mid=24861) -->
<img width="600" src="https://upload-images.jianshu.io/upload_images/11876740-9063b346bb0348bf.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240"></img>

假设不使用 websocket，可以通过定时发送 ajax 请求来实现，假设将 ajax 设置成 200ms 一次，对用户来说延时的感觉不是很明显。

但是这种做法对网络和服务器资源的浪费很大：
①：大量的 ajax 每次都要通过 TCP 3次握手建立连接之后再返回
②：即使没有数据也需要不断的发送 ajax 请求去后端，后端的 web server 和 WSGI server 也需要不断的处理这些请求


由上面的缺点我们可以看到，我们不能使用 Ajax 轮询的方式，只能使用 websocket。
那么我们该选择哪种 websocket 方式呢？



## Django Channels


Channel 有哪些优势呢？
<!-- [link 2:21](https://coding.imooc.com/lesson/333.html#mid=24861) -->
- 区分路由 HTTP 请求和 Websocke 请求
- 兼容 Django 的认证系统
- 接收和推送 Websocket 消息
- 通过 ORM 保存和获取数据


还有一个 dwebsocket 也可以实现 websocket，但是兼容 django 没有 channels 做得好，并不能完全兼容 django 框架




### Channels 的原理

<!-- [link 2:09](https://coding.imooc.com/lesson/333.html#mid=24862) -->

- **django websocket 架构**

<img width="600" src="https://upload-images.jianshu.io/upload_images/11876740-fd875defa13b232c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240"></img>

- **`Protoco Type Router`**：不同协议解释器。负责对协议进行解析，将不同协议分发到不同的 Router


<!-- [link 3:10](https://coding.imooc.com/lesson/333.html#mid=24862) -->

- **Channels 的整体架构**
  
<img width="600" src="https://upload-images.jianshu.io/upload_images/11876740-40986e1d34960b02.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240"></img>

3 层架构：
- **`Interface Server`**：负责对协议进行解析，将不同协议分发到不同的 Channel
- **`Channel Layer`**：频道层，可以是一个 FIFO 队列，通常使用 Redis
- **`Consumer`**：消费者，接收和处理消息


##  channels 中文件和配置的含义

- **`asgi.py`**: 相当于 django 中的 wsgi.py 的异步扩展，
  介于网络协议服务和 Python 应用之间的标准接口，能够处理多种通用协议类型，包括 HTTP、HTTP2 和 Websocket

- **`channel_layers`**：在 settings.py 中配置，类似于一个通道，
发送者（producer）在一端发送消息，消费者（consumer）在另外一端监听。
==如果是 websocket 的频道，会把数据缓存在 redis 中==（[7:07](https://coding.imooc.com/lesson/333.html#mid=24862)）

- **`routings.py`** ：相当于 django 中的 urs.py
- **`consumers.py`** ：相当于 django 中的 views.py


## WSGI 和 ASGl 的区别

- **`WSGI (Python Web Server Gateway Interface)`**:

为 Python 语言定义的 Web 服务器和 Web 应用程序或框架之间的一种简单而通用的接口

- **`ASGl (Asynchronous Server Gateway Interface)`**

异步服务网关接口，一个介于网络协议服务和 Python 应用之间的标准接口，
能够处理多种通用的协议类型，包括 HTTP, HTTP2 和 Websocket
<br>

- **`WSGI`** 和 **`ASGI`** 的区别： 

WSGI 是基于 HTTP 协议模式的，不支持Websocket。
而 ASGi 就是为了支持 Python 常用的 WSl 所不支持的新的协议标准，即 **==ASGI 是 WSG 的扩展==**。
而且能通过 asyncio 异步运行.