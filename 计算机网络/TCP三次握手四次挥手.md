# 目录

[toc]

---


[出处：TCP的三次握手与四次挥手理解及面试题（很全面）](https://blog.csdn.net/qq_38950316/article/details/81087809)




<img style="width:600px" src="https://img-blog.csdn.net/20180717201939345?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4OTUwMzE2/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70"></img>


<span style="color:FireBrick; font-weight:bold">序列号 `seq` ：</span>
占 4 个字节，用来标记数据段的顺序。
TCP 把连接中 <u>发送的所有数据 **字节** 都编上一个序号</u>，
**第一个字节的编号由本地随机产生；**
给字节编上序号后，就给每一个报文段指派一个序号；
序列号 seq 就是这个报文段中的第一个字节的数据编号。

<span style="color:FireBrick; font-weight:bold">确认号 `ack` ：</span>
占 4 个字节，**期待收到**对方下一个报文段的第一个数据字节的序号；
序列号表示报文段携带数据的第一个字节的编号；
而确认号指的是期望接收到下一个字节的编号；
因此 ==当前报文段最后一个字节的编号 +1== 即为确认号。

<span style="color:FireBrick; font-weight:bold">确认 `ACK` ：</span>
标志位，占 1 位，仅当 
`ACK=1` 时，确认号字段才有效。 
`ACK=0` 时，确认号无效

<span style="color:FireBrick; font-weight:bold">同步 `SYN` ：</span>
标志位，连接建立时用于同步序号。
当 **`SYN=1, ACK=0`** 时表示：这是一个连接请求报文段。
若同意连接，则在响应报文段中使得 **`SYN=1, ACK=1`** 。
因此， **`SYN=1`** 表示这是一个连接请求，或连接接受报文。 
<u>**SYN 这个标志位只有在 TCP 建立连接时才会被置 1 ，
握手完成后 SYN 标志位被置 0**</u>。

<span style="color:FireBrick; font-weight:bold">终止 `FIN` ：</span>
标志位，用来释放一个连接。 
**`FIN=1`** 表示：此报文段的发送方的数据已经发送完毕，并要求释放运输连接

PS ： 
==**`ACK, SYN, FIN`** 这些大写的单词表示标志位，其值要么是 1 ，要么是 0 ； 
**`ack, seq`** 小写的单词表示序号==。
<br>


## 标志位

- **`URG`**	：紧急指针是否有效。为1，表示某一位需要被 **优先处理**
- **`ACK`**	：确认号是否有效，一般置为1。
- **`PSH`**	：提示接收端应用程序立即从TCP缓冲区把数据读走。
- **`RST`**	：对方要求重新建立连接，复位。
- **`SYN`**	：请求建立连接，并在其序列号的字段进行序列号的初始值设定。
- 建立连接，设置为1
- **`FIN`** ：希望断开连接。
<br>



## 三次握手

<img style="width:600px" src="https://img-blog.csdn.net/20180717202520531?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4OTUwMzE2/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70"></img>


第 **①** 次握手：`client --> server: `
 **`SYN = 1, seq = x`** ：
```html
SYN = 1: 请求建立 client --> server 方向上的连接通道
seq = x: client --> server 方向 报文的第一个字节的序列号
```
建立连接时，
客户端发送 syn 包（`syn=x`）到服务器，并进入 **`SYN_SENT`** 状态，等待服务器确认； 
（SYN ：同步序列编号`Synchronize Sequence Numbers`）。

第 **②** 次握手：`server <-- client: `
 **`SYN = 1, ACK = 1, seq = y, ack = x+1`** ：
```html
SYN = 1  : 请求建立 server <-- client 方向上的连接通道
ACK = 1  : 标示位，表 ack 序列号有效
seq = y  : server --> client 方向 报文的第一个字节的序列号
ack = x+1: 确认ack, 表示已经收到了 x，期待下一个收到的报文序列号为 x+1
```
服务器收到 syn 包，必须确认客户的 SYN （`ack=x+1`），
同时自己也发送一个 SYN 包（`syn=y`），即 **`SYN`**+**`ACK`** 包，
此时服务器进入 **`SYN_RECV`** 状态；

第 **③** 次握手：`client --> server: `
 **`ACK = 1, seq = x+1, ack = y+1`** ：
```html
ACK = 1     : 标示位，表 ack 序列号有效
seq = x+1   : 由于上一个收到的 ack 表示期待接收 x+1 的序列号数据，所以这个报文就传输 x+1 的序列号数据到 server 端
ack = y+1   : 表示我 client 已经收到了 y, 期待下一个从 server 端收到的序列号为 y+1
```
客户端收到服务器的 **`SYN`**+**`ACK`** 包，
向服务器发送确认包 ACK (`ack=y+1`），
此包发送完毕，客户端和服务器进入 **`ESTABLISHED`** （ TCP 连接成功）状态，
完成三次握手。



## 四次挥手

<img style="width:600px" src="https://img-blog.csdn.net/20180717204202563?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4OTUwMzE2/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70"></img>


1）客户端进程发出连接释放报文，并且停止发送数据。
释放数据报文首部，`FIN=1` ，其序列号为 `seq=u` 
（u 等于前面已经传送过来的数据的最后一个字节的序号加 1）。
此时，**客户端进入 **`FIN-WAIT-1`** （终止等待 1）状态**。
TCP 规定，<u>`FIN` 报文段即使不携带数据，也要消耗一个序号</u>。



2）服务器收到连接释放报文，发出确认报文， `ACK=1, ack=u+1` ，
并且带上自己的序列号 `seq=v` ，
此时，**服务端就进入了 `CLOSE-WAIT`（关闭等待）状态**。
TCP 服务器通知高层的应用进程，客户端向服务器的方向就释放了，这时候处于半关闭状态，
即客户端已经没有数据要发送了，但是服务器若发送数据，客户端依然要接受。
这个状态还要持续一段时间，也就是整个 CLOSE-WAIT 状态持续的时间。

3）客户端收到服务器的确认请求后，此时，
**客户端就进入 `FIN-WAIT-2`（终止等待 **2** ）状态，**
等待服务器发送连接释放报文（在这之前还需要接受服务器发送的最后的数据）。

4）服务器将最后的数据发送完毕后，就向客户端发送连接释放报文， `FIN=1, ack=u+1` ，
由于在半关闭状态，服务器很可能又发送了一些数据，假定此时的序列号为 `seq=w` ，
此时，**服务器就进入了 `LAST-ACK`（最后确认）状态**，等待客户端的确认。

5）客户端收到服务器的连接释放报文后，必须发出确认， `ACK=1,  ack=w+1` ，而自己的序列号是 `seq=u+1` ，此时，**客户端就进入了 `TIME-WAIT`（时间等待）状态**。
注意此时 TCP 连接还没有释放，必须经过 2 MSL （最长报文段寿命）的时间后，当客户端撤销相应的 TCB 后，才进入 **`CLOSED`** 状态。

6）**服务器只要收到了客户端发出的确认，立即进入 `CLOSED` 状态**。
同样，撤销 TCB 后，就结束了这次的 TCP 连接。
可以看到，服务器结束 TCP 连接的时间要比客户端早一些。

<br>


## 常见面试题

### 1、为什么连接的时候是三次握手，关闭的时候却是四次握手？

答：
因为当 Server 端收到 Client 端的 SYN 连接请求报文后，可以直接发送 SYN+ACK 报文。
其中 ACK 报文是用来应答的， SYN 报文是用来同步的。
但是关闭连接时，当 Server 端收到 FIN 报文时，很可能并不会立即关闭 SOCKET ，
所以只能先回复一个 ACK 报文，告诉 Client 端， " 你发的 FIN 报文我收到了 " 。
**只有等到我 Server 端所有的报文都发送完了，我才能发送 FIN 报文**，因此不能一起发送。
故需要四步握手。

### 2、为什么 `TIME_WAIT` 状态需要经过 2MSL (最大报文段生存时间)才能返回到 `CLOSE` 状态？

答：虽然按道理，四个报文都发送完毕，我们可以直接进入 CLOSE 状态了，
但是我们必须假象网络是不可靠的，**最后一个 ACK 有可能丢失**。
所以 TIME_WAIT 状态就是用来重发可能丢失的 ACK 报文。
**在 Client 发送出最后的 ACK 回复，但该 ACK 可能丢失。 
Server 如果没有收到 ACK ，将不断重复发送 FIN 片段。**
所以 Client 不能立即关闭，它必须确认 Server 接收到了该 ACK 。 

Client 会在发送出 ACK 之后进入到 TIME_WAIT 状态。 
**Client 会设置一个计时器，等待 2MSL 的时间。
如果在该时间内再次收到 `FIN` ，那么 Client 会重发 `ACK` 并再次等待 2MSL**。

所谓的 2MSL 是两倍的 **`MSL`**`(Maximum Segment Lifetime)` 。 
**`MSL`** 指一个片段在网络中最大的存活时间， 
**`2MSL` 就是一个发送和一个回复所需的最大时间。**
==如果直到 2MSL，Client 都没有再次收到 FIN，
那么 Client 推断 ACK 已经被成功接收，则结束 TCP 连接==。


### 3、为什么不能用两次握手进行连接？

答： 3 次握手完成两个重要的功能，既要双方做好发送数据的准备工作 ( 双方都知道彼此已准备好 ) ，也要允许双方就初始序列号进行协商，这个序列号在握手过程中被发送和确认。

现在把三次握手改成仅需要两次握手，死锁是可能发生的。
作为例子，考虑计算机 Server 和 Client 之间的通信，
假定 Client 给 Server 发送一个连接请求分组， Server 收到了这个分组，并发送了 ack 确认应答分组。

按照两次握手的协定， Server 认为连接已经成功地建立了，可以开始发送数据分组。
<u>可是， Client 在 Server 的 ack 应答分组在传输中被丢失的情况下，
将不知道 Server 是否已准备好，不知道 Server 建立什么样的序列号， 
Client 甚至怀疑 Server 是否收到自己的连接请求分组。</u>

在这种情况下， Client 认为连接还未建立成功，
将忽略 Server 发来的任何数据分组，只等待连接确认应答分组。
而 Server 在发出的分组超时后，重复发送同样的分组。
这样就形成了 ==**死锁**==。


### 4、如果已经建立了连接，但是客户端突然出现故障了怎么办？

TCP 还设有一个保活计时器，显然，客户端如果出现故障，服务器不能一直等下去，白白浪费资源。

服务器每收到一次客户端的请求后都会重新复位这个计时器，时间通常是设置为 2 小时，若两小时还没有收到客户端的任何数据，服务器就会发送一个 **==探测==** 报文段，以后每隔 75 秒钟发送一次。
**若一连发送 10 个探测报文仍然没反应，服务器就认为客户端出了故障，接着就关闭连接**。



## 直接在 Linux 中抓包查看握手挥手

[link](https://www.bilibili.com/video/BV1Ma4y1Y7Xg?p=3)


</u>




<br>
<br><br><br><br><br><br>
<br><br><br><br><br><br>
<br><br><br><br><br><br>
<br><br><br><br><br><br>







