[引用](https://blog.csdn.net/t8116189520/article/details/88388801)
```py
# 启动主进程，来管理其他进程，其它的uwsgi进程都是这个master进程的子进程，如果kill这个master进程，相当于重启所有的uwsgi进程。
master = true 

# 在app加载前切换到当前目录， 指定运行目录
chdir = /web/www/mysite

# 加载一个WSGI模块,这里加载mysite/wsgi.py这个模块
module = mysite.wsgi 

# 监控python模块mtime来触发重载 (只在开发时使用)
py-autoreload=1

# 在每个worker而不是master中加载应用
lazy-apps=true  

# 指定socket文件，也可以指定为127.0.0.1:9000，这样就会监听到网络套接字
socket = /test/myapp.sock 

# 启动2个工作进程，生成指定数目的worker/进程
processes = 2

# 设置用于uwsgi包解析的内部缓存区大小为64k。默认是4k。
buffer-size = 32768

# 使进程在后台运行，并将日志打到指定的日志文件或者udp服务器
daemonize = /var/log/myapp_uwsgi.log 

# 以固定的文件大小（单位KB），切割日志文件。 例如：log-maxsize = 50000000  就是50M一个日志文件。一旦超过设定大小将切割生成新的日志文件，新文件名在原始文件名的基础上扩展名被替换为时间戳
log-maxsize = 5000000

# 禁用请求日志记录
disable-logging = true 

# 当服务器退出的时候自动删除 unix socket 文件和 pid 文件。
vacuum = true 

# 设置socket的监听队列大小（默认：100）
listen = 120 

# 指定pid文件 记录主进程的pid号。
pidfile = /var/run/uwsgi.pid 

# 允许用内嵌的语言启动线程。这将允许你在app程序中产生一个子线程
enable-threads = true 

# 设置在平滑的重启（直到接收到的请求处理完才重启）一个工作子进程中，等待这个工作结束的最长秒数。这个配置会使在平滑地重启工作子进程中，如果工作进程结束时间超过了8秒就会被强行结束（忽略之前已经接收到的请求而直接结束）
reload-mercy = 8 

# 为每个工作进程设置请求数的上限。当一个工作进程处理的请求数达到这个值，那么该工作进程就会被回收重用（重启）。你可以使用这个选项来默默地对抗内存泄漏
max-requests = 5000 

# 通过使用POSIX/UNIX的setrlimit()函数来限制每个uWSGI进程的虚拟内存使用数。这个配置会限制uWSGI的进程占用虚拟内存不超过256M。如果虚拟内存已经达到256M，并继续申请虚拟内存则会使程序报内存错误，本次的http请求将返回500错误。
limit-as = 256 

# 一个请求花费的时间超过了这个harakiri超时时间，那么这个请求都会被丢弃，并且当前处理这个请求的工作进程会被回收再利用（即重启）
harakiri = 60 
```

下面是项目中常用的 uwsgi.ini 配置
```ini
[uwsgi]
; project dir
chdir = /home/hugin/hugin/tracking_management/tracking_management/
; sock file path. must match nginx's port if use nginx
socket = 127.0.0.1:8400
wsgi-file = tracking_management/wsgi.py
processes = 2
threads = 1
stats = 127.0.0.1:8401
uid = hugin
gid = hugin
; a master process will respawn your processes when they die.
master = true
enable-threads = true
; reload whenever this config file changes
; %p is the full path of the current config file
touch-reload = %p
pidfile = tracking_management_uwsgi.pid
daemonize = tracking_management_uwsgi.log
; max size 50000000 -> 50m
log-maxsize = 50000000 
http-websockets = true
; websocket
async = 30
ugreen = ''
http-timeout = 300
```
