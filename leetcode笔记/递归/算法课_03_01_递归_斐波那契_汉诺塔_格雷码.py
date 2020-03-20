"""
二分查找
"""
# 循环方式
def bi_search_iter(alist, item):
    left, right = 0, len(alist) - 1
    while left <= right:
        # mid = (left + right) // 2
        mid = left + (right - left) // 2 # 注意这种写法是为什么养成写其他语言时防止input过大造成溢出 （虽然python可以避免）
        if alist[mid] < item:
            left = mid + 1
        elif alist[mid] > item:
            right = mid - 1
        else: # alist[mid] = item
            return mid
    return -1


# 单元测试 测试用例
import unittest

class TestBinarySearch1(unittest.TestCase):
    
    def setUp(self):
        self._f = bi_search_iter
    
    def test_empty(self):      # 为空
        alist = []
        r = self._f(alist, 5)
        self.assertEqual(-1, r)

    def test_one(self):        # 只有一个元素时
        alist = [1]
        r = self._f(alist, 0)
        self.assertEqual(-1, r)

        r = self._f(alist, 1)
        self.assertEqual(0, r)

    def test_two(self):        # 只有两个元素时
        alist = [1, 10]

        r = self._f(alist, 0)
        self.assertEqual(-1, r)

        r = self._f(alist, 1)
        self.assertEqual(0, r)

        r = self._f(alist, 2)
        self.assertEqual(-1, r)

        r = self._f(alist, 10)
        self.assertEqual(1, r)

        r = self._f(alist, 11)
        self.assertEqual(-1, r)
        
    def test_multiple(self):      # 多个元素时
        alist = [1,2,3,4,5]
        r = self._f(alist, 5)
        self.assertEqual(4, r)

        r = self._f(alist, 4)
        self.assertEqual(3, r)

        r = self._f(alist, 2)
        self.assertEqual(1, r)

        r = self._f(alist, 1)
        self.assertEqual(0, r)

        r = self._f(alist, 6)
        self.assertEqual(-1, r)

        r = self._f(alist, 0)
        self.assertEqual(-1, r)
        
    def test_duplicate(self):      # 测试有重复元素时
        alist = [1,1,1,2,3,3,3,3,3,3,4,5,5,5]
        r = self._f(alist, 5)
        self.assertEqual(5, alist[r])

        r = self._f(alist, 4)
        self.assertEqual(4, alist[r])

        r = self._f(alist, 2)
        self.assertEqual(2, alist[r])

        r = self._f(alist, 3)
        self.assertEqual(3, alist[r])

        r = self._f(alist, 1)
        self.assertEqual(1, alist[r])

        r = self._f(alist, 6)
        self.assertEqual(-1, -1)
        
        r = self._f(alist, 0)
        self.assertEqual(-1, -1)
