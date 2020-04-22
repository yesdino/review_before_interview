'''
求数据流的中位数
'''


from heapq import *

class MedianFinder:

    def __init__(self):
        self.heaps = [], []     # 一个最大堆，一个最小堆

    def addNum(self, num):
        small, large = self.heaps
        heappush(small, -heappushpop(large, num))
        if len(large) < len(small):
            heappush(large, -heappop(small))

    def findMedian(self):
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        return (large[0] - small[0]) / 2.0

# ---------------------------------------------------
finder = MedianFinder()
finder.addNum(2)
finder.addNum(3)
finder.addNum(4)
finder.findMedian()