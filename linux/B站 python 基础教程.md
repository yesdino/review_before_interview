
## 查看网络 网卡

下面出来的信息表示本台服务器上面有3个网卡 其中

- `eth0` 表示可以用于通信的网卡
- `lo` 表示本地 用于显示本地网线等信息

```
[dino@iz8vbedklyif6ai6rxa557z ~]$ ifconfig
docker0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        inet 172.17.0.1  netmask 255.255.0.0  broadcast 172.17.255.255
        ether 02:42:24:b9:e5:c2  txqueuelen 0  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.26.104.107  netmask 255.255.240.0  broadcast 172.26.111.255
        ether 00:16:3e:04:03:ac  txqueuelen 1000  (Ethernet)
        RX packets 806215  bytes 189666118 (180.8 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 753426  bytes 238689875 (227.6 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 9731  bytes 2268232 (2.1 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 9731  bytes 2268232 (2.1 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

[dino@iz8vbedklyif6ai6rxa557z ~]$
```

关闭/开启网卡， 需要管理员权限
```
ifconfig eth0 down
ifconfig eth0 up
```


## ip 地址

### ip-v4 / ip-v6

v 是 version，是指 ip 命名规则的版本，即为第 4 个版本，前面 3 个版本为实验版本，到了第4个版本时实验可用。

那么 ip-v4 的命名规则是怎么样的呢？
- 由四组 XXX 组成
- 每组 XXX 的范围为 0~255 (256个)

即 `XXX.XXX.XXX.XXX` 那么 ip-v4 可以设定的ip数量是 `256*256*256*256`

本来以前设定时是认为一定够用，但是随着互联网的爆发，不够用了。

由此便需要继续发展新的 ip 命名规则的版本
继续研究时，第 5 个实验验证不可用，到第 6 个版本验证可用，于是又有了 Ip-v6

但由于目前的光纤设备都是根据 ip-v4 设定好的，ip-v6 即使可用大家都不愿意用，所以 ip-v6 发展缓慢，==目前说到的 ip 基本都是说的 ip-v4==

