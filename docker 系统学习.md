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

docker 守护进程 docker-daemon 运行在主机上，++**docker-daemon 通过 ==Socket== 连接从客户端接收命令并管理运行在主机上的容器**++

### docker 架构
![image](https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1578069293898&di=9f16d7ec562fa59361b62de054f9b143&imgtype=0&src=http%3A%2F%2Fimg1.mukewang.com%2F5b783ab700016b6a08840463.jpg)

看右上角的蓝色鲸鱼，鲸鱼背上有集装箱

```
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



担心会冲突 这里放增加的内容


## 常见应用容器安装

### **Mysql** docker

[link](https://www.bilibili.com/video/BV1Vs411E7AR?p=31)
先去 pull mysql 镜像下来
然后用下面指令 run 镜像（有些参数根据情况修改一下
```
docker run -p 12345:3306 --name mysql 
-v /zzyyuse/mysql/conf:/etc/mysql/conf.d 
-v /zzyyuse/mysql/log:/logs 
-v /zzyyuse/mysql/data:/var/lib/mysql 
-e MYSQL_ROOT_PASSWORD=123456 
-d mysql:5.6
```
指令说明：

<img src="/img/docker/docker_mysql_run.png">


#### 在 docker 中进行 mysql DB 操作

[link 10:01](https://www.bilibili.com/video/BV1Vs411E7AR?p=31)

在 docker mysql run 起来之后：

<img src="/img/docker/docker_mysql_db.png">


#### 外部 win10 连接 docker mysql

[link 12:10](https://www.bilibili.com/video/BV1Vs411E7AR?p=31)


#### docker mysql 数据备份到宿主机

[link 13:33](https://www.bilibili.com/video/BV1Vs411E7AR?p=31)

指令
<img src="/img/docker/docker_mysql_dumpload_data.png">
 

### **nginx** docker 


[link](https://www.bilibili.com/video/BV1Vs411E7AR?p=32)



---


# **Docker Compose**

[出处：作者 朱敬志](https://www.cnblogs.com/zhujingzhi/p/9786622.html)

## 一、什么是 Docker Compose

Compose 项目是Docker官方的开源项目，负责实现Docker容器集群的快速编排，开源代码在https://github.com/docker/compose 上

我们知道使用Dockerfile模板文件可以让用户很方便的定义一个单独的应用容器，其实在工作中，经常会碰到需要多个容器相互配合来完成的某项任务情况，例如工作中的web服务容器本身，往往会在后端加上数据库容器，甚至会有负责均衡器，比如LNMP服务

Compose 就是来做这个事情的，它允许用户通过一个单独的docker-compose.yml模板文件(YAML格式)来定义一组相关联的应用容器为一个项目(project)

Compose 中有两个重要的概念：

服务(service):一个应用的容器，实际上可以包括若干运行相同镜像的容器实例
项目(project):由一组关联的应用容器组成的一个完整业务单元，在docker-compose.yml中定义


## 二、基本原理

Compose 项目是由Python编写的，实际上就是调用了Docker服务提供的API来对容器进行管理，因此，只要所在的操作系统的平台支持Docker API，就可以在其上利用Compose来进行编排管理.



## 三、安装

- **二进制包安装**
```
[root@operation ~]## curl -L https://github.com/docker/compose/releases/download/1.23.0-rc2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
% Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                Dload  Upload   Total   Spent    Left  Speed
100   617    0   617    0     0    373      0 --:--:--  0:00:01 --:--:--   373
100 11.1M  100 11.1M    0     0   368k      0  0:00:31  0:00:31 --:--:--  444k
[root@operation ~]# chmod +x /usr/local/bin/docker-compose
[root@operation ~]# docker-compose version
docker-compose version 1.23.0-rc2, build 350a555e
docker-py version: 3.5.0
CPython version: 3.6.6
OpenSSL version: OpenSSL 1.1.0f  25 May 2017
```

- **pip 安装** （安装的是最新稳定版本

Compose 既然是用python编写的那么肯定是可以用pip install 进行安装的
```
[root@operation ~]# pip install docker-compose
```
安装完需要做个软链接
```
[root@operation ~]# ln -s /usr/bin/docker-compose /usr/local/bin/
[root@operation ~]# docker-compose version
docker-compose version 1.22.0, build f46880f
docker-py version: 3.5.0
CPython version: 2.7.5
OpenSSL version: OpenSSL 1.0.1e-fips 11 Feb 2013
```


- **容器安装**

```
[root@operation ~]# curl -L https://github.com/docker/compose/releases/download/1.23.0-rc2/run.sh > /usr/local/bin/docker-compose
% Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                Dload  Upload   Total   Spent    Left  Speed
100   596    0   596    0     0    158      0 --:--:--  0:00:03 --:--:--   158
100  1670  100  1670    0     0    343      0  0:00:04  0:00:04 --:--:-- 1630k
[root@operation ~]# chmod +x /usr/local/bin/docker-compose
[root@operation ~]# docker-compose
Unable to find image 'docker/compose:1.23.0-rc2' locally
1.23.0-rc2: Pulling from docker/compose
3489d1c4660e: Pull complete
2e51ed086e7d: Pull complete
07d7b41c67a1: Pull complete
Digest: sha256:14f5ad3c2162b26b3eaafe870822598f80b03ec36fd45126952c891fd5e5a59a
# 实际上就是下的镜像(可以看下下载的run.sh脚本)
[root@operation ~]# docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
docker/compose      1.23.0-rc2          dc59a0b5e981        5 days ago          45.6MB
alpine              latest              196d12cf6ab1        4 weeks ago         4.41MB
[root@operation ~]# docker-compose version
docker-compose version 1.23.0-rc2, build 350a555e
docker-py version: 3.5.0
CPython version: 3.6.6
OpenSSL version: OpenSSL 1.1.0f  25 May 2017
```


## 四、命令
Compose 大部分命令的对象即可以是项目的本身，也可以是指定为项目中的服务或者容器
执行 `docker-compose [COMMAND] --help` 或者 `docker-compose help [COMMAND]` 可以查看命令的帮助信息

具体的使用格式：
```py
docker-compose [-f=<arg>...] [options] [COMMAND] [ARGS]

参数选项
-f,--file file指定模板文件，默认是docker-compose.yml模板文件,可以多次指定
-p,--project-name name指定项目名称，默认使用所在目录名称作为项目名称
--x-networking 使用Docker的后端可插拔网络特性
--x-networking-driver driver指定网络的后端驱动，默认使用bridge
--verbose 输入更多的调试信息
-v,--version 输出版本信息
```


### Compose 所支持的命令
```python
build              Build or rebuild services (构建项目中的服务容器)
bundle             Generate a Docker bundle from the Compose file (从Compose文件生成分布式应用程序包)
config             Validate and view the Compose file (验证并查看Compose文件)
create             Create services (为服务创建容器)
down               Stop and remove containers, networks, images, and volumes (停止容器并删除由其创建的容器，网络，卷和图像up)
events             Receive real time events from containers (为项目中的每个容器流式传输容器事件)
exec               Execute a command in a running container (这相当于docker exec。使用此子命令，您可以在服务中运行任意命令。默认情况下，命令分配TTY，因此您可以使用命令docker-compose exec web sh来获取交互式提示。)
help               Get help on a command (获得一个命令的帮助)
images             List images ()
kill               Kill containers (通过发送SIGKILL信号来强制停止服务容器)
logs               View output from containers (查看服务容器的输出)
pause              Pause services (暂停一个容器)
port               Print the public port for a port binding (打印某个容器端口所映射的公共端口)
ps                 List containers (列出项目中目前所有的容器)
pull               Pull service images (拉取服务依赖镜像)
push               Push service images (推送服务镜像)
restart            Restart services (重启项目中的服务)
rm                 Remove stopped containers (删除所有停止状态的服务容器)
run                Run a one-off command (在指定服务上执行一个命令)
scale              Set number of containers for a service (设置指定服务执行的容器个数)
start              Start services (启动已存在的服务容器)
stop               Stop services (停止已存在的服务容器)
top                Display the running processes (显示容器正在运行的进程)
unpause            Unpause services (恢复处于暂停状态的容器)
up                 Create and start containers (自动完成包括构建镜像、创建服务、启动服务并关联服务相关容器的一系列操作)
version            Show the Docker-Compose version information (输出版本)
```


因为太多的原因我这里就不写了,有时间我在把每个命令的使用方法补上吧

针对模板文件的使用才是重中之重，我在后面会对模板文件详细讲解

官方链接：https://docs.docker.com/compose/reference/build/



## 五、环境变量

环境变量可以用来配置 Compose 的行为,以 **`DOCKER_`** 开头的变量和用来配置 Docker 命令行客户端的使用一样。
如果使用 boot2docker , $(boot2docker shellinit) 将会设置它们为正确的值
 
```python
COMPOSE_PROJECT_NAME    设置通过 Compose 启动的每一个容器前添加的项目名称，默认是当前工作目录的名字。
 
COMPOSE_FILE            设置要使用的 docker-compose.yml 的路径。默认路径是当前工作目录。
 
DOCKER_HOST             设置 Docker daemon 的地址。默认使用 unix:///var/run/docker.sock，与 Docker 客户端采用的默认值一致。
 
DOCKER_TLS_VERIFY       如果设置不为空，则与 Docker daemon 交互通过 TLS 进行。
 
DOCKER_CERT_PATH        配置 TLS 通信所需要的验证（ca.pem、cert.pem 和 key.pem）文件的路径，默认是 ~/.docker
```

在使用的时候在做解释和操作吧，因为一般不会改环境变量的东西，默认的就OK，做个简单的了解

官方链接：https://docs.docker.com/compose/reference/envvars/#compose_project_name



## 六、模板文件（重点

模板文件时Compose的核心，涉及的指令关键字比较多，但是大部分的指令与 docker run 相关的参数的含义是类似的

默认的模板名是 docker-compose.yml

官网链接：https://docs.docker.com/compose/compose-file/#compose-file-structure-and-examples

```python
Compose 和 Docker 兼容性：
    Compose 文件格式有3个版本,分别为1, 2.x 和 3.x
    目前主流的为 3.x 其支持 docker 1.13.0 及其以上的版本
 
 
常用参数：
    version           # 指定 compose 文件的版本
    services          # 定义所有的 service 信息, services 下面的第一级别的 key 既是一个 service 的名称
 
        build                 # 指定包含构建上下文的路径, 或作为一个对象，该对象具有 context 和指定的 dockerfile 文件以及 args 参数值
            context               # context: 指定 Dockerfile 文件所在的路径
            dockerfile            # dockerfile: 指定 context 指定的目录下面的 Dockerfile 的名称(默认为 Dockerfile)
            args                  # args: Dockerfile 在 build 过程中需要的参数 (等同于 docker container build --build-arg 的作用)
            cache_from            # v3.2中新增的参数, 指定缓存的镜像列表 (等同于 docker container build --cache_from 的作用)
            labels                # v3.3中新增的参数, 设置镜像的元数据 (等同于 docker container build --labels 的作用)
            shm_size              # v3.5中新增的参数, 设置容器 /dev/shm 分区的大小 (等同于 docker container build --shm-size 的作用)
 
        command               # 覆盖容器启动后默认执行的命令, 支持 shell 格式和 [] 格式
 
        configs               # 不知道怎么用
 
        cgroup_parent         # 不知道怎么用
 
        container_name        # 指定容器的名称 (等同于 docker run --name 的作用)
 
        credential_spec       # 不知道怎么用
 
        deploy                # v3 版本以上, 指定与部署和运行服务相关的配置, deploy 部分是 docker stack 使用的, docker stack 依赖 docker swarm
            endpoint_mode         # v3.3 版本中新增的功能, 指定服务暴露的方式
                vip                   # Docker 为该服务分配了一个虚拟 IP(VIP), 作为客户端的访问服务的地址
                dnsrr                 # DNS轮询, Docker 为该服务设置 DNS 条目, 使得服务名称的 DNS 查询返回一个 IP 地址列表, 客户端直接访问其中的一个地址
            labels                # 指定服务的标签，这些标签仅在服务上设置
            mode                  # 指定 deploy 的模式
                global                # 每个集群节点都只有一个容器
                replicated            # 用户可以指定集群中容器的数量(默认)
            placement             # 不知道怎么用
            replicas              # deploy 的 mode 为 replicated 时, 指定容器副本的数量
            resources             # 资源限制
                limits                # 设置容器的资源限制
                    cpus: "0.5"           # 设置该容器最多只能使用 50% 的 CPU
                    memory: 50M           # 设置该容器最多只能使用 50M 的内存空间
                reservations          # 设置为容器预留的系统资源(随时可用)
                    cpus: "0.2"           # 为该容器保留 20% 的 CPU
                    memory: 20M           # 为该容器保留 20M 的内存空间
            restart_policy        # 定义容器重启策略, 用于代替 restart 参数
                condition             # 定义容器重启策略(接受三个参数)
                    none                  # 不尝试重启
                    on-failure            # 只有当容器内部应用程序出现问题才会重启
                    any                   # 无论如何都会尝试重启(默认)
                delay                 # 尝试重启的间隔时间(默认为 0s)
                max_attempts          # 尝试重启次数(默认一直尝试重启)
                window                # 检查重启是否成功之前的等待时间(即如果容器启动了, 隔多少秒之后去检测容器是否正常, 默认 0s)
            update_config         # 用于配置滚动更新配置
                parallelism           # 一次性更新的容器数量
                delay                 # 更新一组容器之间的间隔时间
                failure_action        # 定义更新失败的策略
                    continue              # 继续更新
                    rollback              # 回滚更新
                    pause                 # 暂停更新(默认)
                monitor               # 每次更新后的持续时间以监视更新是否失败(单位: ns|us|ms|s|m|h) (默认为0)
                max_failure_ratio     # 回滚期间容忍的失败率(默认值为0)
                order                 # v3.4 版本中新增的参数, 回滚期间的操作顺序
                    stop-first            #旧任务在启动新任务之前停止(默认)
                    start-first           #首先启动新任务, 并且正在运行的任务暂时重叠
            rollback_config       # v3.7 版本中新增的参数, 用于定义在 update_config 更新失败的回滚策略
                parallelism           # 一次回滚的容器数, 如果设置为0, 则所有容器同时回滚
                delay                 # 每个组回滚之间的时间间隔(默认为0)
                failure_action        # 定义回滚失败的策略
                    continue              # 继续回滚
                    pause                 # 暂停回滚
                monitor               # 每次回滚任务后的持续时间以监视失败(单位: ns|us|ms|s|m|h) (默认为0)
                max_failure_ratio     # 回滚期间容忍的失败率(默认值0)
                order                 # 回滚期间的操作顺序
                    stop-first            # 旧任务在启动新任务之前停止(默认)
                    start-first           # 首先启动新任务, 并且正在运行的任务暂时重叠
               
            注意：
                支持 docker-compose up 和 docker-compose run 但不支持 docker stack deploy 的子选项
                security_opt  container_name  devices  tmpfs  stop_signal  links    cgroup_parent
                network_mode  external_links  restart  build  userns_mode  sysctls
 
        devices               # 指定设备映射列表 (等同于 docker run --device 的作用)
 
        depends_on            # 定义容器启动顺序 (此选项解决了容器之间的依赖关系， 此选项在 v3 版本中 使用 swarm 部署时将忽略该选项)
            示例：
                docker-compose up 以依赖顺序启动服务，下面例子中 redis 和 db 服务在 web 启动前启动
                默认情况下使用 docker-compose up web 这样的方式启动 web 服务时，也会启动 redis 和 db 两个服务，因为在配置文件中定义了依赖关系
 
                version: '3'
                services:
                    web:
                        build: .
                        depends_on:
                            - db     
                            - redis 
                    redis:
                        image: redis
                    db:
                        image: postgres                            
 
        dns                   # 设置 DNS 地址(等同于 docker run --dns 的作用)
 
        dns_search            # 设置 DNS 搜索域(等同于 docker run --dns-search 的作用)
 
        tmpfs                 # v2 版本以上, 挂载目录到容器中, 作为容器的临时文件系统(等同于 docker run --tmpfs 的作用, 在使用 swarm 部署时将忽略该选项)
 
        entrypoint            # 覆盖容器的默认 entrypoint 指令 (等同于 docker run --entrypoint 的作用)
 
        env_file              # 从指定文件中读取变量设置为容器中的环境变量, 可以是单个值或者一个文件列表, 如果多个文件中的变量重名则后面的变量覆盖前面的变量, environment 的值覆盖 env_file 的值
            文件格式：
                RACK_ENV=development
 
        environment           # 设置环境变量， environment 的值可以覆盖 env_file 的值 (等同于 docker run --env 的作用)
 
        expose                # 暴露端口, 但是不能和宿主机建立映射关系, 类似于 Dockerfile 的 EXPOSE 指令
 
        external_links        # 连接不在 docker-compose.yml 中定义的容器或者不在 compose 管理的容器(docker run 启动的容器, 在 v3 版本中使用 swarm 部署时将忽略该选项)
 
        extra_hosts           # 添加 host 记录到容器中的 /etc/hosts 中 (等同于 docker run --add-host 的作用)
 
        healthcheck           # v2.1 以上版本, 定义容器健康状态检查, 类似于 Dockerfile 的 HEALTHCHECK 指令
            test                  # 检查容器检查状态的命令, 该选项必须是一个字符串或者列表, 第一项必须是 NONE, CMD 或 CMD-SHELL, 如果其是一个字符串则相当于 CMD-SHELL 加该字符串
                NONE                  # 禁用容器的健康状态检测
                CMD                   # test: ["CMD", "curl", "-f", "http://localhost"]
                CMD-SHELL             # test: ["CMD-SHELL", "curl -f http://localhost || exit 1"] 或者　test: curl -f https://localhost || exit 1
            interval: 1m30s       # 每次检查之间的间隔时间
            timeout: 10s          # 运行命令的超时时间
            retries: 3            # 重试次数
            start_period: 40s     # v3.4 以上新增的选项, 定义容器启动时间间隔
            disable: true         # true 或 false, 表示是否禁用健康状态检测和　test: NONE 相同
         
        image                 # 指定 docker 镜像, 可以是远程仓库镜像、本地镜像
 
        init                  # v3.7 中新增的参数, true 或 false 表示是否在容器中运行一个 init, 它接收信号并传递给进程
 
        isolation             # 隔离容器技术, 在 Linux 中仅支持 default 值
 
        labels                # 使用 Docker 标签将元数据添加到容器, 与 Dockerfile 中的 LABELS 类似
 
        links                 # 链接到其它服务中的容器, 该选项是 docker 历史遗留的选项, 目前已被用户自定义网络名称空间取代, 最终有可能被废弃 (在使用 swarm 部署时将忽略该选项)
         
        logging               # 设置容器日志服务
            driver                # 指定日志记录驱动程序, 默认 json-file (等同于 docker run --log-driver 的作用)
            options               # 指定日志的相关参数 (等同于 docker run --log-opt 的作用)
                max-size              # 设置单个日志文件的大小, 当到达这个值后会进行日志滚动操作
                max-file              # 日志文件保留的数量
 
        network_mode          # 指定网络模式 (等同于 docker run --net 的作用, 在使用 swarm 部署时将忽略该选项)        
 
        networks              # 将容器加入指定网络 (等同于 docker network connect 的作用), networks 可以位于 compose 文件顶级键和 services 键的二级键
            aliases               # 同一网络上的容器可以使用服务名称或别名连接到其中一个服务的容器
            ipv4_address      # IP V4 格式
            ipv6_address      # IP V6 格式
 
            示例:
                version: '3.7'
                services:
                    test:
                        image: nginx:1.14-alpine
                        container_name: mynginx
                        command: ifconfig
                        networks:
                            app_net:                                # 调用下面 networks 定义的 app_net 网络
                            ipv4_address: 172.16.238.10
                networks:
                    app_net:
                        driver: bridge
                        ipam:
                            driver: default
                            config:
                                - subnet: 172.16.238.0/24
 
        pid: 'host'           # 共享宿主机的 进程空间(PID)
 
        ports                 # 建立宿主机和容器之间的端口映射关系, ports 支持两种语法格式
            SHORT 语法格式示例:
                - "3000"                            # 暴露容器的 3000 端口, 宿主机的端口由 docker 随机映射一个没有被占用的端口
                - "3000-3005"                       # 暴露容器的 3000 到 3005 端口, 宿主机的端口由 docker 随机映射没有被占用的端口
                - "8000:8000"                       # 容器的 8000 端口和宿主机的 8000 端口建立映射关系
                - "9090-9091:8080-8081"
                - "127.0.0.1:8001:8001"             # 指定映射宿主机的指定地址的
                - "127.0.0.1:5000-5010:5000-5010"  
                - "6060:6060/udp"                   # 指定协议
 
            LONG 语法格式示例:(v3.2 新增的语法格式)
                ports:
                    - target: 80                    # 容器端口
                      published: 8080               # 宿主机端口
                      protocol: tcp                 # 协议类型
                      mode: host                    # host 在每个节点上发布主机端口,  ingress 对于群模式端口进行负载均衡
 
        secrets               # 不知道怎么用
 
        security_opt          # 为每个容器覆盖默认的标签 (在使用 swarm 部署时将忽略该选项)
 
        stop_grace_period     # 指定在发送了 SIGTERM 信号之后, 容器等待多少秒之后退出(默认 10s)
 
        stop_signal           # 指定停止容器发送的信号 (默认为 SIGTERM 相当于 kill PID; SIGKILL 相当于 kill -9 PID; 在使用 swarm 部署时将忽略该选项)
 
        sysctls               # 设置容器中的内核参数 (在使用 swarm 部署时将忽略该选项)
 
        ulimits               # 设置容器的 limit
 
        userns_mode           # 如果Docker守护程序配置了用户名称空间, 则禁用此服务的用户名称空间 (在使用 swarm 部署时将忽略该选项)
 
        volumes               # 定义容器和宿主机的卷映射关系, 其和 networks 一样可以位于 services 键的二级键和 compose 顶级键, 如果需要跨服务间使用则在顶级键定义, 在 services 中引用
            SHORT 语法格式示例:
                volumes:
                    - /var/lib/mysql                # 映射容器内的 /var/lib/mysql 到宿主机的一个随机目录中
                    - /opt/data:/var/lib/mysql      # 映射容器内的 /var/lib/mysql 到宿主机的 /opt/data
                    - ./cache:/tmp/cache            # 映射容器内的 /var/lib/mysql 到宿主机 compose 文件所在的位置
                    - ~/configs:/etc/configs/:ro    # 映射容器宿主机的目录到容器中去, 权限只读
                    - datavolume:/var/lib/mysql     # datavolume 为 volumes 顶级键定义的目录, 在此处直接调用
             
            LONG 语法格式示例:(v3.2 新增的语法格式)
                version: "3.2"
                services:
                    web:
                        image: nginx:alpine
                        ports:
                            - "80:80"
                        volumes:
                            - type: volume                  # mount 的类型, 必须是 bind、volume 或 tmpfs
                                source: mydata              # 宿主机目录
                                target: /data               # 容器目录
                                volume:                     # 配置额外的选项, 其 key 必须和 type 的值相同
                                    nocopy: true                # volume 额外的选项, 在创建卷时禁用从容器复制数据
                            - type: bind                    # volume 模式只指定容器路径即可, 宿主机路径随机生成; bind 需要指定容器和数据机的映射路径
                                source: ./static
                                target: /opt/app/static
                                read_only: true             # 设置文件系统为只读文件系统
                volumes:
                    mydata:                                 # 定义在 volume, 可在所有服务中调用
                 
        restart               # 定义容器重启策略(在使用 swarm 部署时将忽略该选项, 在 swarm 使用 restart_policy 代替 restart)
            no                    # 禁止自动重启容器(默认)
            always                # 无论如何容器都会重启
            on-failure            # 当出现 on-failure 报错时, 容器重新启动
 
        其他选项：
            domainname, hostname, ipc, mac_address, privileged, read_only, shm_size, stdin_open, tty, user, working_dir
            上面这些选项都只接受单个值和 docker run 的对应参数类似
 
        对于值为时间的可接受的值：
            2.5s
            10s
            1m30s
            2h32m
            5h34m56s
 
            时间单位: us, ms, s, m， h
 
        对于值为大小的可接受的值：
            2b
            1024kb
            2048k
            300m
            1gb
 
            单位: b, k, m, g 或者 kb, mb, gb
 
 
 
 
 
    networks          # 定义 networks 信息
        driver                # 指定网络模式, 大多数情况下, 它 bridge 于单个主机和 overlay Swarm 上
            bridge                # Docker 默认使用 bridge 连接单个主机上的网络
            overlay               # overlay 驱动程序创建一个跨多个节点命名的网络
            host                  # 共享主机网络名称空间(等同于 docker run --net=host)
            none                  # 等同于 docker run --net=none
 
        driver_opts           # v3.2以上版本, 传递给驱动程序的参数, 这些参数取决于驱动程序
 
        attachable            # driver 为 overlay 时使用, 如果设置为 true 则除了服务之外，独立容器也可以附加到该网络; 如果独立容器连接到该网络，则它可以与其他 Docker 守护进程连接到的该网络的服务和独立容器进行通信
 
        ipam                  # 自定义 IPAM 配置. 这是一个具有多个属性的对象, 每个属性都是可选的
            driver                # IPAM 驱动程序, bridge 或者 default
            config                # 配置项
                subnet                # CIDR格式的子网，表示该网络的网段
         
        external              # 外部网络, 如果设置为 true 则 docker-compose up 不会尝试创建它, 如果它不存在则引发错误
 
        name                  # v3.5 以上版本, 为此网络设置名称
     
 
 
文件格式示例：
    version: "3"
    services:
 
      redis:
        image: redis:alpine
        ports:
          - "6379"
        networks:
          - frontend
        deploy:
          replicas: 2
          update_config:
            parallelism: 2
            delay: 10s
          restart_policy:
            condition: on-failure
 
      db:
        image: postgres:9.4
        volumes:
          - db-data:/var/lib/postgresql/data
        networks:
          - backend
        deploy:
          placement:
            constraints: [node.role == manager]
```


## 七、Compose 使用（重点

举个简单的例子来具有的说明一下 Compose 的使用(也是官网的一个入门小例子)

先决条件：
确保您已经安装了 Docker Engine 和 Docker Compose。
您不需要安装 Python 或 Redis，因为两者都是由 Docker 镜像提供的。

### 1. 创建所有需要的文件

```python
# 创建目录
[root@operation ~]# mkdir composetest
[root@operation ~]# cd composetest/
```
```python
# 创建一个Python应用， 使用Flask，将数值记入Redis
[root@operation composetest]# cat app.py
import time
 
import redis
from flask import Flask
 
 
app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)
 
 
def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)
 
 
@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
 
 
```
```python
# 创建requirements.txt文件，里面是需要安装的Python包
[root@operation composetest]# cat requirements.txt
flask
redis
```
```python
# 创建 Dockerfile文件
# 在此步骤中，您将编写一个构建 Docker 镜像的 Dockerfile。
# 该图像包含 Python 应用程序所需的所有依赖项，包括 Python 本身。
[root@operation composetest]# cat Dockerfile
FROM python:3.6-alpine
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
 
# 这告诉Docker：
# 从 Python 3.6 映像开始构建映像。
# 将当前目录添加.到 /code 映像中的路径中。
# 将工作目录设置为 /code。
# 安装 Python 依赖项。
# 将容器的默认命令设置为 python app.py。
```
```python
# 创建 docker-compose.yml 文件
[root@operation composetest]# cat docker-compose.yml
version: '3'
services:
  web:
    build: .
    ports:
     - "5000:5000"
    volumes:
     - .:/code
  redis:
    image: "redis:alpine"
```
 
此 Compose 文件定义了两个服务，web 和 redis。

- **web 服务**：使用从 Dockerfile 当前目录中构建的图像。 
将容器上的公开端口 5000 转发到主机上的端口 5000 。
我们使用 Flask Web 服务器的默认端口 5000。 

- **redis 服务**：使用从 Docker Hub 注册表中提取的公共 Redis 映像。


### 2. 使用 Compose 构建并运行您的应用程序

```python
[root@operation composetest]# docker-compose up
```
```
# 出现下面说明成功了
redis_1_bfd9eb391c58 | 1:M 14 Oct 08:29:53.581 * Ready to accept connections
web_1_6f42e21c34dd |  * Serving Flask app "app" (lazy loading)
web_1_6f42e21c34dd |  * Environment: production
web_1_6f42e21c34dd |    WARNING: Do not use the development server in a production environment.
web_1_6f42e21c34dd |    Use a production WSGI server instead.
web_1_6f42e21c34dd |  * Debug mode: on
web_1_6f42e21c34dd |  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
web_1_6f42e21c34dd |  * Restarting with stat
web_1_6f42e21c34dd |  * Debugger is active!
web_1_6f42e21c34dd |  * Debugger PIN: 160-344-502
```

### 3. 测试访问

在浏览器访问`IP:5000` 我这里是`192.168.31.43:5000`

每刷新一次就会加一

![img](https://img2018.cnblogs.com/blog/1479220/201810/1479220-20181014163502857-1434099287.png)



<br>

<br><br><br><br><br><br><br><br><br><br><br><br>

```
```

<br><br><br><br><br><br><br><br><br><br><br><br><br>













