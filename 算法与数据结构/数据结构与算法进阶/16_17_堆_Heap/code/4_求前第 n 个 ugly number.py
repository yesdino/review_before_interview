'''
题目：
给一个 n, 求前第 n 个 ugly number

思路：
要遍历 3 个动态列表合并的堆

'''

import heapq

# 正解
def nthUglyNumber(n):
    p1, p2, p3 = [2], [3], [5]
    ugly = 1        # 注意 1 也是 ugly number

    # 要遍历 3 个动态列表合并的堆
    for num in heapq.merge(p1, p2, p3):     # heapq.merge : 融合排序序列,将返回多个序列融合之后排好序的列表
        print("num: {}".format(num))
        if n == 1:
            return ugly     # ugly: 上一轮循环的 num
        if num > ugly:      # 注意有可能会出现重复的数字
            ugly = num
            p1.append(num * 2)
            p2.append(num * 3)
            p3.append(num * 5)
            n -= 1
'''
录音：
为什么要拆成 3 个列表？
是为了方便做融合，在下面的 nthUglyNumber2() 中试过了，如果只是单纯的都放在一个列表中，
既不方便做动态池的堆化，也不方便每次都最小的 pop 出来
'''
# 错误解，试验合成一个列表，不要用 3 个列表会怎么样
def nthUglyNumber2(n):
    ugly_lis = [2,3,5]
    ugly = 1
    for num in heapq.heapify(ugly_lis): # 这里，不方便做动态池的堆化，也不方便每次都最小的 pop 出来
        print("num: {}".format(num))
        if n == 1:
            return ugly
        if num > ugly:
            ugly = num
            ugly_lis.append(num * 2)
            ugly_lis.append(num * 3)
            ugly_lis.append(num * 5)
            n -= 1
# -------------------------------------------------------
n = 10
ret = nthUglyNumber(n)
ret2 = nthUglyNumber2(n)
print(ret)
print(ret2)