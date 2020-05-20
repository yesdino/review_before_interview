[toc]

---

# docker 

[网址](https://www.bilibili.com/video/av27122140)

## docker 三要素

###  镜像（image）
- **镜像就是一个==模板==**，是容器实例化的基础。
- 一个镜像可以创建多个容器
- 镜像只读


### 容器（container）
- **容器就是用镜像创建的==运行实例化==**，相当于**集装箱**。
- 容器是一个 ==**运行环境**==。可以启动、停止、删除
- 容器之间相互隔离，平台安全
- 容器可看做是一个简易版的linux环境(有用户权限、进程、网络等空间)和运行在其中的应用程序
- 容器的定义与镜像几乎一致（因为容器就是从镜像开的）

### 仓库（repository）

- 集中存放镜像文件的地方
- **仓库注册服务器**(Registry)上存放着多个仓库，每个仓库有包含多个镜像，每个镜像有不同的标签
- 仓库分为公开库、私有库。最大的公开库为Docker Hub(慢）,国内公开库有阿里云、网易云


## docker 安装
```py
# 安装依赖
yum install -y epel-release
# 安装 docker
yum install -y docker-io
# 安装后的配置文件位置
/etc/sys
```

## 安装完 docker 之后替换仓库源

由于 docker hub 是国外的服务器，访问下载非常慢，国内阿里云、网易云已经将镜像拷贝到了他们的服务器上可以免费拉下来，所以替换仓库源非常有必要,这里以阿里云为例：

- 1、登录阿里云仓库

- 2、到控制台那里去复制上面提示的国内镜像地址。我的地址：`https://d6reefsh.mirror.aliyuncs.com`

- 3、把地址写入 docker 的配置文件中去

```
vim /etc/docker/daemon.json
```

```
{
    "registry-mirrors": [https://d6reefsh.mirror.aliyuncs.com]
}
```
- 4、重启 docker

```
systemctl daemon-reload
systemctl restart docker
```
![阿里云镜像仓库.png](https://upload-images.jianshu.io/upload_images/11876740-85cd31b5bdd2c5bd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


## docker run
安装完 docker 之后，直接输入下面一条 docker run 指令：

```
docker run hello-world
```


docker run 后面跟的是容器，即要跑哪个容器。那么 docker 接到 run 指令之后内部都做了哪些动作呢？

- 1、找有没有这个容器。若有，然后跑起来
- 2、若没有，找有没有这个容器的镜像。若有，实例化成容器然后跑起来
- 3、若镜像也没有，到设定的仓库上找有没有这个镜像。若有，拉下来、实例化成容器、跑容器
- 4、若仓库里面都没有这个镜像，报错

![docker_run_工作流程.png](https://upload-images.jianshu.io/upload_images/11876740-4c888c0a94b047c1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![docker_run.png](https://upload-images.jianshu.io/upload_images/11876740-c7a5c17fa8cc5f2c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## docker 是怎么工作的

[link](https://www.bilibili.com/video/av27122140?p=11)


docker 是一个 ==Client-Server== 结构的系统。

docker 守护进程 docker-daemon 运行在主机上，<u>**docker-daemon 通过 ==Socket== 连接从客户端接收命令并管理运行在主机上的容器**</u>

### docker 架构
![image](https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1578069293898&di=9f16d7ec562fa59361b62de054f9b143&imgtype=0&src=http%3A%2F%2Fimg1.mukewang.com%2F5b783ab700016b6a08840463.jpg)

看右上角的蓝色鲸鱼，鲸鱼背上有集装箱

```py
蓝色的大海  ：宿主机 (centos)
鲸鱼        ：docker
集装箱      ：容器 （form 镜像）
```



## docker 为什么比虚拟机快

- 1、**docker 不需要实现硬件资源**

docker 有比虚拟机更少的抽象层，由于 docker 不需要 Hypervisor 实现硬件资源虚拟化，运行在 docker 容器上的程序直接使用的都是实际物理机的硬件资源。

因此，在 CPU、内存利用率上 docker 将会在效率上有明显优势

- 2、**docker 利用的宿主机的内核，不需要加载操作系统的内核**

由于其不需要加载内核，因此，在新建一个容器时，docker 不再需要和虚拟机一样加载一个操作系统的内核。避免引寻、加载操作系统内核是个比较费时费力的过程。虚拟机加载 Guest OS，这个新建过程是分钟级别的。而 docker 由于直接利用宿主机的操作系统，省略了这个过程，因此新建一个 docker 容器只需要几秒之。


![docker为什么比VM快1.png](https://upload-images.jianshu.io/upload_images/11876740-db6d82de12f61bbb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![docker与VM的不同.png](https://upload-images.jianshu.io/upload_images/11876740-331e7adf2de54fed.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## docker 常用命令

### 帮助命令

打印 docker 版本信息
```
docker version
```
打印 docker 基本信息，包括 image 数量，container 数量等等
```
docker info
```
指令用法查询
```
docker --help
```

### 镜像命令

#### docker images
```
docker images
docker images -a    # 将所有镜像显示出来，包括底层未加外层的镜像
docker images -q    # 只显示当前镜像的 ID
docker images -qa   # 组合使用 显示当前所有镜像的 ID(可用这个指令得到批量ID传到别的地方进行批量操作)

docker images --digests   # 显示镜像的摘要信息（有点类似于备注
docker images --no-trunc  # 显示完整的镜像信息（哈希值ID也会是完整的
```

#### docker search
注意搜索的话只会用 docker hub 上面查，至于拉取的话会在你设置的那个仓库上面拉
```
docker search [image]
docker search -s [number] [image] # -s : 要求大于设置的 start 数
docker search --no-trunc [image]  # --no-trunc : 搜索结果中显示镜像的完整信息（带有完整的 Decription 信息
docker search --automates [image] # --automates : 要求是自动构建的镜像类型（AUTO MATED->[OK]
```

#### docker pull
下载镜像。
```
docker pull [image]:[tag]
```
如果 tag 不写，**默认 tag 为 lastest**
`docker pull [image]` 等于 `docker pull [image]:lastest`

#### docker rmi
删除镜像。注意不能删除正在 run 的容器，如果非要删正在 run 的，需要强制删除

```
docker rmi [image]:[tag]

docker rmi -f [image]:[tag]               # 强制删除
docker rmi -f [img1]:[tag] [img2]:[tag]   # 删除多个
docker rmi -f $(docker image -qa)         # 全部删除, 将括号内得到的所有镜像ID做为参数给删除指令
```

### 容器指令 1

#### docker run

```
[option]常用参数
--name='容器新名字' :为容器指定一个新的别名, 如果不给容器名，则自动生成一个容器名给你
-d                  :后台运行容器，不占用前台终端
-i                  :以交互模式运行容器，通常与 -t 配合使用
-t                  :为容器重新分配一个伪输入终端，通常与 -i 配合使用
-P                  :(大写)随机端口映射
-p                  :(小写)指定端口映射，有下面几种格式
                        ip:hostPort:containerPort
                        ip::containerPort
                        hostPort:containerPort
                        containerPort
```
`-it` 进入容器终端环境
![run_it进入容器终端环境.png](https://upload-images.jianshu.io/upload_images/11876740-8dce50936e183188.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)



注意：
```
docker run -it centos 
等价于
docker run -it centos /bin/bash
```
`/bin/bash`是默认的，表示当你进入容器的时候，打开 shell 终端，以 shell 终端的形式进程交互

##### 指定端口 -p/-P

```
docker run -it -p [containerID]

-p  :指定端口，格式：-p [主机端口]:[docker容器端口]
-P  : 随机分配端口
```

例：`docker run -it -p 8888:8080 tomcat`：启动之后，浏览器访问 `hostIP:8888` 能访问到 tomcat 页面。
即第一个是对外暴露的端口，第二个是容器内部映射过去的端口

例：`docker run -it -P tomcat` 用 `docker ps` 查到分配端口号 32768
启动之后，浏览器访问 `hostIP:32768` 能访问到 tomcat 页面


#### docker ps
查看 docker 正在运行的容器
```
docker ps   
```
![docker_ps_参数说明.png](https://upload-images.jianshu.io/upload_images/11876740-87efb53bf68b894a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


#### 退出容器

两种方式
- exit  : 容器停止退出
- Ctrl+P+Q  : 容器不停止退出

#### 启动容器 start
```
docker start [image]
```

#### 重启容器 restart
```
docker restart [image]
```

#### 容器关闭 stop/kill
```
docker stop [image]
```
正常关闭，相当于点关机一样等他慢慢关闭


```
docker kill [image]
```
强制关闭，非正常情况下，不等他慢慢关闭，直接拔电源一样


#### 容器删除 rm
注意删除指令 容器是`rm` 镜像`rmi`
```
docker rm [image]     # 正常删除容器
docker rm -f [image]  # 强制删除容器，如果容器正在 run, 关闭了再删除
```

一次删除多个容器
```
docker rm -f $(docker ps -a -q)
docker ps -a -q | xargs docker rm
```



### **容器指令 2**

#### 后台进程模式启动容器 -d

使用 -d 参数
```
docker run -d [containerID]   # 返回一串哈希值
```
这时候你如果用 `docker ps` 查看会发现 ==返回的哈希值没有在 docker 的进程中==，容器已经退出

- **为什么呢？**
这是 docker 的一个机制：==docker 容器要后台运行，就必须有一个前台进程==
用 -d 指令启动是启动一个后台进程应用，但是前台没有与之交互的应用的情况下，docker 就会认为这个进程不再需要，会自动关闭这个进程，

- **解决方案**
    - 将你要运行的程序以 `-it` 前台进程的形式运行
    - 加入你的容器会一直在 run,不断的打印 log 信息这样它也不会自动关闭，比如 uwsgi 这类，不行它运行的时候打印出一堆日志的话，直接后台 run 就可以了


#### 查看容器日志 logs

```
docker logs -f -t --tail [containerID]

-t      : 加入时间戳
-f      : 不截断 自动实时在终端打印新增加的日志
--tail  : +数字 显示最后多少条
```
如果用上面的指令：
```
# 双引号内为 shell 脚本指令
docker run -d centos /bin/sh -c "while true;do echo hello zzyy;sleep 2;done"
```
在容器内会每隔 2s 打印一句 log ，可以用 `docker logs` 加上不同的参数查看 log 打印情况

#### 查看容器内部运行的进程 top
注意是容器里面的进程，不是 docker 的容器进程
```
docker top [containerID]
```

#### 查看容器内部的细节 inspect
以 **json** 串的格式告诉你这个容器的全部信息、实现细节
```
docker inspect [containerID]
```

#### 进入正在运行的容器并以命令行交互 exec/attach

```
1. 直接进入容器启动命令的终端，不会启动新的进程
docker exec -it [containerID] bashShell

2. 在容器中打开新的终端，并且可以启动新的进程
docker attach [containerID]
```
两者的区别
- **attach** 是先进入容器，要做什么做什么
- **exec** 可以进入容器之后拿结果，可以不进入容器直接返回结果
    - `docker exec -t [containerID] ls -l /tmp` : 容器后面跟指令，不进入直接返回结果
    - `docker exec -t [containerID] /bin/bash` : 容器后面不跟指令，进入容器（`/bin/bash`可加可不加）




#### 从容器内部拷贝文件到主机上
```
docker cp [containerID]:容器内路径 宿主机路径
```

---

## **docker 镜像详解**
==镜像就是千层饼 一层套一层==

### 镜像本质（是什么）

- 镜像是一种 **轻量级**、**可执行**的独立软件包。
- 用来 ==**打包软件运行环境**和基于运行环境开发== 的软件。
- 它包含某个软件所需的所有内容，包括代码、运行库、环境变量和配置文件

#### 1、联合文件系统 UnionFS

Union 文件系统 (UnionFS) 是一种分层的、轻量级并且高性能的文件系统。
它**支持对文件系统的修改作为一次提交来进行一层层的叠加**，同时<u>可以将不同的目录挂载到一个虚拟文件系统</u>(unite several directories into a single virtual filesystem)。

<u>Union 文件系统是 docker 镜像的基础。</u>（即 docker 镜像底层原理是 Union 文件系统）

镜像可以通过分层来进行**继承**，基于（没有父镜像的）基础镜像，可以制作各种具体的应用镜像

特性：
- **一次同时加载多个文件系统，但从外面看，只看到一个文件系统。**
- ==联合加载会把各层文件叠加起来，这样最终的文件系统会包含所有底层的文件和目录，形成一个的镜像来对外==。

(当你`pull image`的时候就可以看到两个以上的哈希值 **Pull complete**，这就是内部的层)

<br>

#### 2、镜像加载原理

==docker 的镜像实际上是由一层一层的文件系统组成==。称为联合文件系统 UnionFS。

- **bootfs**
bootfs (boot file system) 主要包含 bootloader 和 kernel。
bootloader 主要引导加载 kernel，linux 刚启动时会加载 bootfs 文件系统，==在 docker 镜像最底层是 bootfs==。
bootfs 这一层和我们典型的 linux/Unix 系统一样，包含 boot加载器和内核。
当 boot 加载完成之后整个内核就都在内存中了，此时内存的使用权由 bootfs 转交给内核，此时系统就会卸载 bootfs。

- **rootfs**
rootfs (root file system), 在 bootfs 之上，包含的就是典型的 linux 系统中的 /dev, /proc, /bin, /etc 等标准目录和文件。
rootfs 就是各种不同的 **操作系统发行版**，如 Ubuntu，centos 等
<br>




#### 3、分层的镜像

- **为什么 docker 的 centos 才 200M ？**
注意一个系统的组成，底层是 bootfs, 上层是发行类型(Ubuntu/centos)。而在 docker 中，bootfs 直接用宿主机的 kernel，docker 只需要提供特定类型的 rootfs 就行了。即原因是因为其==共用内核==。

- **为什么 docker 的 tomcat 才 400多M ？**
因为每一个镜像都是一个迷你 linux 系统，
它在底层都包了 linux 系统的基础上才会继续包你所需要的包所需要叠加的层，而 tomcat 底层的结构如下：
    ```
    ---------------
    |  tomcat        
    ---------------
    |  idk8      
    ---------------
    |  centos      
    ---------------
    |  kernel            
    ---------------
    ```
    上面这么多层对外表现为一个 tomcat 镜像，所以有 400 多m

<br>

#### 4、为什么采用镜像分层？

为了==共享资源==，共用 base 镜像，这也是最大的好处

如：多个镜像都从相同的 base 镜像构建而来，宿主机只需要在磁盘上保险一份 base 镜像，同时内存中只需加载一份 base 镜像，就**可为所有容器服务**了，每一个容器都可以共享 base 镜像

感受就是：
第一个镜像下载很慢，但后面的镜像就明显变快了

<br>

### 镜像特点

- 只读，不可修改镜像
- 当容器启动时，一个 ==**新的**== 可写层被加载到镜像的顶部，这层称为 =="容器层"==，容器层之下的还是旧的 "镜像层"

<br>


### **生成自定义镜像**

#### 1、提交容器形成新镜像 commit

提交容器 ==副本== 形成一个新镜像。修改后的容器想包起来行程一个新的镜像就直接 commit
```
docker commit -m="msg" -a="author" [containerID] [newImageName]:tag
```

#### 2、容器数据卷 ↙

看下面 ↓


## **容器数据卷**

当我们关闭容器的时候，希望部分容器的数据能保存起来，做持久化处理，这时候就要用容器数据卷

**数据卷作用：**
- 容器数据 **持久化**
- 容器之间可以 **继承** + **数据共享**
- 容器到主机，主机到容器数据之间共享（相当于 u 盘的作用）

**数据卷特点：**
1、可在容器之间共享或重用数据
2、卷中国的更改可以直接生效
3、数据卷中的<u>更改不会包含在镜像的更新中</u>
4、数据卷的<u>生命周期一直持续到没有容器使用它为止</u>

### 添加数据卷

#### 直接命令添加
-v 卷的缩写，以下指令表示建立宿主机与容器的数据卷映射
```
docker run -it -v [/宿主机绝对路径目录]:[/容器内部目录] [image]
```
如果宿主机和容器都没有数据卷目录，会自动帮你新建

当执行完上面的映射指令之后用`docker inspect`查看 json 信息可以在 `Volumes` 看到映射信息，在任意一个目录下面做的改动会同步到映射的另外一个目录上

即使容器在停止了，主机继续修改目录中的文件，在容器再次启动的时候会自动同步主机的修改

- 数据卷的权限
限制是否能自由更改数据卷的数据，查看`VolumesRW`可以知道数据卷的权限

设置数据卷权限，下来指令设置容器内的目录只读不可写(ro:read-only)，主机有读写权限，主机做的修改也可同步到容器，但是容器只有读的权限
```
docker run -it -v [/宿主机绝对路径目录]:[/容器内部目录]:ro [image]
```







#### DockerFile 添加





用 DockerFile 实现一对多的数据卷映射

```
# volume test
FROM centos
VOLUME ["/dataVolumeContainer", "/dataVolumeContainer2", "/dataVolumeContainer3"]
CMD echo "finished, ---success1"
CMD /bin/bash
```

如上面，在某==一个==容器的 DockerFile 中设定数据卷，用 **bulid** 指令实现 DockerFile 生成镜像。
当 run 这个镜像时，可以看到容器中会自动生成下面的三个数据卷目录。
而在宿主机中，由于命令没有指定宿主机目录，所以会自动用哈希值在宿主机生成目录。
用 `inspect` 指令可以在 `'Volumes'` 看到这个容器下面设定的3个映射
```
VOLUME["/dataVolumeContainer", "/dataVolumeContainer2", "/dataVolumeContainer3"]
```
注意：
**`[]`内的路径全部都只能是容器的**，
因为由于可移植和分享的考虑，用 `-v 主机目录:容器目录`的方法不能在 DockerFile 中实现

由于宿主机目录是依赖于特定宿主机的，<u>并不能保证在所有的宿主机上都存在这样的特定目录</u>，所以 docker 会自动在宿主机生成一个**默认**的数据卷目录


<br>

#### 数据卷容器

命名的容器挂载数据卷，其他容器通过挂载这个容器(父容器)实现数据共享。
<u>挂载数据卷的容器，成为数据卷容器。</u>

实际上，相当于 U 盘上叠加插一个 U 盘，实现数据的==传递依赖==。



##### 容器间数据共享
参数：`--volumes-from`

示例：
- 1、 先启动一个带有两个数据卷的父容器，容器命名为`dc01`：
```
docker run -it --name dc01 zzzy/centos
```

![2020-01-11 11_44_58-尚硅谷_Docker核心技术（基础篇）_哔哩哔哩 (゜-゜)つロ 干杯~-bilibili.png](https://upload-images.jianshu.io/upload_images/11876740-a8b04a718271cc70.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


- 2、容器`dc02` `dc03` 继承自 `dc01`：
```
docker run -iy --name dc02 --volumes-from dc01 zzyy/contos
docker run -iy --name dc03 --volumes-from dc01 zzyy/contos
```
上面的指令做的动作为：
以`zzyy/contos`image 为模板生成名为 `dc02` and `dc03` 的容器，数据卷继承自 `dc01`。
`dc02` 和 `dc03` 的容器中都有数据卷 `dataVolumeContainer1`, `dataVolumeContainer2`
<br>


**现在我们来看看 父数据卷 和子数据卷 的关系**：
- 父数据卷和子数据卷各自对数据卷的变动都会同步到对方的数据卷中，父->子, 子->父
- 删除父数据卷容器，子数据卷容器还会继续存在与同步

**结论：**
- 容器之间配置信息的传递，数据卷的生命周期一直持续到没有容器使用它位置
- 从父数据卷继承的得到的==子数据卷，**与父数据卷同级**==，不会在父数据卷之下，删除父数据卷不会影响子数据局


<br>

## **DockerFile**

**基本步骤：**
- **编写**：手动编写一个 dockerfile 文件，必须符合 dockerfile 规范
- **构建**：使用 `docker bulid` 命令执行这个 dockerfile 文件，获得一个 dockerfile 文件定义的镜像。
- **执行**：`docker run` 这个镜像


### DockerFile 是什么

[link](https://www.bilibili.com/video/BV1Vs411E7AR?p=22)
DockerFile 是由一系列命令和参数构成，用来构建 Docker 镜像的脚本文件。

DockerFile 定义了进程需要的需要的一起东西。
DockerFile 设计的内容包括执行代码或者是文件、环境变量、依赖包、运行时环境、动态链接库、操作系统发行版、服务进程和内核进程（当应用进程和系统服务和内核京城打交道，这是需要考虑如何设计 namespace 的权限控制）等等。
（==**其实就是个虚拟机镜像的终端版**==）

### 关于 /bin/bash 指令
[link](https://www.bilibili.com/video/BV1Vs411E7AR?p=23)
**注意：**
很多 dockerfile 文件都会在最后一行有 `CMD ["/bin/bash"]` 这表示在 run 这个镜像的时候，它会自动执行 `/bin/bash` 指令。
你 run 的时候可以自己加 `/bin/bash` 指令也可以不加，如果自己 run 的时候再加了，其实是运行了两遍 `/bin/bash` 指令，也没有问题。
但如果有些 dockerfile 文件都会在最后一行没有 `CMD ["/bin/bash"]` ，所以==最好自己 run 的时候要加上 `/bin/bash` 指令==


### DockerFile 构建过程解析

#### 基本规则

- 每条 **保留字指令** 都必须为**大写字母**并后面都要跟随至少一个参数
- 指令从上到下顺序执行
- `#` 表注释
- <u>每条指令都会创建一个新的镜像层，并对镜像进行提交</u>

#### 执行 DockerFile 的大致流程

- 1、docker 从 `FROM` 指定的源镜像运行一个容器
- 2、执行逐条指令并对容器进行修改
- 3、执行类似 `docker commit` 的操作提交一个新的镜像层
- 4、docker 再 <u>基于刚提交的镜像</u> 运行一个新容器
- 5、执行 dockerfile 中下一条指令直到所有指令都执行完成

#### 实质 -- Docker 体系的基石

从应用软件的角度看，DockerFile、镜像、容器三者分别代表软件的不同阶段。三者合力充当 Docker 体系的基石。
- **DockerFile**：是软件的开发要求
- **镜像**：是软件的交付品（已经按照要求包好了的）
- **容器**：是软件的运行形态

![Docker体系的基石.png](https://upload-images.jianshu.io/upload_images/11876740-19b502a200b1088b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


### **保留字指令**
[link](https://www.bilibili.com/video/BV1Vs411E7AR?p=24)

```python
FROM        : 源镜像 or 基础镜像。即当前镜像是基于哪个镜像来的

MAINTAINER  : 镜像维护者的姓名和邮箱

RUN         : 容器构建时需要运行的指令

EXPOSE      : 容器对外暴露的端口

WORKDIR     : 指定在创建容器后，终端默认登录时进的目录

ENV         : 在构建镜像的过程中设置环境变量

ADD         : 将宿主机目录下的文件拷贝进镜像（自动处理 URL 和解压 tar 压缩包）

COPY        : 拷贝文件和目录到镜像像中。从<源路径>的文件/目录 复制到 新的一层的镜像内的<目标路径>位置
              (类似ADD，但只拷贝不解压。有下面两种格式：)
              1. COPY src dest
              2. COPY ["src", "dest"]

VOLUME      : 容器数据卷

CMD         : 指定一个容器启动时要运行的命令。
              可以有多个 CMD 指令，但只有最后一个会生效，
              CMD 会被 docker run 之后的参数替换

ENTRYPOINT  : 指定一个容器启动时要运行的命令。
              追加指令，不止最后一个生效，所有 ENTRYPOINT 指令都会生效

ONBUILD     : 当构建一个被继承的 DockerFile 时运行命令，
              父镜像在被子镜像继承后，父镜像的 onbulid 被触发。
```

![保留字指令.png](https://upload-images.jianshu.io/upload_images/11876740-a380326d88a0baf0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)






#### 案例 1
[link](https://www.bilibili.com/video/BV1Vs411E7AR?p=25)

我们从 docker hub 中拉下来的 centos 镜像是最精简的，不能使用 `vim` `ifconfig` 指令。
现在我们用 DockerFile 做一个能够使用`vim` `ifconfig` 指令，并且指令登录时落脚的目录的镜像。
```
FROM centos                         # 源镜像
MAINTAINER zzyy<zzyy167@126.com>    # 作者 and 邮箱

ENV MYPATH /usr/local               # 环境变量（之后都可以用 $ 在这个容器中使用这个环境变量）
WORKDIR $MYPATH                     # 开启这个镜像时落脚目录

RUN yum -y install vim              # 安装 vim 指令
RUN yum -y install net-tools        # 安装 ifconfig 指令

EXPOSE 80                           # 构建的这个容器暴露 80 端口

CMD echo $MYPATH                    # 构建的最后执行指令
CMD echo "success----ok"             
CMD /bin/bash                       
```
####  案例 2 -- **ENTRYPOINT 追加参数**
```
FROM centos                                 
RUN yum install -y crul                     # 安装 curl (如果原来镜像已经有的话会跳过)
ENTRYPOINT ["curl", "-s", "http://ip.cn"]   # 执行指令 curl -s http://ip.cn 获取 html 文本
```
<u>用 **ENTRYPOINT** 作为最后一个保留字，在 run 这个 DockerFile 镜像的时候，你可以在后面 ==**追加** ENTRYPOINT 指令的参数。==</u>

我 build 这个 DockerFile 文件形成镜像：`docker build -f /dockerfile_path -t myip2 .`
然后 run 这个镜像：`docker run myip2 -i`
相当于 DockerFile 最后一行的指令变成：
`ENTRYPOINT ["curl", "-s", "-i", "http://ip.cn"]`，实际上是执行了`curl -s -i http://ip.cn`
追加了 ENTRYPOINT 指令的参数


但是假如我的 DockerFile 中最后一行是用 **CMD** 做保留字：`CMD ["curl", "-s", "http://ip.cn"]`，那么我如果想上面那样 run 的时候是不能追加参数的，否则会 ==**替换**== 掉原来 DockerFile 中的最后一行 CMD 指令，然后报错。

#### 案例 3 -- **ONBUILD**
```
FROM centos                                 
RUN yum install -y crul                     
ENTRYPOINT ["curl", "-s", "http://ip.cn"]   
ONBUILD RUN echo "now, build from father -- ok" # 当有子镜像继承自这个 DockerFile 生成的父镜像的时候，执行这条指令
```
加入我 build 上面的 DockerFile 文件生成一个名为 `myip_father` 的镜像。
我再写一个子 DockerFile 文件，继承自上面的 DockerFile 文件生成的镜像
```
FROM myip_father                            # 继承：注意是继承 ockerFile 文件生成的镜像
RUN yum install -y crul                     
ENTRYPOINT ["curl", "-s", "http://ip.cn"]   
```
然后 build 的时候会打出红色的提示信息，提示父镜像的 ONBUILD 被触发 (triggers)
```
# Excuting 1 build triggers
执行 ONBUILD 后面指定的动作
```

#### 案例 4 -- 使用全部保留字（自定义镜像tomcat9
1、`mkdir -p /zzyyuse/mydockerfile/tomcat9` 建文件夹

2、  在上面的目录中建一个文件

3、将 jdk 和 tomcat 安装的压缩包拷贝到上面的目录（不演示），在上面的目录中就有`apache-tomcat-9.0.8.tar.gz`、 `jdk-8u171-linux-x64.tar.gz`、 `touch c.txt` 

4、编写 DockerFile
```
FROM centos 
MAINTAINER zzyy<zzyy@163.com>
COPY c.txt /usr/local/cincontainer.txt      # 把宿主机当前目录下的 c.txt 文件拷贝到后面指定的镜像路径中 /use/local，重命名为 cincontainer.txt，不带后面的 txt 就表直接拷贝到 /use/local
ADD apache-tomcat-9.0.8.tar.gz /use/local/  # 把宿主机当前目录下的压缩包拷贝到镜像路径 /use/local 并解压
ADD jdk-8u171-linux-x64.tar.gz /use/local/  # 同上
RUN yum -y install vim
ENV MYPATH /usr/local
WORKDIR $MYPATH
# 配置环境变量
ENV JAVA_HOME /usr/local/jdk1.8.0_171
ENV CLASSPATH $JAVA_HOME/lib/dt.har:$JAVA_HOME/lib/tools.jar
ENV CATALINA_HOME /usr/local/apache-tomacat-9.0.8
ENV CATALINA_BASE /usr/local/apache-tomacat-9.0.8
ENV PATH $PATH:$JAVA_HOME/lib/bin:$CATALINA_HOME/lin:$CATALINA_HOME/bin
EXPOSE 80
# ENTRYPOINT 
# CMD 
CMD /usr/local/apache-tomacat-9.0.8/lib/startup.sh && tail -F /usr/local/apache-tomacat-9.0.8/lib/logs/catalina.out
```

5、build 形成镜像。
由于 DockerFile 在当前目录下，且名字就为 DockerFile，所以省略 -f 参数
```
docker build -t zzyytomcat9
```


6、多参数 run 镜像
```
docker run -d -p 9080:8080 --name myt9
-v /zzyyuse/mydockerfile/tomcat9/test:/usr/local/apache-tomacat-9.0.8/webapps/test
-v /zzyyuse/mydockerfile/tomcat9/tomcat9logs/:/usr/local/apache-tomacat-9.0.8/logs
--privileged=trur
zzyytomcat9
```
可以看到上面有两个数据卷的映射，结合我们自身的项目可以得到方便我们部署项目的操作：
第一个映射：用来放跑在这个容器的 sourcode 目录，当你在宿主机上修改 sourcode 的时候，能立刻同步到 docker 容器中
第二个映射：放容器中的 log 目录，可以直接在宿主机上查看 docker 容器中的执行情况


<br>

### 使用 DockerFile 构建镜像 **build**
指令：
`docker build -f [/dockerfile_path] -t [newImageName]:tag .`

注意最后面有一个 `.` 代表当前路径。
如果是在 DockerFile 所在的目录中， build 可以直接加 DockerFile 文件名。
如果是在 DockerFile 所在的目录中且有一个名为 DockerFile 的文件，可不带 -f 参数。


这 build 的过程中会有很多 step，都是一层一层叠加的镜像层。DockerFile 中的每一行都会生成一层镜像。

后续这个镜像就跟前面讲的镜像一样 run 来使用


### 查看镜像构建历史 **history**

指令：
`docker history [image]`

可以看到我们在 DockerFile 中指令的镜像层步骤



### DockerFile 小总结


![dockerFile架构.png](https://upload-images.jianshu.io/upload_images/11876740-b29b742427f1486c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)





<br>

<br><br><br><br><br><br><br><br><br><br><br><br>

```
```

<br><br><br><br><br><br><br><br><br><br><br><br><br>













