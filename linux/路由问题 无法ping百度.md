[toc]

---

# 1. 在物理机或者在已经映射进网卡的虚拟机上

出现接了外网但是还是无法ping baidu.com 的情况

原因：

```
[root@emma ~]# route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         xx.xx.xx.1      0.0.0.0         UG    102    0        0 eno2
0.0.0.0         192.168.x.1     0.0.0.0         UG    102    0        0 eno1
10.0.0.0        xx.xx.xx.1      255.0.0.0       UG    0      0        0 eno2
xx.xx.xx.0      0.0.0.0         255.255.255.0   U     101    0        0 eno2
192.168.x.0     0.0.0.0         255.255.255.0   U     102    0        0 eno1
192.168.xxx.0   0.0.0.0         255.255.255.0   U     0      0        0 virbr0
[root@emma ~]#
```
查看路由：
最上面看到两个`0.0.0.0`,经当系统无法识别要ping的网域时会走的路径，从上到下会走第一条`0.0.0.0`的路径。
ping baidu走第一条xx.xx的路径一定是走不出去的，所以要把第一条路由删掉：
```
[root@localhost ~]# route del -net 0.0.0.0 netmask 0.0.0.0 gw xx.xx.xx.1 dev eno2
```

添加路由路径：
```
# 添加网段10.0.0.0/255.0.0.0到网关xx.xx.xx.1的网口eno2的路由：
[root@localhost ~]# route add -net 10.0.0.0 netmask 255.0.0.0 gw xx.xx.xx.1 eno2 
```

由普通用户进入root用户：

```
su root
```
退出root用户

```
exit
```

<br><br>

有一种情况是，上面的都没问题，但是`ping baidu.com` 

出现error:  `name or service not know`

解决方法：[参考](https://www.cnblogs.com/Lin-Yi/p/7787392.html) 

root 用户下

添加dns服务器


```
vi /etc/resolv.conf
```


在文件中添加如下两行：


```
nameserver 8.8.8.8
nameserver 8.8.4.4
```


保存退出，重启服务器。之后再 ping baidu 一次试一试

又出现了error：
`
ping: unknown host baidu.com
`

初步估计是域名问题。
参考：
-》[link](https://www.cnblogs.com/happyhotty/articles/2539951.html)

ping 宿主机默认网关
```
ping 192.168.1.1
```
unreachable -> 没有连上路由器


# 2. 虚拟机没有映射网卡

这里以想要设置外网为例：

请先确保外层宿主机的物理机是用外网的。使用步骤1 中的步骤检查并开启外网

开启外网后，进入虚拟机查找有无映射，`-a` 参数可以查找所有可用的网卡，包括关闭的但可用的网卡：

```
ifconfig -a
```

找到外网的网卡之后（此时网卡没有开启，会以一串带::的字符串显示,假设网卡id 为ens3），使用指令开启网卡：
```
ifconfig ens3 up
```

之后使用 ifconfig 指令可以查看所有已经开启的网卡：

```
ifconfig
```