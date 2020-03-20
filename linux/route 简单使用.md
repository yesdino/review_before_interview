[toc]

---


# route 命令格式：
route  **`[add/del]`** **`[-net/-host]`+Destination**  **`[netmask/Nm]`+Genmask** **`[gw/Gw]`+Gateway** `[[dev] If]`
```
参数：
add/del     : 添加/删除 一条路由规则
-net/-host  : 目的地址是一个网络/主机
target      : 目的网络或主机
netmask     : 目的地址的 *网络掩码*
gw          : 路由数据包通过的 *网关*
dev         : 为路由指定的 *网络接口* （可选）
```


# 示例
- 原始 route
```
[root@localhost ~]# route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         192.168.1.1     0.0.0.0         UG    100    0        0 ens3 (不想要这条)
0.0.0.0         10.41.95.1      0.0.0.0         UG    101    0        0 ens8
10.41.95.0      0.0.0.0         255.255.255.0   U     101    0        0 ens8
192.168.1.0     0.0.0.0         255.255.255.0   U     100    0        0 ens3
192.168.122.0   0.0.0.0         255.255.255.0   U     0      0        0 virbr0
```

- 删除不要的 (第一条)
```
[root@localhost ~]# route del -net 0.0.0.0 netmask 0.0.0.0 gw 192.168.1.1
```
```
[root@localhost ~]# route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         10.41.95.1      0.0.0.0         UG    101    0        0 ens8
10.41.95.0      0.0.0.0         255.255.255.0   U     101    0        0 ens8
192.168.1.0     0.0.0.0         255.255.255.0   U     100    0        0 ens3
192.168.122.0   0.0.0.0         255.255.255.0   U     0      0        0 virbr0
```

- 添加需要的
```
[root@localhost ~]# route add -net 192.168.1.0 netmask 255.255.255.0 gw 192.168.1.1
```
```
[root@localhost ~]# route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         10.41.95.1      0.0.0.0         UG    101    0        0 ens8
10.41.95.0      0.0.0.0         255.255.255.0   U     101    0        0 ens8
192.168.1.0     192.168.1.1     255.255.255.0   UG    0      0        0 ens3 (加了这条)
192.168.1.0     0.0.0.0         255.255.255.0   U     100    0        0 ens3
192.168.122.0   0.0.0.0         255.255.255.0   U     0      0        0 virbr0
```

- 测试
```
[root@localhost ~]# ping 192.168.1.2
PING 192.168.1.2 (192.168.1.2) 56(84) bytes of data.
64 bytes from 192.168.1.2: icmp_seq=1 ttl=64 time=0.033 ms
64 bytes from 192.168.1.2: icmp_seq=2 ttl=64 time=0.030 ms
^C
--- 192.168.1.2 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 999ms
rtt min/avg/max/mdev = 0.030/0.031/0.033/0.005 ms
[root@localhost ~]# ping 10.41.95.1
PING 10.41.95.1 (10.41.95.1) 56(84) bytes of data.
64 bytes from 10.41.95.1: icmp_seq=1 ttl=64 time=3.31 ms
64 bytes from 10.41.95.1: icmp_seq=2 ttl=64 time=1.65 ms
^C
--- 10.41.95.1 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1001ms
rtt min/avg/max/mdev = 1.650/2.483/3.317/0.834 ms
[root@localhost ~]# 
```
