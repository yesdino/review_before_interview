[toc]

---

[出处](https://www.cnblogs.com/wj-1314/p/9056555.html)

# Python GIL（Global Interpreter Lock)

# 1. 前言

定义：
```
In CPython, the global interpreter lock, or GIL, is a mutex that prevents multiple
native threads from executing Python bytecodes at once. This lock is necessary mainly
because CPython’s memory management is not thread-safe. (However, since the GIL
exists, other features have grown to depend on the guarantees that it enforces.)
```
结论：
在 `Cpython` 解释器中，同一个进程下开启的多线程，
<u>**同一时刻只能有一个线程执行**</u>，无法利用多核优势

首先需要明确的一点是 <u>GIL 并不是 Python 的特性</u>，它是在实现 Python 解析器 (CPython) 时所引入的一个概念。 
就好比 C++ 是一套语言（语法）标准，但是可以用不同的编译器来编译成 可执行代码。有名的编译器例如 GCC ， INTEL C++ ， Visual C++ 等。

Python 也一样，
同样一段代码可以通过 `CPython`, `PyPy`, `Psyco` 等不同的 **Python 执行环境** 来执行。
像其中的 JPython 就没有 GIL 。

**然而** 因为 CPython 是大部分环境下默认的 Python 执行环境。
所以在很多人的概念 里 CPython 就是 Python ，
也就想当然的把 GIL 归结为 Python 语言的缺陷。
 
所以这里要先明确一点：
==GIL 并不是 Python 的特性， Python 完全可以不依赖于 GIL==

<br>

# 2. **GIL**：保证同一时间只能有一个线程执行
　　
==GIL 本质就是一把 **互斥锁**。== 
用于 <u>保证同一时间只能有一个线程来执行</u>

既然是互斥锁，所有互斥锁的本质都一样，都是将 <u>**并发运行变成串行**</u>，
以此来 <u>控制同一时间内共享数据 ==只能被一个任务所修改== ，进而保证数据安全。</u>


可以肯定的一点是：
<u>保护不同的数据的安全，就应该加不同的锁。 </u>

要想了解 GIL ，首先确定一点：
<u>每次执行 python 程序，都会产生一个独立的进程。</u>
例如 `python test.py`, `python aaa.py`, `python bbb.py` 会产生 3 个不同的 python 进程

验证 python test.py 只会产生一个进程：
```py
# test.py 内容
import os,time
print(os.getpid())
time.sleep(1000)

# 运行 test.py
python3 test.py

# 在windows下
tasklist |findstr python

# 在linux下
ps aux |grep python
```

在一个 python 的进程内，
不仅有 test.py 的主线程 或者 由该主线程开启的其他线程，
还有解释器开启的垃圾回收等解释器级别的线程。

总之，所有线程都运行在这一个进程内，在这个进程内：

- 1。 **所有数据都是共享的**。
这其中，代码作为一种数据也是被所有线程共享的 （ test.py 的所有代码以及 Cpython 解释器的所有代码） 
例如： test.py 定义一个函数 work （代码内容如下图），在进程内所有线程都能访问到 work 的代码， 于是我们可以开启三个线程然后 target 都指向该代码，能访问到意味着就是可以执行。 
- 2。 所有线程的任务，都需要 <u>将**任务的代码** 当做参数传给 **解释器** 的代码去执行</u>。
即所有的线程要想运行自己的任务，首先需要解决的是能够访问到解释器的代码。

综上： 
如果多个线程的 target=work ，
1. 那么执行流程是 多个线程先访问到解释器的代码，即拿到执行权限，
2. 然后将 target 的代码交给解释器的代码去执行。
解释器的代码是所有线程共享的，所以垃圾回收线程也可能访问到解释器的代码而去执行。

这就导致了一个问题 : 
对于同一个数据 100 ，可能线程 1 执行 `x=100` 的同时，而垃圾回收执行的是回收 100 的操作。

解决这种问题没有什么高明的方法，就是 <u>**加锁处理**</u>。
如下图的 GIL ，保证 <u>python 解释器同一时间只能执行一个任务的代码</u>

![gil](https://images2018.cnblogs.com/blog/1226410/201805/1226410-20180518154417222-797641320.png)


<br>

# 3. **GIL 与 Lock**：两把不同的锁

机智的同学可能会问到这个问题： 
Python 已经有一个 GIL 来保证同一时间只能有一个线程来执行了，为什么这里还需要 lock ? 
首先，我们需要达成共识：
锁的目的是为了保护共享的数据，同一时间只能有一个线程来修改共享的数据。

然后，我们可以得出结论：
<u>保护不同的数据就应该加不同的锁。 </u>

最后，问题就很明朗了， 
==**GIL 与 Lock 是两把锁，保护的数据不一样**==。
- GIL 是 **解释器级别** 的（当然保护的就是解释器级别的数据，比如垃圾回收的数据）。
- Lock 是保护 **用户自己开发的** 应用程序的数据。
很明显 GIL 不负责这件事，只能用户自定义加锁处理。即 Lock 。

如下图：
![LOCK](https://images2018.cnblogs.com/blog/1226410/201805/1226410-20180518154550806-814189263.png)


执行过程 **步骤分析**：
1 、 100 个线程去抢 GIL 锁，即抢执行权限。 
2 、肯定有一个线程先抢到 GIL （暂且称为线程 1 ），然后开始执行，一旦执行就会拿到 `lock.acquire()` 
3 、极有可能线程 1 还未运行完毕，就有另外一个线程 2 抢到 GIL ，然后开始运行。
但 <u>线程 2 发现互斥锁 lock 还未被线程 1 释放</u>，于是阻塞，被迫交出执行权限（==两把锁结合控制==）。即释放 GIL 。
4 、直到线程 1 重新抢到 GIL ，开始从上次暂停的位置继续执行，直到正常释放互斥锁 lock。
然后其他的线程再重复 2 3 4 的过程

```py
# 代码示例：
# _*_ coding: utf-8 _*_
from threading import Thread
from threading import Lock
import time
 
N = 100
def task():
    global N
    mutex.acquire()     # 线程抢执行权限
    temp = N
    time.sleep(0.1)
    N = temp - 1
    mutex.release()     # 释放执行权限
 
if __name__ == '__main__':
    mutex = Lock()
    thread_lis = []
    for i in range(100):
        t = Thread(target=task) # 每个线程的任务是执行 task()
        thread_lis.append(t)
        t.start()
 
    for t in thread_lis:
        t.join()

    print("主", N)      # 主 0

# 结果：
# 肯定为0，由原来的并发执行变为串行，牺牲了执行效率保证了数据安全.
# 不加锁则结果可能为99
```

<br>

# 4. **GIL 与多线程**：计算密集型 还是 I/O 密集型

有了 GIL 的存在，同一时刻同一进程中只有一个线程被执行。

有的同学立马质问：
==**进程** 可以利用多核，但是**开销大**。
**多线程** 开销小，但却**无法利用多核优势**。==

要解决这个问题，我们需要在几个点上达成一致：
1、cpu 到底是用来做计算的，还是用来做 I/O 的？ 
2、多 cpu ，意味着可以有多个核并行完成计算，所以多核提升的是计算性能。 
3、每个 cpu 一旦遇到 I/O 阻塞，仍然需要等待，所以多核对 I/O 操作没什么用处。

<br>

**类比：**
一个工人：相当于 cpu 。
计算：相当于 工人在干活。
I/O 阻塞：相当于 <u>为工人干活提供所需原材料的过程。</u>

```
工人干活的过程中如果没有原材料了，则工人干活的过程需要停止，直到等待原材料的到来。

如果你的工厂干的大多数任务都要有准备原材料的过程（ I/O 密集型），
那么你有再多的工人，意义也不大。
还不如一个人，在等材料的过程中让工人去干别的活。

反过来讲，如果你的工厂原材料都齐全，那当然是工人越多，效率越高
```

**结论：**
对计算来说， cpu 越多越好。
但是对于 I/O 来说，再多的 cpu 也没用。

当然对运行一个程序来说，随着 cpu 的增多执行效率肯定会有所提高（不管 提高幅度多大，总会有所提高），这是因为 <u>一个程序基本上不会是纯计算或者 纯 I/O 。</u>
所以我们只能 <u>相对的去看一个程序到底是 **计算密集型** 还是 **I/O 密集型**，</u>
从而进一步分析 python 的多线程到底有无用武之地。

<br>

**举例分析：**
假设我们有 4个任务 需要处理，处理方式肯定是需要玩出并发的效果。
解决方案可以是：
方案 1：开启四个**进程**
方案 2：一个进程下，开启四个**线程**

- **单核** 情况下，分析结果：
    - 如果四个任务是 <u>计算密集型</u>，没有多核来并行计算。
    方案一徒增了创建进程的开销。方案二胜。
    - 如果四个任务是 <u>I/O 密集型</u>，方案一创建进程的开销大，且进程的切换速度远不如线程，方案二胜。
<br>

- **多核** 情况下，分析结果：
    - 如果四个任务是 <u>计算密集型</u>，多核意味着并行计算，在 python 中一个进程中同一时刻只有一个线程执行，并不上多核。方案一胜 
    - 如果四个任务是 <u>I/O 密集型</u>，再多的核也解决不了 I/O 问题，方案二胜

结论：
现在的计算机基本上都是多核。
python 对于计算密集型的任务开多线程的效率并不能带来多大性能上的提升，甚至不如串行 ( 没有大量切换 )。
但是，对于 IO 密集型的任务效率还是有显著提升的。


# 5. 多线程性能测试

要用到的时候再去看[原文](https://www.cnblogs.com/wj-1314/p/9056555.html)


<br>


# 6. **死锁**：互相等待
所谓死锁：
指两个或者两个以上的进程或者线程在执行过程中，因 **争夺资源** 而造成的一种线程之间 **互相等待** 的现象。
若无外力作用，他们都将无法推进下去，此时称系统处于死锁状况或系统产生了死锁。
这些永远在互相等待的进程称为死锁进程。

```py
# 进程死锁
from threading import Thread, Lock
import time

lock_a = Lock()
lock_b = Lock()
 
class MyThread(Thread):
    def run(self):
        self.func1()
        self.func2()

    def func1(self):
        lock_a.acquire()
        print('\033[41m%s 拿到A锁\033[0m' % self.name)
 
        lock_b.acquire()
        print('\033[42m%s 拿到B锁\033[0m' % self.name)
        lock_b.release()
 
        lock_a.release()
 
    def func2(self):
        lock_b.acquire()
        print('\033[43m%s 拿到B锁\033[0m' % self.name)
        time.sleep(2)
 
        lock_a.acquire()
        print('\033[44m%s 拿到A锁\033[0m' % self.name)
        lock_a.release()
 
        lock_b.release()
 
if __name__ == '__main__':
    for i in range(10):
        t = MyThread()  # 10 个线程
        t.start()       # 每个线程执行 func1(), func2()
```


```py
# 执行效果
Thread-1 拿到A锁
Thread-1 拿到B锁
Thread-1 拿到B锁
Thread-2 拿到A锁
 
 
 
 
# 出现死锁，整个程序阻塞住
```

<br>

# 7. **递归锁**：解决死锁
死锁的解决方法是是使用递归锁。递归锁，即 可重入锁 RLock

在 python 中为了支持<u>在同一线程中多次请求同一资源，</u>
python 提供了 **可重入锁 RLock** 。

这个 RLock 内部维护着一个 **Lock** 和一个 **counter** 变量， 
counter 记录了 acquire 的次数，从而使得资源可以被多次 require 。
直到一个线程所有的 acquire 都被 release ，其他的线程才能获得资源。

上面的例子如果使用 RLock 代替 Lock ，则不会发生死锁。
二者的区别是：==**递归锁可以连续 acquire 多次，而互斥锁只能 acquire 一次。**==

一个线程拿到锁，counter 加 1, 该线程内又碰到加锁的情况，则 counter 继续加 1。 
<u>这期间所有 **其他线程** 都只能等待</u>，等待该线程释放所有锁，即 counter 递减到 0 为止。

```py
from threading import Thread, RLock
import time

lock_a = lock_b = RLock()

 
class MyThread(Thread):

    def run(self):
        self.func1()
        self.func2()

    def func1(self):
        lock_a.acquire()
        print('\033[41m%s 拿到A锁\033[0m' %self.name)
 
        lock_b.acquire()
        print('\033[42m%s 拿到B锁\033[0m' %self.name)
        lock_b.release()
 
        lock_a.release()
 
    def func2(self):
        lock_b.acquire()
        print('\033[43m%s 拿到B锁\033[0m' %self.name)
        time.sleep(2)
 
        lock_a.acquire()
        print('\033[44m%s 拿到A锁\033[0m' %self.name)
        lock_a.release()
 
        lock_b.release()
 

if __name__ == '__main__':
    for i in range(10):
        t=MyThread()
        t.start()
```


```py
# 结果：
Thread-1 拿到了A锁
Thread-1 拿到了B锁
Thread-1 拿到了B锁
Thread-1 拿到了A锁
Thread-2 拿到了A锁
Thread-2 拿到了B锁
Thread-2 拿到了B锁
Thread-2 拿到了A锁
Thread-4 拿到了A锁
Thread-4 拿到了B锁
Thread-4 拿到了B锁
Thread-4 拿到了A锁
Thread-6 拿到了A锁
Thread-6 拿到了B锁
Thread-6 拿到了B锁
Thread-6 拿到了A锁
Thread-8 拿到了A锁
Thread-8 拿到了B锁
Thread-8 拿到了B锁
Thread-8 拿到了A锁
Thread-10 拿到了A锁
Thread-10 拿到了B锁
Thread-10 拿到了B锁
Thread-10 拿到了A锁
Thread-5 拿到了A锁
Thread-5 拿到了B锁
Thread-5 拿到了B锁
Thread-5 拿到了A锁
Thread-9 拿到了A锁
Thread-9 拿到了B锁
Thread-9 拿到了B锁
Thread-9 拿到了A锁
Thread-7 拿到了A锁
Thread-7 拿到了B锁
Thread-7 拿到了B锁
Thread-7 拿到了A锁
Thread-3 拿到了A锁
Thread-3 拿到了B锁
Thread-3 拿到了B锁
Thread-3 拿到了A锁
```

<br>

# 8. 信号量
==信号量也是一把 **锁** 。==
可以指定信号量为 5 ，
对比互斥锁同一时间只能有一个任务抢到锁去执行，信号量同一时间可以有 5 个任务可以拿到锁去执行。

<u>与 **进程池** 是完全不同的概念。</u>
进程池`Pool(4)`，最大只能产生4个进程。而且从头到尾都只是这四个进程，不会产生新的。
而信号量是产生一堆线程/进程
<br>

**打比方：**

**互斥锁** 相当于 <u>合租房屋的人去抢一个厕所。</u>
**信号量** 相当于 <u>==一群路人争抢公共厕所，公共厕所有多个坑位==</u>。这意味着同一时间可以有多个人上公共厕所。但公共厕所容纳的人数是一定的，这便是信号量的大小。


```py
from threading import Thread, Semaphore
import threading
import time
 
def func():
    sm.acquire()
    print('%s get sm' %threading.current_thread().getName())
    time.sleep(3)
    sm.release()
 
if __name__ == '__main__':
    sm = Semaphore(5)           # sm: 信号量
    for i in range(23):
        t = Thread(target=func) # 23 个线程 每个线程认为为运行 func()
        t.start()
```
**解析：**
- Semaphore 管理一个内置的计数器，每当调用 `acquire()` 时内置计数器 -1 ； 
- 调用 `release()` 时内置计数器 +1 ； 
- 计数器不能小于 0 ；
- 当计数器为 0 时， acquire() 将阻塞线程直到其他线程调用 release() 。


<br>

# 9. **Event**：实时监测信号
同进程的一样，线程的一个关键特性是每个线程都是独立运行且状态不可预测。
如果程序中的其他线程需要<u>通过判断某个线程的状态来确定自己下一步的操作</u> , 这时线程同步问题就会变得非常棘手。

为了解决这些问题 , 我们需要使用 `threading` 库中的 `Event` 对象。 
对象包含一个可由线程设置的 **信号标志** , 它允许线程等待某些事件的发生。

在 初始情况下 , Event 对象中的信号标志被设置为假。
如果有线程等待一个 Event 对象 , 而这个 Event 对象的标志为假 , 那么这个线程将会被一直 ==**阻塞** 直至该标志为真==。
一个线程如果将一个 Event 对象的信号标志设置为真 , 它将唤醒所有等待这个 Event 对象的线程。
如果一个线程等待一个已经被设置为真的 Event 对象 , 那么它将忽略这个事件 , 继续执行。

```py
event.isSet() ：返回 event 的状态值； 
event.wait()  ：如果 event.isSet()==False 将阻塞线程； 
event.set()   ：设置 event 的状态值为 True ，所有阻塞池的线程激活进入就绪状态， 等待操作系统调度； 
event.clear() ：恢复 event 的状态值为 False 。
```


<br><br>
要用到的时候再去看[原文](https://www.cnblogs.com/wj-1314/p/9056555.html)

<br><br>

# 10. 条件Condition（了解）

要用到的时候再去看[原文](https://www.cnblogs.com/wj-1314/p/9056555.html)


<br><br>

# 11. 定时器

要用到的时候再去看[原文](https://www.cnblogs.com/wj-1314/p/9056555.html)

<u></u>

<br>
<br><br><br><br><br><br><br><br>

··



```py

```

```py

```

```py

```

```py

```

```py

```

```py

```