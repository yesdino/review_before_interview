# 目录

[toc]

---

[出处：python基于redis实现分布式锁](https://www.cnblogs.com/angelyan/p/11523846.html)

## 一、什么是分布式锁


### 需求背景

我们在开发应用的时候，如果需要对某一个 ==**共享变量**== 进行 **多线程同步访问** 的时候，可以使用我们学到的锁进行处理，并且可以完美的运行，毫无Bug！

注意这是单机应用，后来业务发展，需要做集群，
一个应用需要部署到几台机器上然后做负载均衡，大致如下图：
![img](https://img2018.cnblogs.com/blog/1449147/201909/1449147-20190915192400145-1228507196.png)

上图可以看到，变量A存在三个服务器内存中（这个变量A主要体现是在一个类中的一个成员变量，是一个有状态的对象），
如果不加任何控制的话，变量A同时都会在分配一块内存，
**<u>三个请求发过来同时对这个变量操作，显然结果是不对的！</u>**
即使不是同时发过来，三个请求分别操作三个不同内存区域的数据，
变量A之间不存在共享，也不具有可见性，处理的结果也是不对的！
<br>

如果我们业务中确实存在这个场景的话，我们就需要一种方法解决这个问题！

为了保证一个方法或属性在高并发情况下的同一时间只能被同一个线程执行，
在传统单体应用单机部署的情况下，可以使用并发处理相关的功能进行互斥控制。

但是，==随着业务发展的需要，原单体单机部署的系统被演化成 <u>**分布式集群系统**</u>==，
由于分布式系统多线程、多进程并且分布在不同机器上，
这将使原单机部署情况下的并发控制锁策略失效，单纯的应用并不能提供分布式锁的能力。
==为了解决这个问题就需要一种 **<u>跨机器的互斥机制来控制共享资源的访问</u>**，
这就是分布式锁要解决的问题！==

<br>

### 分布式锁应该具备的条件

- 1、在分布式系统环境下，<u>一个方法在同一时间只能被一个机器的一个线程执行</u>；
- 2、<u>高可用</u>的获取锁与释放锁；
- 3、<u>高性能</u>的获取锁与释放锁；
- 4、具备<u>可重入</u>特性；
- 5、具备<u>锁失效</u>机制，防止死锁；
- 6、具备<u>非阻塞锁</u>特性，即没有获取到锁将直接返回获取锁失败

<br>

---

## 二、基于redis实现分布式锁

### 1、选用Redis实现分布式锁原因

（1）Redis 有很高的性能；
（2）Redis 命令对此支持较好，实现起来比较方便
<br>

### 2、使用命令介绍

在使用Redis实现分布式锁的时候，主要就会使用到这三个命令。

**（1）SETNX**

`SETNX key val`：
当且仅当key不存在时，set一个key为val的字符串，返回1；
若key存在，则什么都不做，返回0。

**（2）expire**

`expire key timeout`：为key设置一个超时时间，单位为second，超过这个时间锁会自动释放，避免死锁。

**（3）delete**

`delete key`：删除key

<br>


### 3、实现思路

- **1、设置锁的时候**
    - 使用 `setnx` 加锁，
    - 并使用 `expire` 命令为锁添加一个超时时间，超过该时间则自动释放锁，
    - 锁的 value 值为一个随机生成的 UUID ，通过此在释放锁的时候进行判断。 
    <br>

- **2、获取锁的时候**
    - 设置一个获取的超时时间，若超过这个时间则放弃获取锁。 
    <br>

- **3、释放锁的时候**
    - 通过 UUID 判断是不是该锁，若是该锁，则执行 delete 进行锁释放。

<br>

### 4、分布式锁的简单实现

```python
import time
import uuid
from threading import Thread
import redis

# 连接redis
redis_client = redis.Redis(host="localhost", port=6379, password=123, db=10)

def acquire_lock(lock_name, acquire_time=10, time_out=10):
    """
    获取一个锁
    lock_name   ：锁定名称
    acquire_time: 客户端等待获取锁的时间
    time_out    : 锁的超时时间
    """
    identifier = str(uuid.uuid4())
    end = time.time() + acquire_time
    lock = "string:lock:" + lock_name
    while time.time() < end:
        if redis_client.setnx(lock, identifier):
            # 给锁设置超时时间, 防止进程崩溃导致其他进程无法获取锁
            redis_client.expire(lock, time_out)
            return identifier
        elif not redis_client.ttl(lock):
            redis_client.expire(lock, time_out)
        time.sleep(0.001)
    return False

def release_lock(lock_name, identifier):
    """
    释放一个锁
    通用的锁释放函数
    """
    lock = "string:lock:" + lock_name
    pip = redis_client.pipeline(True)
    while True:
        try:
            pip.watch(lock)
            lock_value = redis_client.get(lock)
            if not lock_value:
                return True

            if lock_value.decode() == identifier:
                pip.multi()
                pip.delete(lock)
                pip.execute()
                return True
            pip.unwatch()
            break
        except redis.excetions.WacthcError:
            pass
    return False
```

测试刚才实现的分布式锁
```python
count = 10

def seckill(i):
    identifier=acquire_lock('resource')
    print("线程:{}--获得了锁".format(i))
    time.sleep(1)
    global count        # 操作函数外的变量 count
    if count < 1:
        print("线程:{}--没抢到，票抢完了".format(i))
        return
    count -= 1
    print("线程:{}--抢到一张票，还剩{}张票".format(i,count))
    release_lock('resource',identifier)


for i in range(50):     # 50 个线程抢锁
    t = Thread(target=seckill, args=(i,))
    t.start()
```
