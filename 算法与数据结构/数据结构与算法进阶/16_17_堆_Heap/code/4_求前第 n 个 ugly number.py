'''
题目：
给一个 n, 求前第 n 个 ugly number

思路：
要遍历 3 个动态列表合并的堆

'''

import heapq

def nthUglyNumber(n):
    p1, p2, p3 = [2], [3], [5]
    ugly = 1        # 注意 1 也是 ugly number

    # 要遍历 3 个动态列表合并的堆
    for num in heapq.merge(p1, p2, p3):
        if n == 1:
            return ugly
        if num > ugly:      # 注意有可能会出现重复的数字
            ugly = num
            p1.append(num * 2)
            p2.append(num * 3)
            p3.append(num * 5)
            n -= 1

# -------------------------------------------------------
n = 10
ret = nthUglyNumber(n)
print(ret)