## 队列 queue

**==先进先出== 像排队的人一样**

![queue_shuang](https://github.com/yesdino/img_upload/blob/master/imooc_study/data_structure/queue_shuang.png?raw=true)


```py
# 借助 deque 实现【 队列 】 定义
from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def append(self, val):
        return self.items.append(val)
    
    def pop(self):
        return self.items.popleft()
    
    def empty(self):
        return len(self.items) == 0


#  测试用例
def test_queue():
    q = Queue()
    q.append(0)
    q.append(1)
    q.append(2)

    print(q.pop())
    print(q.pop())
    print(q.pop())

if __name__ == '__main__':
    test_queue()
```
