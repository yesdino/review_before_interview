[出处](https://www.cnblogs.com/sparkbj/p/7161669.html)

1.列出所有打开的文件:

```py
lsof
```

备注: 如果不加任何参数，就会打开所有被打开的文件，建议加上一下参数来具体定位

2. 查看谁正在使用某个文件

```py
lsof   /filepath/file
```

3.递归查看某个目录的文件信息

```py
lsof +D /filepath/filepath2/
```

备注: 使用了+D，对应目录下的所有子目录和文件都会被列出

4. 比使用+D选项，遍历查看某个目录的所有文件信息 的方法

```py
lsof | grep ‘/filepath/filepath2/’
```

5. 列出某个用户打开的文件信息

```py
lsof  -u username
```

备注: -u 选项，u 其实是 user 的缩写

6. 列出某个程序所打开的文件信息

```py
lsof -c mysql
```

备注: -c 选项将会列出所有以 mysql 开头的程序的文件，其实你也可以写成`lsof | grep mysql`,但是第一种方法明显比第二种方法要少打几个字符了

7. 列出多个程序多打开的文件信息

```py
lsof -c mysql -c apache
```

8. 列出某个用户以及某个程序所打开的文件信息

```py
lsof -u test -c mysql
```

9. 列出除了某个用户外的被打开的文件信息

```py
lsof   -u ^root
```

备注：^这个符号在用户名之前，将会把是 root 用户打开的进程不让显示

10. 通过某个进程号显示该进行打开的文件

```py
lsof -p 1
```

11. 列出多个进程号对应的文件信息

```py
lsof -p 123,456,789
```

12. 列出除了某个进程号，其他进程号所打开的文件信息

```py
lsof -p ^1
```

13 . 列出所有的网络连接

```py
lsof -i
```

14. 列出所有tcp 网络连接信息

```py
lsof  -i tcp
```

15. 列出所有 udp 网络连接信息

```py
lsof  -i udp
```

16. 列出谁在使用某个端口

```py
lsof -i :3306
```

17. 列出谁在使用某个特定的 udp 端口

```py
lsof -i udp:55
```

特定的 tcp 端口

```py
lsof -i tcp:80
```

18. 列出某个用户的所有活跃的网络端口

```py
lsof  -a -u test -i
```

19. 列出所有网络文件系统

```py
lsof -N
```

20.域名socket文件

```py
lsof -u
```

21.某个用户组所打开的文件信息

```py
lsof -g 5555
```

22. 根据文件描述列出对应的文件信息

```py
lsof -d description(like 2)
```

23. 根据文件描述范围列出文件信息

```py
lsof -d 2-3
```



```py
lsof `which httpd`      //那个进程在使用apache的可执行文件 
lsof /etc/passwd        //那个进程在占用/etc/passwd 
lsof /dev/hda6          //那个进程在占用hda6 
lsof /dev/cdrom         //那个进程在占用光驱 
lsof -c sendmail        //查看sendmail进程的文件使用情况 
lsof -c courier -u ^zahn //显示出那些文件被以courier打头的进程打开，但是并不属于用户zahn 
lsof -p 30297       //显示那些文件被pid为30297的进程打开 
lsof -D /tmp        显示所有在/tmp文件夹中打开的instance和文件的进程。但是symbol文件并不在列
lsof -u1000         //查看uid是100的用户的进程的文件使用情况 
lsof -utony         //查看用户tony的进程的文件使用情况 
lsof -u^tony        //查看不是用户tony的进程的文件使用情况(^是取反的意思) 
lsof -i             //显示所有打开的端口 
lsof -i:80          //显示所有打开80端口的进程 
lsof -i -U          //显示所有打开的端口和UNIX domain文件 
lsof -i UDP@[url]www.akadia.com:123     //显示那些进程打开了到www.akadia.com的UDP的123(ntp)端口的链接 
lsof -i tcp@ohaha.ks.edu.tw:ftp -r      //不断查看目前ftp连接的情况(-r，lsof会永远不断的执行，直到收到中断信号,+r，lsof会一直执行，直到没有档案被显示,缺省是15s刷新) 
lsof -i tcp@ohaha.ks.edu.tw:ftp -n      //lsof -n 不将IP转换为hostname，缺省是不加上-n参数
```