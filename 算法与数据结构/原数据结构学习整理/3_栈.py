# 借助 deque 实现【 栈 】
from collections import deque

class Stack(object):
    def __init__(self):
        self.deque = deque()
    
    def push(self, value):
        self.deque.append(value)
    
    def pop(self):
        return self.deque.pop()


#  测试用例
def test_queue():
    s = Stack()
    s.push(0)
    s.push(1)
    s.push(2)

    print(s.pop())
    print(s.pop())
    print(s.pop())

if __name__ == '__main__':
    test_queue()