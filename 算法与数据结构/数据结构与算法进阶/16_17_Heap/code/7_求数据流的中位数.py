'''
求数据流的中位数
'''


from heapq import *

class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num):
        heappush(self.min_heap, -heappushpop(self.max_heap, num))   # 先去 max，然后去 min
        # 如果最大堆的个数比最小堆个数小，把最小堆堆顶放去最大堆
        print("\n{}\nAdd: {}\nmax_heap len: {}, min_heap len: {}\nmax_heap: {} | min_heap: {}".format('='*30 ,num, len(self.max_heap), len(self.min_heap), self.max_heap, self.min_heap))
        if len(self.max_heap) < len(self.min_heap):
            heappush(self.max_heap, -heappop(self.min_heap))        # 因为 python 中的 heap 是最小堆，所以用负号来实现最大堆
            print("---\nmax_heap len: {}, min_heap len: {}\nmax_heap: {} | min_heap: {}\n".format(len(self.max_heap), len(self.min_heap), self.max_heap, self.min_heap))

    def findMedian(self):
        if len(self.max_heap) > len(self.min_heap):
            return float(self.max_heap[0])                          # 可直接用索引 0 获取堆顶元素
        return (self.max_heap[0] - self.min_heap[0]) / 2.0

# ---------------------------------------------------
finder = MedianFinder()
finder.addNum(7)
finder.addNum(2)
finder.addNum(3)
finder.addNum(5)
finder.addNum(4)
finder.addNum(8)
finder.addNum(6)
ret = finder.findMedian()
print(ret)