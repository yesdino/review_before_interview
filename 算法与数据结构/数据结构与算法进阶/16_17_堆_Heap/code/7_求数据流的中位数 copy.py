'''
求数据流的中位数
'''


from heapq import *

class MedianFinder:

    def __init__(self):
        self.heaps = [], []     # 一个最大堆，一个最小堆

    def addNum(self, num):
        min_heap, max_heap = self.heaps
        heappush(min_heap, -heappushpop(max_heap, num))
        print("\n{}\nAdd: {}\nmax_heap len: {}, min_heap len: {}\nmax_heap: {} | min_heap: {}".format('='*30 ,num, len(max_heap), len(min_heap), max_heap, min_heap))
        # 如果最大堆的个数比最小堆个数小，把最小堆堆顶放去最大堆
        if len(max_heap) < len(min_heap):
            heappush(max_heap, -heappop(min_heap))
            print("---\nmax_heap len: {}, min_heap len: {}\nmax_heap: {} | min_heap: {}\n".format(len(max_heap), len(min_heap), max_heap, min_heap))

    def findMedian(self):
        min_heap, max_heap = self.heaps
        if len(max_heap) > len(min_heap):
            return float(max_heap[0])
        if len(max_heap) == 0:
            return None
        return (heappop(max_heap) - heappop(min_heap)) / 2.0

# ---------------------------------------------------
finder = MedianFinder()
ret = finder.findMedian()
print(ret)
finder.addNum(2)
ret = finder.findMedian()
print(ret)
finder.addNum(3)
ret = finder.findMedian()
print(ret)