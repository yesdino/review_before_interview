[toc]

---


当 django 生产环境中使用 uwsgi + nginx 部署时，由于 uwsgi 不能处理 channal + websocker 请求，所以需要我们改变部署方式。

官方推荐 asgi 服务器 **daphne** 来处理 websocker 请求。

而 daphne 需要我们搭配 supervisor 来使用，supervisor 是由 python 实现的一个进程管理工具，可以确保所管理的进程一直运行，当进程一点中断 supervisord 会自动进行重启。

## 一、daphne

### 安装

已经在上面 requirement 与其他包一起装了

### 测试

测试 dephne 是否能够正常运行
```
daphne -p 8001 devops.asgi:application
```



## 二、supervisor


### 1、安装

已经在上面 requirement 与其他包一起装了

### 2、生成 supervisor 配置文件

（若已经产生过配置文件，则跳过这一步）

这里假设配置文件位置为 `/etc/supervisord.conf`

```
echo_supervisord_conf > /etc/supervisord.conf
```

### 3、将 dephne 配置加入 supervisor 配置文件

```
vim /etc/supervisord.conf
```
将下列配置追加至 `supervisord.conf` 末尾
```
[program:daphne进程名]
directory=/opt/app/devops           # 项目目录
command=daphne -b 127.0.0.1 -p 8001 --proxy-headers devops.asgi:application # 启动命令
autostart=true
autorestart=true
stdout_logfile=/tmp/websocket.log   # 生成日志路径
redirect_stderr=true
```

### 4、启动 supervisord

当所有的配置都添加完毕后，使用配置文件启动 supervisor
```
supervisord -c /etc/supervisord.conf
```

### 5、重新加载 supervisord
每次修改配置文件，都要重新加载使新的修改生效
```
supervisorctl reload
```


### 6、启动或者停止 daphne 单独进程
```
supervisorctl start daphne进程名
supervisorctl stop daphne进程名
```



## 三、修改 nginx 配置

```py
##### 转发配置
upstream wsbackend {
    server 127.0.0.1:8001;  # 端口号必须与 daphne 启动指令中设置的端口号一致
}

###### location配置 /ws 的 url 都会转发到 wsbackend 进程中去处理
location /ws {
    proxy_pass http://wsbackend;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
    proxy_redirect off;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Host $server_name;
}
```






