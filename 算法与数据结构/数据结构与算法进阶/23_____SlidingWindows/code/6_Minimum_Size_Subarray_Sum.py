"""
给你一个正整数数组，一个整数 s,
要求找到能够大于 s 的 最小的连续的子数组 的长度。
没有就返回 0。

:param nums : 给定的数组
:return     : 大于 s 的 最小的连续的子数组 的长度
"""
import sys

def minsubarray(alist, target):
    if not len(alist):
        return 0

    i = j = 0
    sums = 0
    min_len = sys.maxsize
    
    while j < len(alist):
        sums += alist[j]
        j += 1                      # 扩展窗口
        while sums >= target:       # 找到有效窗口了
            cur_len = j - i
            min_len = min(min_len, cur_len) # 更新全局的最小长度
            sums -= alist[i]
            i += 1                  # 打破窗口

    if min_len == sys.maxsize:
        min_len = 0
    return min_len

alist = [2, 3, 1, 2, 8]
target = 7
ret = minsubarray(alist, target)
print(ret)