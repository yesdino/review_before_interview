# 借助最小堆解决【 topk 】问题
import heapq

class TopK(object):
    """ 获取大量元素中的前 k 大个元素，固定内存
    思路：
    1. 建立一个最小堆，放入序列的前 K 个元素
    2. 迭代剩余元素：
        if 当前元素 < 最小堆堆顶元素:
            则 跳过元素 （不是前 k 大
        else :
            替换堆顶元素为当前元素，重新调整最小堆堆顶
    3. 迭代完之后得到的最小堆就是我们要的前 k 大个元素
    
    """
    def __init__(self, iterable, k):
        self.minheap = []
        self.capacity = k           # 最小堆容量
        self.iterable = iterable
    
    def push(self, cur_val):
        if len(self.minheap) < self.capacity:
            heapq.heappush(self.minheap, cur_val)   # 步骤 1
        else:
            min = self.minheap[0]   # 堆顶元素
            if cur_val < min:
                pass
            else:
                heapq.heapreplace(self.minheap, cur_val)
        
    def get_topk(self):
        for val in self.iterable:
            self.push(val)
        return self.minheap


def test_TopK():
    import random
    lis = list(range(50))
    random.shuffle(lis)
    t = TopK(lis, 10)
    print(t.get_topk())


if __name__ == '__main__':
    test_TopK()