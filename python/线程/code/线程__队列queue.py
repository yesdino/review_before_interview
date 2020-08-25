'''
同一个进程下 多个线程数据是共享的
为什么同一个进程下 还会去使用队列呢？
因为：
    队列 = 管道 + 锁
所以：
    用队列还是为了【保证数据的安全】
'''

import queue

# 我们现在使用的队列 都是只能在本地测试使用的

''' 
1.队列 先进先出 '''
q1 = queue.Queue(3)
q1.put(1)
q1.get()
# q1.get_nowait()
# q1.get(timeout=3)
q1.full()
q1.empty()


''' 
2.队列 后进先出 （stack 栈） '''
q2 = queue.LifoQueue(3)  # Last in first out
q2.put(1)
q2.put(2)
q2.put(3)
print(q2.get())  # 3


''' 
3.优先级队列  你可以给放入队列中的数据 设置进出的优先级
# put括号内放一个元组 第一个数字表示优先级
# 注意：数字越小 优先级越高！！！'''
q3 = queue.PriorityQueue(4)
q3.put((10, '111'))      # (优先级, '数据')
q3.put((101, '222'))     # (优先级, '数据')
q3.put((0, '333'))       # (优先级, '数据')
q3.put((1, '444'))       # (优先级, '数据')
print(q3.get())          # (0, '333')

