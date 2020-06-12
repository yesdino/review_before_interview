# 目录

[toc]

---

[转载！出处：Linux（CentOS7）常用命令详解 史上最全！！！！！！！！！](https://blog.csdn.net/weixin_39951988/article/details/87613816)


**`.`** ：代表当前路径

**`..`** ：代表上一级目录

**`~`** ：代表用户目录路径


# 常用命令详解

## ls

ls是英文单词 list 的缩写.用来查看文件目录的属性。

例如直接输入 ls 按回车，查看根目录的文件以及目录。
```
[root@172 ~]# ls
docker  Kanban  project  test.py  vimrc
```

### `ls -l` / `ll`

l 参数代表以列表的方式显示。两种指令效果相同
```
[root@172 ~]# ls -l
total 20
drwxr-xr-x  5 root root 4096 May 28 16:19 docker
drwxr-xr-x 13 root root 4096 Sep 28  2019 Kanban
drwxr-xr-x  5 root root 4096 May 29 14:16 project
-rw-r--r--  1 root root   11 Aug 23  2019 test.py
-rw-r--r--  1 root root  458 Jun  3 13:29 vimrc

[root@172 ~]# ll
total 20
drwxr-xr-x  5 root root 4096 May 28 16:19 docker
drwxr-xr-x 13 root root 4096 Sep 28  2019 Kanban
drwxr-xr-x  5 root root 4096 May 29 14:16 project
-rw-r--r--  1 root root   11 Aug 23  2019 test.py
-rw-r--r--  1 root root  458 Jun  3 13:29 vimrc
(1)(2)     (3) (4)  (5)  (6) (7)           (8)
```

- **(1)第一个字符** 
    - **`d`** 代表这是一个目录文件。
    - **`‐`**  代表普通文件
    - **`c`**  字符设备文件
    - **`b`**  块设备文件
    - **`p`**  管道文件
    - **`l`**  链接文件
    - **`s`**  socket文件

- **(2)后面的 `rwxr‐xr‐x` 字符**
代表 user、group、other 对文件所拥有的权限，
    - **`rwx`** 代表该用户拥有 **读写执行** 的权限。
    - **`r‐x`** 代表同一组的用户拥有的 **读** 和 **执行** 权限，
    - **`r‐x`** 代表其他用户拥有 **读** 和 **执行** 权限。

- (3) 代表 **文件硬链接的计数**，表示该文件有两个硬链接。
- (4) where 文件 **所属的用户名**。
- (5) where  文件 **所属的用户组**。
- (6) 4096 文件 **大小**，单位字节。
- (7) 6月 25 16:53  文件 **最后被修改的日期。**
- (8) 文件名

### `ls -a`

a 参数代表 all 的意思，表示把所有的文件都罗列出来，包括隐藏文件，点号开头的在 Linux 中都表示隐藏文件。

```
[root@172 ~]# ls -a
.   .bash_history  .bash_profile  .cache   .cshrc  Kanban  .mysql_history  .pki     .pydistutils.cfg  .rediscli_history  .tcshrc  .vim      .viminfo.tmp  .vimrc
..  .bash_logout   .bashrc        .config  docker  .local  .pip            project  .python_history   .ssh               test.py  .viminfo  vimrc
```
ls 的更多参数直接看

```
[root@172 ~]# ls --help
Usage: ls [OPTION]... [FILE]...
List information about the FILEs (the current directory by default).
Sort entries alphabetically if none of -cftuvSUX nor --sort is specified.

Mandatory arguments to long options are mandatory for short options too.
  -a, --all                  do not ignore entries starting with .
  -A, --almost-all           do not list implied . and ..
      --author               with -l, print the author of each file
  -b, --escape               print C-style escapes for nongraphic characters
      --block-size=SIZE      scale sizes by SIZE before printing them; e.g.,
                               '--block-size=M' prints sizes in units of
                               1,048,576 bytes; see SIZE format below
  -B, --ignore-backups       do not list implied entries ending with ~
  ......
```
<br>


## stat
查看文件的访问时间，修改时间等

```
[root@172 ~]# ls
docker  Kanban  project  test.py  vimrc
```
```
[root@172 ~]# stat docker
  File: ‘docker’
  Size: 4096            Blocks: 8          IO Block: 4096   directory
Device: fd01h/64769d    Inode: 262415      Links: 5
Access: (0755/drwxr-xr-x)  Uid: (    0/    root)   Gid: (    0/    root)
Access: 2020-06-01 09:25:57.413405564 +0800
Modify: 2020-05-28 16:19:44.451207858 +0800
Change: 2020-05-28 16:19:44.451207858 +0800
 Birth: -
```
访问时间 `Access`，是指通过指令如 `cat`、`vi` 等来查看的文件的最近一次时间。
更改时间 `Modify`，是指修改文件内容的最近一次时间。
改动时间 `Change`，是指修改文件属性的最近一次时间。
注意：访问时间是内容更改后，第一次访问的时间，后面再次访问的时候访问时间不会改变

## cd

```
cd -        # 回上一次所在的目录
cd ~ 或 cd  # 回当前用户的主目录
cd /        # 回根目录
cd ..       # 回当前目录的上一层目录
```


## pwd

print working diretory, 显示当前所在路径


## which
寻找可执行文件 ，并在 **PATH 环境变量** 里面寻找

```
[root@172 ~]# which python
/usr/bin/python

[root@172 ~]# which python3.6
/usr/local/python3/bin/python3.6

[root@172 ~]# which pg_dump
/usr/bin/which: no pg_dump in (/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin:/usr/local/python3/bin)

[root@172 ~]# which psql
/usr/bin/which: no psql in (/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin:/usr/local/python3/bin)
```

## touch 
将每个文件的 **访问及修改时间都更新为目前的时间**。
如果文件不存在，则创建一个字节数为 0 的文件。
```
‐a           # 只更新访问时间，不改变修改时间
‐c           # 不创建不存在的文件
‐m           # 只更新修改时间，不改变访问时间
‐r file      # 使用文件 file 的时间更新文件的时间
‐t           # 将时间修改为参数指定的日期, 如：07081556 代表 7 月 8 号 15 点 56 分
```

## mkdir 
创建目录 。 英文缩写 make directory 

可以一次创建多个。OPTION 如果是­ `p`，表示可以连同父目录一起创建


## rmdir 命令 

**删除<u>空目录</u>**，可以一次删除多个。英文缩写 remove directory

OPTION 如果是­ `p`，表示可以连同空的父目录一起删除。
但是一旦父目录中还包含其他文件，则删除失败。

## rm 命令 

删除文件或目录。英文缩写 remove

可以用来删除普通文件，
也可以用来删除目录，特别用来删除目录中嵌套有子目录的目录文件。

常用参数：

```
‐f  ‐‐force         # 强制删除，不询问是否要删除。
‐r  ‐‐recursive     # 递归删除，包括文件夹中的内容。
```

## mv 

可以用来移动文件夹或者文件，也可以用来 **更改文件名**。
英文缩写 move

```
mv file /           # 把文件file移动到根目录中
mv file file_bak    # 把文件 file 重命名为 file_bak。
```

## cp 
拷贝文件/目录。
英文缩写 copy

```
cp file file_bak    # 拷贝一份file为file_bak
cp dir dir_bak ‐r   # 拷贝一个目录 dir 并命名为 dir_bak, ‐r 参数代表递归拷贝，把 dir 目录中的文件也拷贝过去
```
拷贝目录并 重命名，可直接用于 **目录备份**
```
[dino@172 test]$ ls
celery_test  ch01  ch02  git_test  read_execl

[dino@172 test]$ cp ch01 ch01_cp -r
[dino@172 test]$ ls
celery_test  ch01  ch01_cp  ch02  git_test  read_execl
```


## cat 

用来查看文件内容，以及 **将几个文件连成一个文件**，
英文缩写 concatenate (连锁)

不填文件参数，默认的情况下是从标准输入中获取内容：

- 查看文件： cat fileName
- 将文件file1 file2连成file3文件
    ```
    cat file1 file2 > file3
    ```

## more 
more 是我们最常用的工具之一，
最常用的就是 **显示输出的内容，然后根据窗口的大小进行分页显示**，
并且提示文件的百分比。

参数如下：

```
+num    # 从第 num 行开始显示；
‐num    # 定义每屏显示 num 行；
```

more 区域打开之后的快捷键：
```
f / 空格        # 向下显示一屏
b               # 返回上一屏
n Enter         # 键可以向下滚动显示 n 行 （默认为 1 行）
q               # 退出
```

## less 
less 工具也是对文件或其它输出进行分页显示的工具

参数如下:
```
‐f    # 强制打开文件，二进制文件显示时，不提示警告；
‐N    # 在每行前输出行号；
```

less 区域打开之后的快捷键：
![img](https://img-blog.csdnimg.cn/20190218154036725.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTk1MTk4OA==,size_16,color_FFFFFF,t_70)


## locate （全盘寻找文件
**全盘寻找文件**。文件名部分匹配，只要有包含该字符串的都罗列出来。
这个指令查找速度很快，<u>它需要一个数据库</u>，这个数据库由每天的例行工作（crontab）程序来更新。
当我们建立好这个数据库后，就可以方便地来搜寻所需文件了。

马上创建的文件没办法使用 locate 查找到:
如果想马上更新可以使用一下指令：**`updatedb`**


## find （直接在全文件系统上搜寻
**直接在全文件系统上搜寻**。功能强大，速度慢。

格式：

```py
find [path] [‐option] [ ‐print ‐exec ‐ok command ] {} \;

path:       # 要执行查找的目录。
‐option:    # 查找的具体方法。
‐print：    # find命令将匹配的文件输出到标准输出。
‐exec：     # find命令对匹配的文件执行该参数所给出的shell命令。相应命令的形式为'command' {} \;，注意{}和 \；之间的空格。
‐ok：       # 和‐exec的作用相同，只不过以一种更为安全的模式来执行该参数所给出的shell命令，在执行每一个命令之前，都会给出提示，让用户来确定是否执行。
```

```py
find / ‐name filename   # 在根目录里面搜索【文件名为 filename 的文件
find /etc ‐name *s*     # 在目录里面搜索【带有s的文件
find /etc ‐name *S      # 在目录里面搜索【以 s 结尾的文件
find /etc ‐name s*      # 在目录里面搜索【以 s 开头的文件
find / ‐amin ‐10        # 在系统中搜索【最后 10 分钟访问的文件
find / ‐atime ‐2        # 查找在系统中【最后 48 小时访问的文件
find / ‐mmin ‐5         # 查找在系统中【最后 5 分钟修改过的文件
find / ‐mtime ‐1        # 查找在系统中【最后 24 小时修改过的文件
find / ‐ctime ‐1        # 查找在系统中【最后 24 小时被改变状态的文件
find / ‐user username   # 查找在系统中【属于用户 username 的文件
find / ‐group groupname # groupname 查找在系统中属于 groupname 的文件
find / ‐empty           # 查找在系统中【为空的文件或者是文件夹
find / ‐inum 3          # 查找【inode 号为 3 的文件
find / ‐type d          # 查找【文件类型为文件夹的文件 d 为文件夹
                                f     # 普通文件
                                d     # 目录文件
                                l     # 链接文件
                                b     # 块设备文件
                                c     # 字符设备文件
                                p     # 管道文件
                                s     # socket文件
```

## grep
搜索内容中是否包含指定的字符串，并打印出该行。


常用参数有：

```py
‐i    ‐‐ignore‐case   # 忽略字符大小写的差别。
‐v                    # 输出没有指定字符串的文件
‐c                    # 只输出匹配行的计数。
‐R                    # 连同子目录中所有文件一起查找。
```

## ln 
ln是英文单词link的缩写，用来创建链接的命令。
Linux链接分两种，
一种被称为硬链接（Hard Link），
另一种被称为符号链接（Symbolic Link）。
默认情况下，ln命令产生硬链接。

- **【硬链接】**

硬链接指通过索引节点来进行链接。
在Linux的文件系统中，保存在磁盘分区中的文件不管是什么类型都给它分配一个编号，
称为 **索引节点号** (Inode Index)。
在Linux中，**<u>多个文件名指向同一索引节点</u>**，一般这种链接就是硬链接。

<u>硬链接的作用是 **允许一个文件拥有多个有效路径名**，
这样用户就可以建立硬链接到重要文件，**以防止“误删”**。</u>

**如果有多个硬链接，只删除一个链接并不影响本身和其它的链接，
只有当最后一个链接被删除后，文件的才会被正在删除。**
也就是说，**==文件真正删除的条件是与之相关的所有硬链接文件均被删除==**。

给flie文件创建一个硬链接
```
touch file
ln file file_hard
```

- **【软链接】**

另外一种链接称之为符号链接（Symbolic Link），也叫软链接。
软链接文件有 **==类似于Windows的快捷方式==**。
它实际上是一个特殊的文件。
符号链接文件实际上是一个文本文件，其中包含的有另一文件的位置信息。

给 file 文件创建一个软链接
```
touch file
ln ‐s file flie_soft
```
注意: 软链接的时候尽量使用绝对路径，避免由于链接文件移动后，造成文件失效。

## wc 
Linux系统中的wc为英文 Word Count 的缩写，


**命令功能：**
统计指定文件中的字节数、字数、行数，并将统计结果显示输出。
如果没有给出文件名，则从标准输入读取。
wc 同时也给出所指定文件的总统计数。

命令参数：
```
‐c      # 统计字节数。 
‐l      # 统计行数。 
‐m      # 统计字符数。这个标志不能与 ‐c 标志一起使用。 
‐w      # 统计字数。一个字被定义为由空白、跳格或换行字符分隔的字符串。 
‐L      # 打印最长行的长度。 
```

## od 

od是英文 octal dump 的缩写

**命令功能：**
把文件用 8 进制或者其他的格式显示出来，
通常用于查看特殊格式文件的内容，可以用来查看不可见字符。


## du (所占的空间大小
du是英文 Disk usage 的缩写

**命令功能：**
计算某个目录在硬盘中所占的空间大小，默认情况下以 kb 为单位。
通过递归统计每一个目录中所占用的空间大小。

![img](https://img-blog.csdnimg.cn/20190218173645611.PNG)



## df（磁盘使用情况
df是英文Disk free的缩写，

**命令功能：**
统计磁盘使用情况。
![img](https://img-blog.csdnimg.cn/20190218173747526.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTk1MTk4OA==,size_16,color_FFFFFF,t_70)



## gedit 
gedit全称 GNU edit 是一个文本编辑器，类似windows里面的txt文本编辑器。编辑file文本。

## 管道命令
用法：`command 1 | command 2` 

功能：把第一个命令command 1执行的结果作为command 2的输入。

管道命令操作符是：”|”它只能处理经由前面一个指令传出的正确输出信息，
对错误信息信息没有直接处理能力.


## 重定向 
在shell中，标准输入是0，标准输出是1，标准错误是2.
使用>表示重定向。
**`1>`** 表示标准输出重定向，
**`2>`** 表示标准错误重定向。
默认情况下>表示输出重定向。

例如：

```py
ls > list.txt                       # ls的输出重定向到文件list.txt中。                     
find / ‐name "*.c" 2>/dev/null      # 标准错误重定向到无底洞文件。     
find / ‐name "*.c" 2>/dev/null      # 标准错误重定向到无底洞文件。     
find / ‐name "*.c" >/dev/null 2>&1  # 标准输出、标准错误重定向到无底洞文件。
```


## 后台运行
Linux中可以使用 **`&`** ，让程序在后台运行。
如：`cat &`


## awk 
**命令功能：**
把文件逐行的读入，以空格为默认分隔符将每行切片，
切开的部分再进行各种分析处理。
```py
格式：
awk [‐F field‐separator] 'commands' [input‐file(s)]
```

```
commands 是真正awk命令，
[­F 域分隔符]是可选的。 
input­file(s) 是待处理的文件。
```
print 是awk打印指定内容的主要命令, `$1` 分割出来的第一段，`$2`分割出来的第二段，依次类推，`$0`代表所有

字段例如：
```
ls ‐l | awk '{print $1 "\t" $2 "\t" $3 "\t" $4}'
```

将`/proc/meminfo`文件中的字段提取出来，并且在每个字段前面添加meminfo：

```
awk ‐F ':' '{print "meminfo:" $1}' /proc/meminfo
```

继续看 [Linux（CentOS7）下文件操作（权限、打包、解包操作）](https://blog.csdn.net/weixin_39951988/article/details/87687242)


<br>

<u></u>