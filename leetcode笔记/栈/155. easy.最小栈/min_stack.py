class MinStack(object):
    
    def __init__(self):
        self.stk = []
        self.minstk = []
        
    # 入栈
    def push(self, x):
        self.stk.append(x)
        # minstk的栈顶元素一定要为最小，所以要入栈的值要比minstk栈的栈顶元素小才入栈
        if len(self.minstk) == 0 or x <= self.minstk[-1]:
            self.minstk.append(x)
        
    # 出栈
    def pop(self):
        tmp = self.stk.pop()
        # 有可能之前入栈的元素中有比最小栈栈顶大的，只入了stk栈而没入minstk栈
        if tmp == self.minstk[-1]:
            self.minstk.pop()
        
    # 获取栈顶元素
    def top(self):
        return self.stk[-1]

    # 获取栈内最小元素
    def getMin(self):
        return self.minstk[-1]