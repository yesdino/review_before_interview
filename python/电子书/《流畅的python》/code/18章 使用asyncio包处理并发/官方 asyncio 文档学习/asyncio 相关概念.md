

[出处](https://www.cnblogs.com/yy-cola/p/9532007.html)



- **event_loop 事件循环：**

  程序开启一个无限的循环，程序员会把一些函数注册到事件循环上。
  当满足事件发生的时候，调用相应的协程函数。

- **coroutine 协程**：

  协程对象，指一个使用 `async` 关键字定义的函数，它的调用不会立即执行函数，而是会返回一个协程对象。协程对象需要注册到事件循环，由事件循环调用。

- **task 任务**：

  一个协程对象就是一个原生可以挂起的函数，任务则是对协程进一步封装，其中包含任务的各种状态。

- **future**： 

  代表将来执行或没有执行的任务的结果。它和task上没有本质的区别

- **async/await 关键字**：

  python3.5 用于定义协程的关键字，`async` 定义一个协程，`await` 用于挂起阻塞的异步调用接口。





**② `ensure_future()`、`asyncio.BaseEventLoop.create_task`、`asyncio.Task`三者的区别和取舍：**

ensure_future 除了接受 coroutine 作为参数，还接受 future 作为参数。

看 ensure_future 的代码，会发现 ensure_future 内部在某些条件下会调用 create_task，综上所述：

- `encure_future`: 最高层的函数，推荐使用，除了接受coroutine 作为参数，还接受 future 作为参数，`返回一个task`
- `create_task`: 在确定参数是 coroutine 的情况下可以使用，因为它只接受协程程序。
- `Task`: 可能很多时候也可以工作，但真的没有使用的理由！

