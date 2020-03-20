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