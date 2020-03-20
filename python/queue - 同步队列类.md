参考 [官网](https://docs.python.org/3.6/library/queue.html)

# queue 模块
queue 模块实现多生产者，多消费者队列。
当必须在 **==多个线程之间安全地交换信息==** 时，它在线程编程中特别有用。

此模块中的Queue类实现了所有必需的锁定语义。<br>这取决于Python中线程支持的可用性;看到线程模块。

该模块实现了三种类型的队列，区别仅在于**检索条目的顺序**。
## 三种类型队列
### FIFO队列
先入先出。在 FIFO队列 中，添加的第一个任务是第一个检索的任务。
### LIFO队列
后入先出。在 LIFO队列 中，最近添加的 item 是第一个被`get()`检索的（像**堆栈**一样运行）。
### 优先级队列
使用 优先级队列，item 将保持排序（使用heapq模块），并首先被`get()`检索到的是最低值的 item。

<br>
在内部，模块使用锁来临时阻止竞争线程;<br>但是，它不是为处理线程内的重入而设计的。

queue 模块定义以下类和异常：
## class 类
### Queue
FIFO队列的构造函数。
```py
queue.Queue(maxsize=0)

# maxsize是一个整数，用于设置可以放入队列的项目数的上限。
# 达到此大小后，插入将阻止，直到消耗队列项。
# 如果maxsize小于或等于零，则队列大小为无限大。
```

### LifoQueue
LIFO队列的构造函数。
```py
queue.LifoQueue(maxsize=0)

# maxsize是一个整数，用于设置可以放入队列的项目数的上限。
# 达到此大小后，插入将阻止，直到消耗队列项。
# 如果maxsize小于或等于零，则队列大小为无限大。
```

### PriorityQueue
优先级队列的构造函数。
```py
queue.PriorityQueue(maxsize=0)

# maxsize是一个整数，用于设置可以放入队列的项目数的上限。
# 达到此大小后，插入将阻止，直到消耗队列项。
# 如果maxsize小于或等于零，则队列大小为无限大。
# 首先检索最低值的条目（最低值条目是由 sorted(list(entries))[0] )返回的条目。
# 条目的典型模式是以下形式的元组：(priority_number，data)。
```

## 异常
### Empty
在对空的 Queue对象调用非阻塞 `get()`（ 或 `get_nowait()` ）时引发异常。
```py
queue.Empty
```

### Full
在已满的 Queue对象调用非阻塞 `get()`（ 或 `get_nowait()` ）时引发异常。
```py
queue.Full
```

## 方法
queue 对象（Queue，LifoQueue 或 PriorityQueue）提供下面描述的公共方法。

|   |   |  |
|---|---|---|
Queue .**qsize** ()|   返回队列的大致大小。|注意，`size()>0` 不保证后续的 `get()` 不会阻塞，<br>`qsize()<maxsize` 也不保证`put()`不会阻塞。   
Queue .**empty** () |队列是否为空，是返回True否返回False。|如果empty()返回True，则不保证对put()的后续调用不会阻塞。<br>类似地，如果empty()返回False，则不保证对get()的后续调用不会阻塞
Queue .**full** ()  |队列是否已满
Queue .**put** (item, block=True, timeout=None) |  将 item 放入队列   | 如果可选的block为true且timeout为None（默认值），则在必要时阻塞，直到有空闲插槽可用。<br>如果timeout是一个正数，它会阻止最多超时秒，如果在该时间内没有可用的空闲槽，则会引发Full异常。<br>若 block 为 false，如果空闲插槽立即可用，则将项目放在队列上，否则引发完全异常（在这种情况下忽略超时）。
Queue .put_nowait (item)    |相当于 `put(item, False)`
Queue .**get** (block=True, timeout=None)   |从队列中删除并返回一个item|如果可选的block为true且timeout为None（默认值），则在必要时阻止，直到某个项可用为止。<br>如果timeout是一个正数，它会阻止最多超时秒，如果在该时间内没有可用的项，则会引发Empty异常。<br>若 block 为 false，如果一个项立即可用则返回一个项，否则引发Empty异常（在这种情况下忽略超时）。
Queue .get_nowait ()    |相当于`get(False)`
Queue .task_done () |   表示以前排队的任务已完成|由队列使用者线程使用。对于用于获取任务的每个get()，对task_done()的后续调用会告知队列该任务的处理已完成。   
Queue .**join** ()  |主线程等待子线程结束才结束