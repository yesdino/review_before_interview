# 目录

[toc]


---

# Nginx


## nginx 启动

[link 00:00](https://www.bilibili.com/video/BV1zE411N7m9?p=6)
1、普通启动
切换到 nginx 安装目的 sbin 目录下，执行：：
```html
./nginx
```

2、通过配置文件启动
`/nginx -c /usr/local/nginx/conf/nginx.conf`
或
`/usr/local/nginx/sbin/nginx -c /usr/local/nginx/conf/nginx.conf`(绝对路径 推荐)


3、检查 Nginx是否启动
通过查看进程：
`ps -ef | grep nginx`

<img 
src="https://upload-images.jianshu.io/upload_images/11876740-8d1827a4e65e3bc7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240">
</img>


**nginx 体系结构由 master 进程和其 worker 进程组成**
- **master** ：主进程。读取 config 配置文件，并维加 worker 进程，
- **worker** ：子进程。对请求进行实际处理；


## nginx 关闭

[link 00:00](https://www.bilibili.com/video/BV1zE411N7m9?p=7)



## nginx 配置文件

[link 00:00](https://www.bilibili.com/video/BV1zE411N7m9?p=10)

Nginx 的核心配置文件主要由三个部分构成：
- 基本配置
- **`events`** 配置
- **`http`** 配置


### 基本配置

[link 02:49](https://www.bilibili.com/video/BV1zE411N7m9?p=10)

```py
user root;              # 运行用户
worker_processes  1;    # 启动进程, 通常设置成和 cpu 的数量相等

error_log  /var/log/nginx/error.log;    
pid        /var/run/nginx.pid;          # 全局错误日志及PID文件
```

### events 配置
 
[link 00:00](https://www.bilibili.com/video/BV1zE411N7m9?p=11)
配置工作模式和连接数

```py
# 工作模式及连接数上限
events {
    # use   epoll;              # 使用 epoll 事件模型（epoll 是多路复用 IO (I/O Multiplexing) 中的一种方式 , 但是仅用于 linux2.6 以上内核 , 可以大大提高 nginx 的性能
    worker_connections  1024;   # 单个 worker process 进程的在接数上限
    #  multi_accept on; 
}
```
 

### http 配置

- **http 内 server 外：**

[link 00:00](https://www.bilibili.com/video/BV1zE411N7m9?p=12)

```py
# 设定 http 服务器，利用它的反向代理功能提供负载均衡支持
http {
    
    include       /etc/nginx/mime.types;        # 设定 nginx 支持哪些多媒体类型, 类型由 mime.type 文件定义
    default_type  application/octet-stream;
    
    access_log    /var/log/nginx/access.log;    # 设定日志格式

    # sendfile 指令指定 nginx 是否调用 sendfile 函数（ zero copy 方式）来输出文件，对于普通应用，
    # 必须设为 on, 如果用来进行下载等应用磁盘 IO 重负载应用，可设置为 off ，以平衡磁盘与网络 I/O 处理速度，降低系统的 uptime.
    sendfile        on;
    # tcp_nopush     on;

    keepalive_timeout  65;  # 连接超时时间
    tcp_nodelay        on;
    
    
    gzip  on;               # 开启 gzip 压缩
    gzip_disable "MSIE [1-6]\.(?!.*SV1)";

    # 设定请求缓冲
    client_header_buffer_size    1k;
    large_client_header_buffers  4 4k;

    include /etc/nginx/conf.d/*.conf;
    include /etc/nginx/sites-enabled/*;

    # 设定负载均衡的服务器列表
    upstream mysvr {
        # weigth 参数表示权值，权值越高被分配到的几率越大
        # 本机上的 Squid 开启 3128 端口
        server 192.168.8.1:3128 weight=5;
        server 192.168.8.2:80  weight=1;
        server 192.168.8.3:80  weight=6;
    }

    server {
        ......
    }
    server {
        ......
    }
}
```

- **server 内**

[link 00:00](https://www.bilibili.com/video/BV1zE411N7m9?p=13)




# nginx 部署

## 直接部署静态网站

[link 00:00](https://www.bilibili.com/video/BV1zE411N7m9?p=15)


### **location 路由映射规则**

[link 07:25](https://www.bilibili.com/video/BV1zE411N7m9?p=15)

`ip + port` = `root`后面的路径



## 负载均衡


- **负载均衡概述**
[00:00](https://www.bilibili.com/video/BV1zE411N7m9?p=16)
 

- 负载均衡实现方式
  - 硬件负载均衡
  - 软件负载均衡

**硬件负载均衡**

[03:55](https://www.bilibili.com/video/BV1zE411N7m9?p=16)

其实就是一台将服务分发出去，实现负载均衡的机器，外面出售的。
知名一点的 比如 **F5**、**深信服**、**Array** 等
<img 
src="https://upload-images.jianshu.io/upload_images/11876740-baf916ce2b280fed.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240">
</img>
**优点** 是有厂商专业的技术服务团队提供支持，性能稳定；
**缺点** 是费用昂贵，对于规模较小的网络应用成本太高；
<br>

**软件负载均衡**

比如 **`Nginx`**、**`LVS`**、 **`Haproxy`** 等
优点是免费开源，成本低廉；


### nginx 实现负载均衡
[00:00](https://www.bilibili.com/video/BV1zE411N7m9?p=17)




















<br>
<br><br><br><br><br><br><br><br><br><br><br><br>