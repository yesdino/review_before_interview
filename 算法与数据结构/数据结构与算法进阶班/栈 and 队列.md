[toc]

---



# **栈 stack**

## 自己构造栈 stack

抓住一个重点：
++入栈和出栈都在==栈顶==++，找一个端口作为栈顶，所有操作都在那个端口就可以了

基本都要实现的成员函数：
- `top()` 获取栈顶
- `push()` 入栈
- `pop()` 出栈

### 使用数组(列表)构造

```python
# 利用数组 Array 构造 栈 stack
class ArrayStack(object):
    def __init__(self):
        self._data = []         # 在 python 中用 list 作为动态 array
    
    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0

    def top(self):
        """ 返回栈顶元素 """
        if self.is_empty():
            raise ValueError('stack is empty')
        return self._data[-1]   # 这里以最后一个元素作为栈顶
    
    def push(self, val):
        """ 添加元素 O(1) """
        self._data.append(val)  # 以最后一个元素作为栈顶，在栈顶添加元素

    def pop(self):
        """ 删除元素 O(1) """
        if self.is_empty():
            raise ValueError('stack is empty')
        return self._data.pop()

    def print_stack(self):
        """ 打印整个栈 """
        for i in range(len(self._data)):
            print(self._data[i], end='')
```


### 使用链表构造栈 


```python
from Linkedlist import LinkedList   # 前面自定义的链表结构
from Linkedlist import Node

class LinkedStack(object):
    def __init__(self):
        self._linkedlist = LinkedList()
    
    def __len__(self):
        return self._linkedlist.length
    
    def is_empty(self):
        return self._linkedlist.length == 0

    def top(self):
        """ 获取栈顶元素 O(1) """
        return self._linkedlist.get_first.value

    def push(self, val):
        """ 向栈内添加元素 O(1) """
        self._linkedlist.add_first(val)     # 以头结点作为栈顶

    def pop(self):
        """ 出栈 O(1) """
        return self._linkedlist.remove_first().value
    
    def printstack(self):
        """ 打印栈内元素 """
        self._linkedlist.printlist()
```





---


# **队列 queue**

## 自己构造队列 queue

### 使用数组(列表)构造 


```python
# 注意用到的表示 size 的几个变量
# - DEFAULT_CAPACITY    : 初始队列总容量, 这个变量只在初始化的时候有用，后面都用 len(self._arr) 看实际容量(因为可能会被扩容)
# - len(self._arr)      : 实际队列总容量，由于有可能被扩容过，所以要看当前能够容纳的总容量用这个变量
# - self._size          : 队列中已经被放入元素的容量
class ArrayQueue(object):
    DEFAULT_CAPACITY = 4    # 初始队列容量（设置小一点看resize）
    def __init__(self):
        self._arr = [None] * ArrayQueue.DEFAULT_CAPACITY  # 长度为 DEFAULT_CAPACITY 的一维列表
        self._size = 0
        self._front = 0     # maintain 一个出队列的端口位置（这个位置指向队列中最前面（最先进去）的元素

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def resize(self, capacity):
        """ 内部数组扩容 并 重新整理数组中的元素的顺序（可能会有转向的元素）"""
        old_arr = self._arr
        self._arr = [None] * capacity   # 新的容量的数组
        walk = self._front
        for k in range(self._size):     # 重新整理数组  
            # 为什么不 k 直接遍历 old_arr? 因为可能会有转向的元素 需要用转向换算得到的 walk
            self._arr[k] = old_arr[walk]
            walk = (walk + 1) % len(old_arr)
        self._front = 0
    
    def first(self):
        """ 返回队列中最先进去的元素 O(1) """
        if self.is_empty():
            raise ValueError('Queue is empty')
        return self._arr[self._front]
    
    def dequeue(self):
        """ 出队列 O(1) """
        if self.is_empty():
            raise ValueError('Queue is')
        fir_item = self._arr[self._front]       # 出队列是在最前面的位置
        self._arr[self._front] = None
        # 元素出数组之后后面的元素不顺序推移上来，而是只推移[头指向]的位置，所以时间复杂度是 O(1), 不是 O(n)
        pop = (self._front + 1) % len(self._arr)# 【转向换算】得到出队列后最新的最前面的元素的位置
        self._front = pop
        self._size -= 1
        return fir_item
    
    def enqueue(self, val):
        """ 出队列 O(1) """
        if self._size == len(self._arr):    # 此时队列已经满了 需要扩容
            self.resize(2 * len(self._arr))
        pos = (self._front + self._size) % len(self._arr)# 【转向换算】得到入队列的位置（即最后面的元素的位置）
        self._arr[pos] = val
        self._size += 1
    
    def printqueue(self):
        """ 打印队列内元素 """
        for i in range(self._size):
            pos = ((self._front + self._size) -1 - i) % len(self._arr)  # 遍历元素的索引 换算
            print(self._arr[pos], end=" ")
        print()
```

### 使用链表构造数组 



```python
from LinkedList import LinkedList
from LinkedList import Node

class LinkedQueue(object):  # 用链表构造队列
    def __init__(self):
        self.count = 0
        self.head = None    # maintain 队列头指向,【 出队列 】注意这里 self.head 不是哨兵结点 是队列头指向
        self.tail = None    # maintain 队列尾指向,【 进队列 】
    
    def is_empty(self):
        # return self.count == 0
        if self.head is None and self.tail is None:
            return True
        else:
            return False

    def enqueue(self, val):
        """ 进队列 O(1) """
        new_node = Node(value=val)
        # 更新指向，如果已经有元素更新尾指向，如果还没有元素更新头指向
        if self.tail is not None:   
            self.tail.next = new_node   
        else:
            self.head = new_node
        self.tail = new_node        # 更新 tail 指向，指向队列尾
        self.count += 1
    
    def dequeue(self):
        """ 出队列 O(1) """
        if self.is_empty():
            raise ValueError('Queue is empty')
        del_node = self.head        # 把要出队列的 node 暂存起来
        self.head = self.head.next  # 更新 head 指向
        self.count -= 1
        return del_node

    def peek(self):
        """ 瞧一眼队列头(最先出队列的元素) O(1) """
        return self.head.value
    
    def print(self):
        """ 打印队列 """
        cur_node = self.head    # 注意这里 self.head 不是哨兵结点 是队列头指向
        while cur_node:
            print(cur_node.value, end=" ")
            cur_node = cur_node.next
        print(" ")
    
    def __len__(self):
        return self.count
```

# -------------------------

# 练习

## 利用 stack 构造 queue **TODO**







<br><br><br><br><br>


## 利用 queue 构造 stack 


```python
from LinkedList import LinkedList


class StackWithQueue:   # 使用 queue 实现 stack

    def __init__(self):
        self.queue = LinkedList()   # 使用队列
    
    def push(self, val):
        self.queue.add_last(val)    # 队列最后面作为栈顶
    
    def pop(self):
        size = self.queue.size()
        for _ in range(1, size):    
            rem_val = self.queue.remove_first()
            self.queue.add_last(rem_val)
        self.queue.remove_first()
    
    def top(self):
        size = self.queue.size()
        for _ in range(1, size):
            rem_val = self.queue.remove_first()
            self.queue.add_last(rem_val)
        top_val = self.queue.remove_first()
        self.queue.add_last(top_val)    # 注意：为了看栈顶把越来的结构打乱了要恢复回去
        return top_val
```





<br><br><br><br><br>

## 写一个最小值栈 min_stack **（类继承）** 

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

getMin() -- Retrieve the minimum element in the stack.

构造一个 stack, 操作 `push, pop, top` 函数的同时能检索到当前 stack 中所有元素的最小值

<br>

**方法 ①**

使用 **pair 数据对** 的方式存储元素

此方法使用类继承，

注意子类调用父类的方法：**`super(子类名, self)`** ==！！！==
```
import sys
from ArrayStack import ArrayStack

class MinStack(ArrayStack):     # 继承自 ArrayStack

    def __init__(self):
        super(MinStack, self).__init__()    # 调用父类: super(自类名, self)

    def push(self, val):
        """ 重新定义父类 push 方法, push 新的数据类型 NodeWithMin """
        pre_min = self.min()
        new_min = min(val, pre_min)
        new_node = NodeWithMin(val, new_min)
        super(MinStack, self).push(new_node)
    
    # pop() 不要重新定义 因为 本质是一个列表[], 使用的是 [].pop() 所有可以直接沿用父类方法

    def min(self):
        """ 获取 min stack 的最小值 """
        if super(MinStack, self).is_empty():    # 当前栈为空
            return sys.maxsize                  # 随意给一个系统最大值作为 min
        else:
            node = super(MinStack, self).top()
            return node._min
        

class NodeWithMin:  # 新的数据结构：带有最小值，作为最小栈的元素
    def __init__(self, value, min):
        self._value = value
        self._min = min
```

**方法 ②**

另外 maintain 一个**最小值栈** （此方法更好）

此方法使用类继承，

注意子类调用父类的方法：**`super(子类名, self)`** ==！！！==
```python
import sys
from ArrayStack import ArrayStack


class MinStack2(ArrayStack):

    def __init__(self):
        super(MinStack2, self).__init__()
        self.min_stack = ArrayStack()    # 不改变原来的 stack 内部数据结构，另外maintain一个最小栈
    
    def push(self, val):
        """ 重新定义子类 push: push 的同时在最小栈中 maintain 当前最小值 """ 
        if val <= self.min():
            self.min_stack.push(val)
        super(MinStack2, self).push(val)
        return val
    
    def pop(self):
        """ 重新定义子类 pop: pop 的同时在最小栈中 maintain 当前最小值 """ 
        pop_val = super(MinStack2, self).pop()
        if pop_val == self.min():
            self.min_stack.pop()
        return pop_val
        
    def min(self):
        """ 获取当前最小值 """ 
        if self.min_stack.is_empty():
            return sys.maxsize
        else:
            return self.min_stack.top()
```


## 一个 array 实现 2 个 stack **TODO**


```python
class twoStacks:

    def __init__(self, n):
        self.size = n
        self.arr = [None] * n   # 内部数据结构为数组
        # maintain 两个栈顶，一个头一个尾
        self.top1 = -1          # 进+1 第一个元素的索引为 0 
        self.top2 = self.size   # 进-1 第一个元素的索引为 size-1
    
    def push1(self, val):
        """ stack1 进栈 """
        if self.is_full():
            print('Stack Overflow')
        else:
            self.top1 += 1              # stack1 的栈顶 top1 从上往下移
            self.arr[self.top1] = val
    
    def pop1(self):
        """ stack1 出栈 """
        if self.top1 == -1:
            print("Stack1 Unferflow")
        else:
            pop_val = self.arr[self.top1]
            self.top1 -= 1
            return pop_val
    
    def push2(self, val):
        """ stack2 进栈 """
        if self.is_full():
            print('Stack Overflow')
        else:
            self.top2 -= 1
            self.arr[self.top2] = val
    
    def pop2(self):
        """ stack2 出栈 """
        if self.top2 == self.size:
            print("Stack2 Unferflow")
        else:
            pop_val = self.arr[self.top2]
            self.top2 += 1
            return pop_val

    def is_full(self):
        if self.top2 -1 <= self.top1:    # top2 top1 撞一起了 没位置了
            return True
        else:
            return False
```



## 一个 array 实现 3 个 stack **TODO**


```python

```


## Stack 中的元素排序 **TODO**


```python

```


## 翻转 string **TODO**


```python

```


## 判断回文字符串 Palindrome **TODO**


```python

```
