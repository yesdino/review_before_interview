# 目录

[toc]


---

# HTTP协议

[source](https://www.cnblogs.com/ranyonsue/p/5984001.html)

## HTTP 简介
**`HTTP`** 协议是 `Hyper Text Transfer Protocol (超文本传输协议)` 的缩写。
是用于从万维网（**`WWW`**:`World Wide Web`）服务器 <u>传输超文本到本地浏览器</u> 的传送协议。

HTTP 是一个 ==**基于 TCP/IP**== 通信协议来传递数据（ HTML 文件 , 图片文件 , 查询结果等）。

HTTP 是一个属于应用层的面向对象的协议，由于其简捷、快速的方式，适用于分布式超媒体信息系统。

它于 1990 年提出，经过几年的使用与发展，得到不断地完善和扩展。
目前在 WWW 中使用的是 HTTP/1.0 的第六版， 
HTTP/1.1 的规范化工作正在进行之中，
而且 HTTP-NG (Next Generation of HTTP) 的建议已经提出。

HTTP 协议工作于客户端 - 服务端架构为上。
浏览器作为 HTTP 客户端通过 URL 向 HTTP 服务端即 WEB 服务器发送所有请求。 
Web 服务器根据接收到的请求后，向客户端发送响应信息。

<img style="width:370px" src="https://upload-images.jianshu.io/upload_images/2964446-5a35e17f298a48e1.jpg?imageMogr2/auto-orient/strip%7CimageView2/2"></img>



## HTTP 主要特点
1、**简单快速**
==客户端只需传送请求方法和路径==。
请求方法常用的有 **`GET`**、**`HEAD`**、**`POST`**。
每种方法规定了客户与服务器联系的类型不同。
由于 HTTP 协议简单，使得 HTTP 服务器的程序规模小，因而通信速度很快。

2、**灵活**
HTTP ==允许传输任意类型的数据对象==。
正在传输的类型由 **`Content-Type`** 加以标记。

3、**无连接**
无连接的含义是限制==每次连接只处理一个请求==。
服务器处理完客户的请求，并收到客户的应答后，即断开连接。
采用这种方式可以节省传输时间。

4、**无状态**
HTTP 协议是无状态协议。无状态是指==协议对于事务处理没有记忆能力==。
缺少状态意味着如果后续处理需要前面的信息，则它必须重传，
这样可能导致每次连接传送的数据量增大。
另一方面，在服务器不需要先前信息时它的应答就较快。

5、**支持 B/S 及 C/S 模式**。

<br>



## URL
HTTP 使用统一资源标识符 **`URI`** 来传输数据和建立连接。 
**`URL`** 是一种特殊类型的 `URI` ，包含了用于查找某个资源的足够的信息

**`URI`**, 全称是 `Uniform Resource Identifiers`, 中文叫 **统一资源定位符**, 
是互联网上用来标识某一处资源的地址。

以下面这个 URL 为例，介绍下普通 URL 的各部分组成：
http://www.aspxfans.com:8080/news/index.asp?boardID=5&ID=24618&page=1#name
从上面的 URL 可以看出，一个完整的 URL 包括以下几部分：
1）**协议部分**
该 URL 的协议部分为“ `http:`”，这代表网页使用的是 HTTP 协议。
在 Internet 中可以使用多种协议，如 HTTP ， FTP 等等本例中使用的是 HTTP 协议。
在 "HTTP" 后面的“ `//` ”为分隔符


2）**域名部分**
该 URL 的域名部分为“ www.aspxfans.com ”。
一个 URL 中，也可以使用 IP 地址作为域名使用

3）**端口部分**
跟在域名后面的是端口，域名和端口之间使用“ : ”作为分隔符。端口不是一个 URL 必须的部分，如果省略端口部分，将采用默认端口

4）**虚拟目录部分**
从域名后的第一个“ / ”开始到最后一个“ / ”为止，是虚拟目录部分。虚拟目录也不是一个 URL 必须的部分。本例中的虚拟目录是“ /news/ ”

5）**文件名部分**
从域名后的最后一个“ / ”开始到“？”为止，是文件名部分，如果没有“ ? ” , 则是从域名后的最后一个“ / ”开始到“ # ”为止，是文件部分，如果没有“？”和“ # ”，那么从域名后的最后一个“ / ”开始到结束，都是文件名部分。本例中的文件名是“ index.asp ”。文件名部分也不是一个 URL 必须的部分，如果省略该部分，则使用默认的文件名

6）**锚部分**
从“ # ”开始到最后，都是锚部分。
本例中的锚部分是“ `name` ”。
锚部分也不是一个 URL 必须的部分

7）**参数部分**
从“`?`”开始到“ `#` ”为止之间的部分为参数部分，又称搜索部分、查询部分。
参数可以允许有多个参数，参数与参数之间用“ `&` ”作为分隔符。

本例中的参数部分为“ `boardID=5&ID=24618&page=1` ”。

<br>

## 请求与响应

###  请求 Request

Http请求消息结构:
<img style="width:500px" src="https://upload-images.jianshu.io/upload_images/2964446-fdfb1a8fce8de946.png?imageMogr2/auto-orient/strip%7CimageView2/2"></img>


客户端发送一个 HTTP 请求到服务器的请求消息包括以下格式：
- 请求行 (`request line`) 、
- **请求头** (`header`) 、
- 空行 (用于分隔请求头和数据，空行后面跟着的就是数据)
- **请求数据** 四个部分组成。
<br>



**Get 请求例子**

使用 Charles 抓取的 request：
```py
1) GET /562f25980001b1b106000338.jpg HTTP/1.1
2) Host    img.mukewang.com
3) User-Agent    Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36
4) Accept    image/webp,image/*,*/*;q=0.8
5) Referer    http://www.imooc.com/
6) Accept-Encoding    gzip, deflate, sdch
7) Accept-Language    zh-CN,zh;q=0.8
```

```py
1) 请求行。用来说明 请求类型、要访问的资源、所使用的 HTTP 版本。
# GET说明请求类型为GET, 
# /562f25980001b1b106000338.jpg 为要访问的资源，
# 该行的最后一部分说明使用的是HTTP1.1版本

第 2 行 ~ 空格行均为请求头：
2) HOST             : 将指出请求的目的地
3) User-Agent       : 发送请求的应用名称。服务器端和客户端脚本都能访问它,它是浏览器类型检测逻辑的重要基础
4) Accept           : 
5) Referer          : 
6) Accept-Encoding  : 通知服务器端可以发送的数据压缩格式
7) Accept-Language  : 通知服务器端可以发送的语言
```


**POST 请求例子**

使用 Charles 抓取的 request ：
```py
1) POST / HTTP1.1
2) Host:www.wrox.com
3) User-Agent:Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022)
4) Content-Type:application/x-www-form-urlencoded
5) Content-Length:40
6) Connection: Keep-Alive
7) 
8) name=Professional%20Ajax&publisher=Wiley
```

```py
请求行      第 1 行明了是post请求，以及 http1.1 版本。
请求头部    第 2~6 行。
空行        第 7 行的空行。
请求数据    第 8 行。
```
```py
1) 请求行。用来说明 请求类型、要访问的资源、所使用的 HTTP 版本。
2) Host             : 
3) User-Agent       : 
4) Content-Type     : 
5) Content-Length   : 
6) Connection       : 指定与连接相关的属性，例如（Keep_Alive，长连接）
7)                  : 
8) data             : 
```


### 响应 response

HTTP 响应也由四个部分组成，分别是：
- 状态行、
- 响应头、
- 空行、
- 响应正文

<img style="width:500px" src="https://upload-images.jianshu.io/upload_images/2964446-1c4cab46f270d8ee.jpg?imageMogr2/auto-orient/strip%7CimageView2/2"></img>


response 例子

```html
1) HTTP/1.1 200 OK
2) Date: Fri, 22 May 2009 06:07:21 GMT
3) Content-Type: text/html; charset=UTF-8
4) 
<html>
      <head></head>
      <body>
            <!--body goes here-->
      </body>
</html>
```
```py
*【状态行】
由 HTTP 协议版本号， 状态码， 状态消息 三部分组成。
第 1 行为状态行，（HTTP/1.1）表明 HTTP 版本为1.1版本，状态码为200，状态消息为（ok）

*【响应头】
用来说明客户端要使用的一些附加信息
第 2 行开始到空行 都为响应头，
Date        : 生成响应的日期和时间；
Content-Type: 指定了 MIME 类型的 HTML(text/html),
charset     : 编码类型是UTF-8

*【空行】
第 4 行。响应头后面的空行是必须的

*【响应正文】
服务器返回给客户端的文本信息。
空行后面的 html 部分为响应正文。
```


## 状态码
状态代码有三位数字组成，第一个数字定义了响应的类别，共分五种类别:
**`1xx`** ：**指示信息**。表示请求已接收，继续处理
**`2xx`** ：**成功**。表示请求已被成功接收、理解、接受
**`3xx`** ：**重定向**。要完成请求必须进行更进一步的操作
**`4xx`** ：**客户端错误**。请求有语法错误或请求无法实现
**`5xx`** ：**服务器端错误**。服务器未能实现合法的请求


常见状态码：
```c
200 OK                        // 客户端请求成功
400 Bad Request               // 客户端请求有语法错误，不能被服务器所理解
401 Unauthorized              // 请求未经授权，这个状态代码必须和 WWW-Authenticate 报头域一起使用 
403 Forbidden                 // 服务器收到请求，但是拒绝提供服务
404 Not Found                 // 请求资源不存在，eg：输入了错误的 URL
500 Internal Server Error     // 服务器发生不可预期的错误
503 Server Unavailable        // 服务器当前不能处理客户端的请求，一段时间后可能恢复正常
```

更多状态码 http://www.runoob.com/http/http-status-codes.html



## HTTP 请求方法
根据 HTTP 标准， HTTP 请求可以使用多种请求方法。
**`HTTP1.0`** 定义了三种请求方法：`GET`, `POST` 和 `HEAD` 方法。
```c
GET         请求指定的页面信息，并返回实体主体。
POST        向指定资源提交数据进行处理请求（例如提交表单或者上传文件）。数据被包含在请求体中。POST请求可能会导致新的资源的建立和/或已有资源的修改。
HEAD        类似于 get 请求，只不过返回的响应中没有具体的内容，用于获取报头
```
**`HTTP1.1`** 新增了五种请求方法：`OPTIONS`, `PUT`, `DELETE`, `TRACE` 和 `CONNECT` 方法。

```c
PUT         从客户端向服务器传送的数据取代指定的文档的内容。
DELETE      请求服务器删除指定的页面。
CONNECT     HTTP/1.1 协议中预留给能够将连接改为管道方式的代理服务器。
OPTIONS     允许客户端查看服务器的性能。
TRACE       回显服务器收到的请求，主要用于测试或诊断。
```
<br>

## HTTP 工作原理

### 请求/响应模型

HTTP 协议定义 Web 客户端如何从 Web 服务器请求 Web 页面，以及服务器如何把 Web 页面传送给客户端。 
HTTP 协议采用了 **请求/响应模型**。
- 客户端向服务器发送一个请求报文，请求报文包含请求的方法、URL、协议版本、请求头部和请求数据。
- 服务端以一个状态行作为响应，响应的内容包括协议的版本、成功或者错误代码、服务器信息、响应头部和响应数据。


### HTTP 请求/响应的步骤

**1、客户端连接到 Web 服务器**
一个 HTTP 客户端，通常是浏览器，
与 Web 服务器的 HTTP 端口（默认为 80）建立一个 ==TCP 套接字连接==。
例如， http://www.oakcms.cn。

**2、发送 HTTP 请求**
通过 TCP 套接字，客户端向 Web 服务器发送一个文本的请求报文。
一个请求报文由请求行、请求头部、空行和请求数据 4 部分组成。

**3、服务器接受请求并返回 HTTP 响应**
Web 服务器解析请求，定位请求资源。
服务器将资源复本写到 TCP 套接字，由客户端读取。
一个响应由状态行、响应头部、空行和响应数据 4 部分组成。

**4、释放连接TCP连接**
- 若 **`connection`** 模式为 `close`，
则服务器主动关闭 TCP 连接，客户端被动关闭连接，释放 TCP 连接; 
- 若 **`connection`** 模式为 `keepalive`，
则该连接会保持一段时间，在该时间内可以继续接收请求 ;

**5、客户端浏览器解析 HTML 内容**
客户端浏览器首先解析状态行，查看表明请求是否成功的状态代码。
然后解析每一个响应头，响应头告知以下为若干字节的 HTML 文档和文档的字符集。
客户端浏览器读取响应数据 HTML ，根据 HTML 的语法对其进行格式化，并在浏览器窗口中显示。


### 在浏览器地址栏键入URL到显示出页面经历的过程
例如：在浏览器地址栏键入URL，按下回车之后会经历以下流程：

1、浏览器向 DNS 服务器请求解析该 URL 中的域名所对应的 IP 地址;

2、解析出 IP 地址后，根据该 IP 地址和默认端口 80，和服务器建立TCP连接;

3、浏览器发出读取文件(URL 中域名后面部分对应的文件)的 HTTP 请求，该请求报文作为 TCP 三次握手的第三个报文的数据发送给服务器;

4、服务器对浏览器请求作出响应，并把对应的 html 文本发送给浏览器;

5、释放 TCP 连接;

6、浏览器将该 html 文本并显示内容; 　




## GET 和 POST 请求的区别

- GET 请求
```html
GET /books/?sex=man&name=Professional HTTP/1.1
Host: www.wrox.com
User-Agent: Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.6)
Gecko/20050225 Firefox/1.0.1
Connection: Keep-Alive

```
(注意最后一行是空行)

- POST 请求
```html
POST / HTTP/1.1
Host: www.wrox.com
User-Agent: Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.6)
Gecko/20050225 Firefox/1.0.1
Content-Type: application/x-www-form-urlencoded
Content-Length: 40
Connection: Keep-Alive

name=Professional%20Ajax&publisher=Wiley
```


GET 和 POST 的区别

### 提交传输数据的方式不同

GET 提交的数据会放在 URL 之后，以 `?` 分割 URL 和传输数据，参数之间以 `&` 相连，
如 `EditPosts.aspx?name=test1&id=123456`. 
POST 方法是把提交的数据放在 HTTP 包的 Body 中 .

### 提交的数据大小限制不同

GET 提交的数据大小有限制（因为浏览器对 URL 的长度有限制），
POST 方法提交的数据没有限制 .

### 获取数据变量方式不同

GET 方式需要使用 **`Request.QueryString`** 来取得变量的值，
POST 方式通过 **`Request.Form`** 来获取变量的值。

### 安全性不同

GET 方式提交数据，会带来安全问题，
比如一个登录页面，通过 GET 方式提交数据时，用户名和密码将出现在 URL 上，
如果页面可以被缓存或者其他人可以访问这台机器，就可以从历史记录获得该用户的账号和密码。

<br>
<br>


**1、请求数据的方式不同**
- GET 提交，**请求的数据会附在 URL 之后**。

以 `?` 分割 URL 和传输数据，多个参数用 `&` 连接；
例如：`login.action?name=hyddd&password=idontknow&verify=%E4%BD%A0 %E5%A5%BD`。
如果数据是英文字母/数字，原样发送，
如果是空格，转换为+，
如果是中文/其他字符，则直接把字符串用BASE64加密，得出如： `%E4%BD%A0%E5%A5%BD`，
其中 **`％XX`** 中的XX为该符号以16进制表示的ASCII。

- POST 提交：**把提交的数据放置在是 HTTP 包的包体中**。

因此， GET 提交的数据会在地址栏中显示出来，而 POST 提交，地址栏不会改变
<br>


**2、传输数据的大小**
首先声明： HTTP 协议没有对传输的数据大小进行限制， HTTP 协议规范也没有对 URL 长度进行限制。

而在实际开发中存在的限制主要有：
- GET 提交: 

<u>特定浏览器和服务器对 URL 长度有限制</u>。
例如 `IE` 对 URL 长度的限制是 2083 字节 (2K+35) 。
其他浏览器，如 `Netscape` 、 `FireFox` 等，理论上没有长度限制，其限制取决于操作系 统的支持。
<u>GET提交时，传输数据就会受到URL长度的限制</u>。

- POST 提交:

由于不是通过 URL 传值，理论上数据不受限。
但实际 <u>各个 WEB 服务器会规定对 post 提交数据大小进行限制</u>， Apache 、 IIS6 都有各自的配置。
<br>

**3、安全性**

POST 的安全性要比 GET 的安全性高。
比如：通过 GET 提交数据，**用户名和密码将明文出现在 URL 上**，因为 
(1) 登录页面有可能被浏览器缓存； 
(2) 其他人查看浏览器的历史纪录，那么别人就可以拿到你的账号和密码了，
除此之外，使用 GET 提交数据还可能会造成 **`Cross-site request forgery`** 攻击




**4、get, post, soap 协议都是在 http 上运行的**

- **`Get`** ：请求参数是作为一个 <u>key/value</u> 对的序列（查询字符串）附加到 URL 上的
查询字符串的长度受到 web 浏览器和 web 服务器的限制（如 IE 最多支持 2048 个字符），**不适合传输大型数据集同时，它很不安全**
<br>

- **`Post`**：请求参数是在 http 标题的一个不同部分（名为 entity body ）传输的，
这一部分用来传输表单信息，因此必须将 `Content-type` 设置为 :`application/x-www-form-urlencoded`。 
post 设计用来支持 web 窗体上的用户字段，其参数也是作为 <u>key/value</u> 对传输。
但是：**它不支持复杂数据类型**，因为 post 没有定义传输数据结构的语义和规则。
<br>

- **`Soap`**：是 http post 的一个专用版本，遵循一种特殊的 xml 消息格式
`Content-type` 设置为 : `text/xml` **任何数据都可以 xml 化**。

Http协议定义了很多与服务器交互的方法，
最基本的有 4 种，分别是 `GET`,`POST`,`PUT`,`DELETE`。

一个 URL 地址用于描述一个网络上的资源，
而 HTTP 中的 **`GET`,`POST`,`PUT`,`DELETE`** 就对应着对这个资源的 **查，改，增，删** 4 个操作。 
我们最常见的就是 GET 和 POST 了。 GET 一般用于获取 / 查询资源信息，而 POST 一般用于更新资源信息 .
<br>











</u>

<br>

<br><br><br><br><br><br><br>
<br><br><br><br><br><br><br>



---


<!-- 
# 2、HTTP 协议

[非原创 出处](https://www.cnblogs.com/jking10/p/5525519.html)

**HTTP协议即超文本传送协议(Hypertext Transfer Protocol)**。
是Web联网的基础，也是手机联网常用的协议之一，<br>HTTP协议是建立在TCP协议之上的一种应用。


HTTP连接最显著的特点是
**客户端发送的每次请求都需要服务器回送响应**，在请求结束后，会主动释放连接。<br>从建立连接到关闭连接的过程称为“一次连接”。

## 一次连接
1. 在HTTP 1.0中，客户端的每次请求都要求建立一次单独的连接，在处理完本次请求后，就自动释放连接。
2. 在HTTP 1.1中则可以在一次连接中处理多个请求，并且多个请求可以重叠进行，不需要等待一个请求结束后再发送下一个请求。

## 无状态 短连接
- **由于HTTP在每次请求结束后都会主动释放连接**，
HTTP 连接是一种 " ==短连接=="，要保持客户端程序的在线状态，
需要不断地向服务器发起连接请求。<br>
通常的做法是即时不需要获得任何数据，客户端也保持每隔一段固定的时间向服务器发送一次“保持连接”的请求，服务器在收到该请求后对客户端进行回复，表明知道 客户端“**在线**”。<br>若服务器长时间无法收到客户端的请求，则认为客户端“**下线**”，<br>若客户端长时间无法收到服务器的回复，则认为**网络已经断开**。<br><br>

- **http协议是==无状态==的**。
同一个客户端的这次请求和上次请求是没有对应关系，
对http服务器来说，它并不知道这两个请求来自同一个客户端。 
为了解决这个问题， Web程序引入了 **Cookie** 机制来维护状态.

## 状态码
Response 消息中的第一行叫做状态行，
由HTTP协议版本号， 状态码， 状态消息 三部分组成。

状态码用来告诉HTTP客户端,HTTP服务器是否产生了预期的Response.

HTTP/1.1中定义了5类状态码， 状态码由三位数字组成，第一个数字定义了响应的类别

- **1XX**  提示信息
表示请求已被成功接收，继续处理<br><br>

- **2XX**  成功
表示请求已被成功接收，理解，接受<br><br>
- **3XX**  重定向
要完成请求必须进行更进一步的处理<br><br>
- **4XX**  客户端错误 
请求有语法错误或请求无法实现<br><br>
- **5XX**  服务器端错误  
服务器未能实现合法的请求 
-->







