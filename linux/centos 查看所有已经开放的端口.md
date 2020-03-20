**netstat -tlunp**
```
[root@iz8vbedklyif6ai6rxa557z imooc]# netstat -tlunp
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 127.0.0.1:42284         0.0.0.0:*               LISTEN      26268/python3.6
tcp        0      0 127.0.0.1:42800         0.0.0.0:*               LISTEN      27171/python3.6
tcp        0      0 127.0.0.1:38800         0.0.0.0:*               LISTEN      27171/python3.6
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      930/nginx: master p
tcp        0      0 127.0.0.1:56594         0.0.0.0:*               LISTEN      26268/python3.6
tcp        0      0 172.26.104.107:1234     0.0.0.0:*               LISTEN      26263/python3.6
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      4994/sshd
tcp        0      0 127.0.0.1:46520         0.0.0.0:*               LISTEN      27171/python3.6
tcp        0      0 127.0.0.1:41979         0.0.0.0:*               LISTEN      26268/python3.6
tcp        0      0 127.0.0.1:46236         0.0.0.0:*               LISTEN      26268/python3.6
tcp        0      0 127.0.0.1:38789         0.0.0.0:*               LISTEN      27171/python3.6
tcp        0      0 127.0.0.1:43910         0.0.0.0:*               LISTEN      26268/python3.6
tcp        0      0 127.0.0.1:47016         0.0.0.0:*               LISTEN      26268/python3.6
tcp        0      0 127.0.0.1:60298         0.0.0.0:*               LISTEN      27171/python3.6
tcp        0      0 127.0.0.1:44746         0.0.0.0:*               LISTEN      27171/python3.6
tcp6       0      0 :::80                   :::*                    LISTEN      930/nginx: master p
tcp6       0      0 :::33060                :::*                    LISTEN      26804/mysqld
tcp6       0      0 :::3306                 :::*                    LISTEN      26804/mysqld
udp        0      0 0.0.0.0:68              0.0.0.0:*                           707/dhclient
udp        0      0 172.17.0.1:123          0.0.0.0:*                           5230/ntpd
udp        0      0 172.26.104.107:123      0.0.0.0:*                           5230/ntpd
udp        0      0 127.0.0.1:123           0.0.0.0:*                           5230/ntpd
udp        0      0 0.0.0.0:123             0.0.0.0:*                           5230/ntpd
udp        0      0 0.0.0.0:27363           0.0.0.0:*                           707/dhclient
udp6       0      0 :::123                  :::*                                5230/ntpd
udp6       0      0 :::37588                :::*                                707/dhclient
```
