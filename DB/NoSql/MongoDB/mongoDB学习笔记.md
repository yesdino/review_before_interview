
[toc]


---

<!-- # 安装 mongodb 记录 -->

## 下载安装 MongoDB


参考：[link](https://www.runoob.com/mongodb/mongodb-linux-install.html)

首先确定安装路径为：`/usr/local/mongodb`
- 下载安装
```
# 进入存放安装包的路径
curl -O https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-3.0.6.tgz     # 下载
tar -zxvf mongodb-linux-x86_64-3.0.6.tgz                                    # 解压
mv mongodb-linux-x86_64-3.0.6/ /usr/local/mongodb                           # 将解压包拷贝到安装目录
```

- 进入安装目录，创建数据库目录
```
cd /usr/local/mongodb
mkdir -p /data/db
```
此时数据库目录为 `/usr/local/mongodb/data/db`

- 进入 MongoDB bin 目录，运行测试是否能正常运行
```
cd /usr/local/mongodb/bin
./mongod
```
中间出现 **exception: connect failed**
原因是未指定数据库位置
```
./mongod --dbpath /data/db
```
启动 MongoDB 成功

- 另开一个终端连接 MongoDB
```
cd /usr/local/mongodb/bin
./mongo
...
...
> 3+3
6
>
```
出现 `>` shell 界面则表示 MongoDB 正常启动，仍出现**exception: connect failed** 表示启动失败，需另找原因

<br>

## 后台启动 MongoDB

### 创建 MongoDB 启动配置项文件
```
[root@localhost system]# cd /usr/local/mongodb/bin
[root@localhost bin]# touch mongodb.conf
[root@localhost bin]# vim mongodb.conf

port=27017
dbpath=/usr/local/mongodb/data/db
logpath=/usr/local/mongodb/bin/mongodb.log
logappend=true
fork=true
```
注意上述配置项含义：
```
port = 端口号
dbpath= MongoDB 数据库文件夹路径
logpath = 后台启动产生的 log 文件路径
logappend = log 是否追加
fork = 后台启动，这个一定要加
```
注意上述配置项路径错误将导致启动失败
<br>

### 创建 system 后台启动文件
```
[root@localhost bin]# cd /lib/systemd/system
[root@localhost bin]# vi mongodb.service
```

```
[Unit]  
Description=mongodb
After=network.target remote-fs.target nss-lookup.target
  
[Service]
Type=forking
RuntimeDirectory=mongodb
RuntimeDirectoryMode=0751
# PIDFile=/var/run/mongodb/mongod.pid
ExecStart=/usr/local/mongodb/bin/mongod --config /usr/local/mongodb/bin/mongodb.conf
ExecStop=/usr/local/mongodb/bin/mongod --shutdown --config /usr/local/mongodb/bin/mongodb.conf  
PrivateTmp=false  
  
[Install]  
WantedBy=multi-user.target
```

后台启动，开机启动
```
[root@localhost bin]# system start mongodb.service
[root@localhost bin]# system enable mongodb.service
```

查看状态
```
[root@localhost bin]# system status mongodb.service
â— mongodb.service - mongodb
   Loaded: loaded (/usr/lib/systemd/system/mongodb.service; enabled; vendor preset: disabled)
   Active: active (running) since Mon 2019-10-07 16:06:04 CST; 10s ago
  Process: 6752 ExecStart=/usr/local/mongodb/bin/mongod --config /usr/local/mongodb/bin/mongodb.conf (code=exited, status=0/SUCCESS)
 Main PID: 6756 (mongod)
    Tasks: 11
   CGroup: /system.slice/mongodb.service
           â””â”€6756 /usr/local/mongodb/bin/mongod --config /usr/local/mongodb/bin/mongodb.conf

Oct 07 16:06:03 localhost.localdomain systemd[1]: Starting mongodb...
Oct 07 16:06:03 localhost.localdomain mongod[6752]: about to fork child process, waiting until server is ready for connections.
Oct 07 16:06:03 localhost.localdomain mongod[6752]: forked process: 6756
Oct 07 16:06:04 localhost.localdomain mongod[6752]: child process started successfully, parent exiting
Oct 07 16:06:04 localhost.localdomain systemd[1]: Started mongodb.
```
<br>


## 中间遇到的坑 
**mongodb进程莫名退出**
现象：启动了一段时间之后自己关闭 mongodb 进程

查看 log 
```
2019-10-07T15:53:28.632+0800 I NETWORK  [initandlisten] waiting for connections on port 27017
2019-10-07T15:54:58.494+0800 I CONTROL  [signalProcessingThread] got signal 15 (Terminated), will terminate after current cmd ends
2019-10-07T15:54:58.494+0800 I CONTROL  [signalProcessingThread] now exiting
2019-10-07T15:54:58.494+0800 I NETWORK  [signalProcessingThread] shutdown: going to close listening sockets...
2019-10-07T15:54:58.494+0800 I NETWORK  [signalProcessingThread] closing listening socket: 6
2019-10-07T15:54:58.494+0800 I NETWORK  [signalProcessingThread] closing listening socket: 7
2019-10-07T15:54:58.494+0800 I NETWORK  [signalProcessingThread] removing socket file: /tmp/mongodb-27017.sock
2019-10-07T15:54:58.494+0800 I NETWORK  [signalProcessingThread] shutdown: going to flush diaglog...
2019-10-07T15:54:58.494+0800 I NETWORK  [signalProcessingThread] shutdown: going to close sockets...
2019-10-07T15:54:58.494+0800 I STORAGE  [signalProcessingThread] shutdown: waiting for fs preallocator...
2019-10-07T15:54:58.494+0800 I STORAGE  [signalProcessingThread] shutdown: final commit...
2019-10-07T15:54:58.506+0800 I JOURNAL  [signalProcessingThread] journalCleanup...
2019-10-07T15:54:58.506+0800 I JOURNAL  [signalProcessingThread] removeJournalFiles
2019-10-07T15:54:58.507+0800 I JOURNAL  [signalProcessingThread] Terminating durability thread ...
2019-10-07T15:54:58.605+0800 I JOURNAL  [journal writer] Journal writer thread stopped
2019-10-07T15:54:58.605+0800 I JOURNAL  [durability] Durability thread stopped
2019-10-07T15:54:58.605+0800 I STORAGE  [signalProcessingThread] shutdown: closing all files...
2019-10-07T15:54:58.605+0800 I STORAGE  [signalProcessingThread] closeAllFiles() finished
2019-10-07T15:54:58.605+0800 I STORAGE  [signalProcessingThread] shutdown: removing fs lock...
2019-10-07T15:54:58.605+0800 I CONTROL  [signalProcessingThread] dbexit:  rc: 0
```
但是把 systemctl stop 掉重新 start 注意到
```
root@instance-tbbjrcnc:~# systemctl status mongodb.service
?.mongodb.service - mongodb
   Loaded: loaded (/lib/systemd/system/mongodb.service; enabled; vendor preset: enabled)
   Active: failed (Result: timeout) since Tue 2019-08-13 10:32:22 CST; 8s ago
  Process: 23145 ExecStart=/usr/bin/mongod --config /etc/mongod.conf --fork (code=exited, status=0/SUCCESS)
      CPU: 716ms
 
Aug 13 10:30:52 instance-tbbjrcnc systemd[1]: Starting mongodb...
Aug 13 10:30:52 instance-tbbjrcnc mongod[23145]: 2019-08-13T10:30:52.295+0800 I STORAGE  [main] Max cache overflow file size custom option: 0
Aug 13 10:30:52 instance-tbbjrcnc mongod[23145]: about to fork child process, waiting until server is ready for connections.
Aug 13 10:30:52 instance-tbbjrcnc mongod[23145]: forked process: 23147
Aug 13 10:30:52 instance-tbbjrcnc mongod[23145]: child process started successfully, parent exiting
Aug 13 10:30:52 instance-tbbjrcnc systemd[1]: mongodb.service: PID file /var/run/mongodb/mongod.pid not readable (yet?) after start: No such file or directory
Aug 13 10:32:22 instance-tbbjrcnc systemd[1]: mongodb.service: Start operation timed out. Terminating.
Aug 13 10:32:22 instance-tbbjrcnc systemd[1]: Failed to start mongodb.
Aug 13 10:32:22 instance-tbbjrcnc systemd[1]: mongodb.service: Unit entered failed state.
Aug 13 10:32:22 instance-tbbjrcnc systemd[1]: mongodb.service: Failed with result 'timeout'.
```
报错
```
mongodb.service: PID file /var/run/mongodb/mongod.pid not readable (yet?) after start: No such file or directory
```
没有 `/var/run/mongodb/mongod.pid` 这个文件
由于赶时间后面直接注释掉 `mongodb.service` 文件中的 pid 文件配置

```
[Service]
...
# PIDFile=/var/run/mongodb/mongod.pid
...
```
设置 `mongodb.service` 文件权限

```
chmod 754 mongodb.service
```
重新启动，搞定！



---

参考：
[Linux平台安装MongoDB](https://www.runoob.com/mongodb/mongodb-linux-install.html)
[mongoDB服务启动失败（exception: connect failed）](https://blog.csdn.net/leisure_life/article/details/78580630)
[Linux安装mongodb总结](https://www.cnblogs.com/Lovebugs/p/8606000.html)
