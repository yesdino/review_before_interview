[toc]

---


[原文链接](https://blog.csdn.net/qq_40036754/article/details/102463099)




前言
# 一、nginx简介
## 1. 什么是 nginx 和可以做什么事情
Nginx 是高性能的 HTTP 和反向代理的web服务器，处理高并发能力是十分强大的，能经受高负 载的考验，有报告表明能支持高达 50，000 个并发连接数。

其特点是占有内存少，并发能力强。
事实上nginx的并发能力确实在同类型的网页服务器中表现较好，
中国大陆使用nginx网站用户有：百度、京东、新浪、网易、腾讯、淘宝等。

## 2.Nginx 作为 web 服务器
Nginx 可以作为静态页面的 web 服务器，同时还支持 CGI 协议的动态语言，比如 perl、php 等。
但是不支持 java。Java 程序只能通过与 tomcat 配合完成。

https://lnmp.org/nginx.html

## 3. 正向代理
Nginx 不仅可以做反向代理，实现负载均衡。
还能用作正向代理来进行**上网**等功能。 

正向代理：
如果把局域网外的 Internet 想象成一个巨大的资源库，则局域网中的客户端要访问 Internet，则需要通过**代理服务器**来访问，这种代理服务就称为正向代理。

简单一点：
通过代理服务器来访问服务器的过程 就叫正向代理。
需要在客户端配置代理服务器进行指定网站访问。

## 4. 反向代理
反向代理，其实客户端对代理是无感知的，因为客户端不需要任何配置就可以访问。
我们只需要将请求发送到反向代理服务器，由反向代理服务器去选择目标服务器获取数据后，在返回给客户端，此时反向代理服务器和目标服务器对外就是一个服务器，暴露的是代理服务器地址，隐藏了真实服务器 IP 地址。

### 区别

正向代理与反向代理的区别：
- **正向代理**相对于目标服务器而言**隐藏了客户端**的真实IP地址，
因为对于目标服务器而言所有请求都是从正向代理服务器发出的，
正向代理主要作用：
    - 为了突破网络访问限制，比如科学上网，
    - 还有就是隐藏客户端IP地址。

- **反向代理**对于客户端而言**隐藏了目标服务器**IP地址，
只需要知道代理服务器地址就能访问到目标服务器的资源。
反向代理主要作用：
    - 负载均衡
    - 安全防护

不过，不管正向代理还是反向代理，都能加快客户端的访问速度，因为 nginx 服务器是一个高性能的http web服务器，其能够对代理中的数据作缓冲。

## 5. 负载均衡
增加服务器的数量，然后将请求分发到各个服务器上，将原先请求集中到单个服务器上的情况改为将请求分发到多个服务器上，
**将负载分发到不同的服务器**，也就是我们所说的负载均衡

### 衍生过程 
客户端发送多个请求到服务器，服务器处理请求，有一些可能要与数据库进行交互，服务器处理完毕后，再将结果返回给客户端。

这种架构模式对于早期的系统相对单一，并发请求相对较少的情况下是比较适合的，成本也低。
但是随着信息数量的不断增长，访问量和数据量的飞速增长，以及系统业务的复杂度增加，这种架构会造成服务器相应客户端的请求日益缓慢，并发量特别大的时候，还容易造成服务器直接崩溃。
- **很明显这是由于服务器性能的瓶颈造成的问题，那么如何解决这种情况呢？**

我们首先想到的可能是升级服务器的配置，比如提高 CPU 执行频率，加大内存等提高机器的物理性能来解决此问题。
但是我们知道摩尔定律的日益失效，硬件的性能提升已经不能满足日益提升的需求了。
最明显的一个例子，天猫双十一当天，某个热销商品的瞬时访问量是极其庞大的，那么类似上面的系统架构，将机器都增加到现有的顶级物理配置，都是不能够满足需求的。

- **那么怎么办呢？**

上面的分析我们去掉了增加服务器物理配置来解决问题的办法，也就是说纵向解决问题的办法行不通了，那么横向增加服务器的数量呢？
这时候**集群**的概念产生了，单个服务器解决不了，我们增加服务器的数量，然后将请求分发到各个服务器上，将原先请求集中到单个服务器上的情况改为将请求分发到多个服务器上，将负载分发到不同的服务器，也就是我们所说的负载均衡



## 6. 动静分离
为了加快网站的解析速度，可以把动态页面和静态页面由不同的服务器来解析，加快解析速度。
降低原来单个服务器的压力。


# 二、Nginx 的安装(Linux:centos为例)
nginx 安装时，用到的包，我都准备好啦，方便使用：
https://download.csdn.net/download/qq_40036754/11891855
本来想放百度云的，但是麻烦，所以我就直接上传到我的资源啦，大家也可以直接联系我，我直接给大家的。

1. 准备工作
打开虚拟机，使用finallshell链接Linux操作系统
到nginx下载软件
http://nginx.org/

先安装其依赖软件，最后安装nginx。
依赖工具：pcre-8.3.7.tar.gz，openssl-1.0.1t.tar.gz，zlib-1.2.8.tar.gz，nginx-1.11.1.tar.gz。 我这里也提供下。
2. 开始安装
都有两种方式，一种直接下载，第二种使用解压包方式。这里大多使用解压包方式。
我的安装路径：/usr/feng/
安装pcre
方式一、wget http://downloads.sourceforge.net/project/pcre/pcre/8.37/pcre-8.37.tar.gz 。
方拾二、上传源码压缩包，解压、编译、安装 三部曲。
1）、解压文件，进入pcre目录，
2）、./configure 完成后，
3）、执行命令： make && make install
安装 openssl
下载OpenSSL的地址:
http://distfiles.macports.org/openssl/
1）、解压文件，回到 pcre 目录下，
2）、./configure 完成后，
3）、执行命令： make && make install
安装zlib
1）、解压文件，回到 pcre 目录下，
2）、./configure 完成后，
3）、执行命令： make && make install
安装nginx
1）、解压文件，回到 pcre 目录下，
2）、./configure 完成后，
3）、执行命令： make && make install
3. 运行nginx
安装完nginx后，会在 路径 /usr/local 下nginx 的文件夹。这是自动生成的。
进入这个目录：
cd /usr/local/nginx
1
目录内容如下：


进入sbin文件夹，里面有两个文件：nginx 和 nginx.old。
执行命令：./nginx 即可执行
测试启动： ps -ef | grep nginx

已经启动。
查看nginx默认端口（默认为80），使用网页的形式测试，（像Tomcat一样。）
进入目录查看端口：cd /usr/local/nginx/conf 下的 nginx.conf文件。这个文件也是nginx的配置文件。vim 下：
如下
输入IP:80，则显示：

4. 防火墙问题
在 windows 系统中访问 linux 中 nginx，默认不能访问的，因为防火墙问题 （1）关闭防火墙 （2）开放访问的端口号，80 端口

查看开放的端口号

firewall-cmd --list-all 
1
设置开放的端口号

firewall-cmd --add-service=http –permanent 
firewall-cmd --add-port=80/tcp --permanent 
1
2
重启防火墙

firewall-cmd –reload 
1

# 三、 Nginx 的常用命令和配置文件
## 1. Nginx常用命令
a. 使用nginx操作命令前提
使用nginx操作命令前提：必须进入到nginx的自动生成目录的下/sbin文件夹下。
nginx有两个目录：
第一个：安装目录，我放在：

/usr/feng/
1
第二个：自动生成目录：

/usr/local/nginx/
1
b. 查看 nginx 的版本号
./nginx -v
1


c. 启动 nginx
./nginx
1


d. 关闭nginx
./nginx -s stop
1


e. 重新加载 nginx
在目录：/usr/local/nginx/sbin 下执行命令，不需要重启服务器，自动编译。

./nginx -s reload
1

## 2. Nginx配置文件

### a. 配置文件位置
/usr/local/nginx/conf/nginx.conf


### b. nginx 的组成部分
配置文件中有很多#，开头的表示注释内容，我们去掉所有以 # 开头的段落，精简之后的 内容如下：
```
worker_processes  1;

events {
    worker_connections  1024;
}

http {
    include       mime.types;
    default_type  application/octet-stream;
    sendfile        on;
    keepalive_timeout  65;

    server {
        listen       80;
        server_name  localhost;

        location / {
            root   html;
            index  index.html index.htm;
        }
        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   html;
        }
    }
}
```
nginx 配置文件有三部分组成

#### ① 全局块
从配置文件开始到 events 块**之前**的内容，主要会设置一些影响 nginx 服务器整体运行的配置指令。
主要包括配置运行 Nginx 服务器的用户（组）、允许生成的 worker process 数，进程 PID 存放路径、日志存放路径和类型以及配置文件的引入等。
比如上面第一行配置的：
```
worker_processes  1;
```
这是 Nginx 服务器并发处理服务的关键配置，worker_processes 值越大，可以支持的并发处理量也越多，但是 会受到硬件、软件等设备的制约。


#### ② events 块

events 块涉及的指令主要影响 Nginx 服务器与用户的网络连接。
常用的设置包括是否开启对多 work process 下的网络连接进行序列化，是否允许同时接收多个网络连接，选取哪种事件驱动模型来处理连接请求，每个 word process 可以同时支持的最大连接数等。

比如上面的配置：

```
events {
    worker_connections  1024;
}
```
上述例子就表示每个 work process 支持的最大连接数为 1024.
这部分的配置对 Nginx 的性能影响较大，在实际中应该灵活配置。


#### ③ http 块
```
http {
    include       mime.types;
    default_type  application/octet-stream;
    sendfile        on;
    keepalive_timeout  65;

    server {
        listen       80;
        server_name  localhost;

        location / {
            root   html;
            index  index.html index.htm;
        }
        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   html;
        }
    }
}
```
这算是 Nginx 服务器配置中最频繁的部分，代理、缓存和日志定义等绝大多数功能和第三方模块的配置都在这里。

需要注意的是：
http 块也可以包括 http全局块、server 块。

##### http 全局块
http 全局块配置的指令
包括文件引入、`MIME-TYPE` 定义、日志自定义、连接超时时间、单链接请求数上限等。

##### server 块
这块和虚拟主机有密切关系，虚拟主机从用户角度看，和一台独立的硬件主机是完全一样的，该技术的产生是为了 节省互联网服务器硬件成本。
每个 http 块可以包括多个 server 块，而每个 server 块就相当于一个虚拟主机。
而每个 server 块也分为全局 server 块，以及可以同时包含多个 locaton 块。
全局 server 块
最常见的配置是本虚拟机主机的监听配置和本虚拟主机的名称或IP配置。
location 块
一个 server 块可以配置多个 location 块。

这块的主要作用是基于 Nginx 服务器接收到的请求字符串（例如 server_name/uri-string），对虚拟主机名称 （也可以是IP 别名）之外的字符串（例如 前面的 /uri-string）进行匹配，对特定的请求进行处理。 地址定向、数据缓 存和应答控制等功能，还有许多第三方模块的配置也在这里进行。


# 八、 Nginx 的原理

## 1. mater 和 worker
nginx 启动后，是由两个进程组成的。master（管理者）和worker（工作者）。
一个 nginx 只有一个master,但可以有多个worker.
过来的请求由master管理，worker进行争抢式的方式去获取请求。




## 2. master-workers 的机制的好处
首先，对于每个 worker 进程来说，独立的进程，不需要加锁，所以省掉了锁带来的开销，同时在编程以及问题查找时，也会方便很多。
可以使用 nginx –s reload 热部署，利用 nginx 进行热部署操作
其次，采用独立的进程，可以让互相之间不会影响，一个进程退出后，其它进程还在工作，服务不会中断，master 进程则很快启动新的 worker 进程。当然，worker 进程的异常退出，肯定是程序有 bug 了，异常退出，会导致当 前 worker 上的所有请求失败，不过不会影响到所有请求，所以降低了风险。

## 3. 设置多少个 worker
Nginx 同 redis 类似都采用了 io 多路复用机制，每个 worker 都是一个独立的进程，但每个进程里只有一个主线程。

通过异步非阻塞的方式来处理请求，即使是千上万个请求也不在话下。
每个 worker 的线程可以把一个 cpu 的性能发挥到极致。
所以 worker 数和服务器的 cpu 数相等是最为适宜的。
设少了会浪费 cpu，设多了会造成 cpu 频繁切换上下文带来的损耗。

worker 数和服务器的 cpu 数相等是最为适宜

## 4. 连接数 worker_connection
第一个：发送请求，占用了 woker 的几个连接数？

答案：2 或者 4 个
第二个：nginx 有一个 master，有四个 woker，每个 woker 支持最大的连接数 1024，支持的 最大并发数是多少？

普通的静态访问最大并发数是： worker_connections * worker_processes /2，
而如果是 HTTP 作 为反向代理来说，最大并发数量应该是 worker_connections * worker_processes/4。
这个值是表示每个 worker 进程所能建立连接的最大值，所以，一个 nginx 能建立的最大连接 数，应该是 worker_connections * worker_processes。当然，这里说的是最大连接数，对于 HTTP 请 求 本 地 资 源 来 说 ，能 够 支 持 的 最 大 并 发 数 量 是 worker_connections * worker_processes，如果是支持 http1.1 的浏览器每次访问要占两个连接，所以普通的静态访 问最大并发数是： worker_connections * worker_processes /2，而如果是 HTTP 作 为反向代 理来说，最大并发数量应该是 worker_connections * worker_processes/4。因为作为反向代理服务器，每个并发会建立与客户端的连接和与后端服 务的连接，会占用两个连接。

