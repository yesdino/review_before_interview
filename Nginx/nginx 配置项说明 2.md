[出处](https://blog.csdn.net/u014218983/article/details/81217032)

# 问题描述

后台server服务响应时间正常，但是请求没有打到服务器，在nginx很慢才看到error日志，如下：

**upstream timed out (110: Connection timed out) while reading response header from upstream**

```py
2018/07/26 10:17:42 [error] 45762#0: *7489 upstream timed out (110: Connection timed out) while reading response header from upstream, client: 10.2.127.6, server: et_dev.rong360.com, request: “GET /data/names HTTP/1.1”, upstream: “uwsgi://127.0.0.1:8528”, host: “et_dev.rong360.com”, referrer: “http://et_dev.rong360.com/static/html/index.html”
```

## 解决方法

添加或修改nginx反向代理超时时间，如下：

```py
server {
    listen       80;
    server_name  XXX.rong360.com;
    large_client_header_buffers 4 16k;  # 读取大型客户端请求头的缓冲区的最大数量和大小
    client_max_body_size 300m;          # 设置 nginx 能处理的最大请求主体大小。
    client_body_buffer_size 128k;       # 请求主体的缓冲区大小。 
    proxy_connect_timeout 600;
    proxy_read_timeout 600;
    proxy_send_timeout 600;
    proxy_buffer_size 64k;
    proxy_buffers   4 32k;
    proxy_busy_buffers_size 64k;
    proxy_temp_file_write_size 64k;
    ……
    location / {
        uwsgi_send_timeout 600;         # 指定向 uWSGI 传送请求的超时时间，完成握手后向 uWSGI 传送请求的超时时间。
        uwsgi_connect_timeout 600;      # 指定连接到后端 uWSGI 的超时时间。
        uwsgi_read_timeout 600;         # 指定接收 uWSGI 应答的超时时间，完成握手后接收uWSGI应答的超时时间。
        ……
    }
```

## 提高 nginx 网络吞吐量 buffers 优化指令说明

- **large_client_header_buffers**
此指令规定了用于读取大型客户端请求头的缓冲区的最大数量和大小。 这些缓冲区仅在缺省缓冲区不足时按需分配。 当处理请求或连接转换到保持活动状态时，释放缓冲区。<br><br>

- **client_max_body_size**
此指令设置`NGINX`能处理的最大请求主体大小。 如果请求大于指定的大小，则`NGINX`发回HTTP 413（Request Entity too large）错误。 如果服务器处理大文件上传，则该指令非常重要。<br><br>

- **client_body_buffer_size**
此指令设置用于请求主体的缓冲区大小。 如果主体超过缓冲区大小，则完整主体或其一部分将写入临时文件。 如果`NGINX`配置为使用文件而不是内存缓冲区，则该指令会被忽略。 默认情况下，该指令为32位系统设置一个8k缓冲区，为64位系统设置一个16k缓冲区。 该指令在 `NGINX` 配置的http，server和location区块使用。<br><br>

## nginx代理超时配置
- **proxy_connect_timeout**
默认值60s, nginx连接到后端服务器的连接超时时间，发起握手等候响应超时时间。<br><br>

- **proxy_read_timeout**
连接成功后，等候后端服务器响应时间。其实已经进入后端的排队之中等候处理（也可以说是后端服务器处理请求的时间）。<br><br>

- **proxy_send_timeout**
后端服务器数据回传时间，就是在规定时间之内后端服务器必须传完所有的数据。
注：nginx使用proxy模块时，默认的读取超时时间是60s。<br><br>

## nginx缓存区大小设置

- **proxy_buffer_size**
nginx可从服务器一次接收的最大数据大小<br><br>

- **proxy_buffers**
该指令设置缓冲区的大小和数量,从被代理的后端服务器取得的响应内容,会放置到这里. 默认情况下,一个缓冲区的大小等于内存页面大小,可能是4K也可能是8K,这取决于平台。<br><br>

- **proxy_busy_buffers_size**
proxy_busy_buffers_size不是独立的空间，他是proxy_buffers和proxy_buffer_size的一部分。nginx会在没有完全读完后端响应的时候就开始向客户端传送数据，所以它会划出一部分缓冲区来专门向客户端传送数据(这部分的大小是由proxy_busy_buffers_size来控制的，建议为proxy_buffers中单个缓冲区大小的2倍)，然后它继续从后端取数据，缓冲区满了之后就写到磁盘的临时文件中。<br><br>

- **proxy_max_temp_file_size** 和 **proxy_temp_file_write_size**
临时文件由 `proxy_max_temp_file_size` 和 `proxy_temp_file_write_size` 这两个指令决定。 
`proxy_temp_file_write_size` 是一次访问能写入的临时文件的大小，默认是 `proxy_buffer_size` 和 `proxy_buffers` 中设置的缓冲区大小的2倍，Linux 下一般是8k。
`proxy_max_temp_file_size` 指定当响应内容大于 proxy_buffers 指定的缓冲区时, 写入硬盘的临时文件的大小. 如果超过了这个值, Nginx将与Proxy服务器同步的传递内容, 而不再缓冲到硬盘. 设置为0时, 则直接关闭硬盘缓冲.<br><br>

## 示例
```py
    proxy_buffer_size 4k;   # 设置代理服务器（nginx）保存用户头信息的缓冲区大小
    proxy_buffers 4 32k;    # proxy_buffers缓冲区，网页平均在32k以下的设置
    proxy_busy_buffers_size 64k;    # 高负荷下缓冲大小（proxy_buffers*2）
    proxy_temp_file_write_size 64k; # 设定缓存文件夹大小，大于这个值，将从upstream服务器传
```