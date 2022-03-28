'''
【 二分搜索模板 】 

在有序列表 lis 中查找 target 目标值，并返回目标值的索引，若目标值不存在，返回 -1
'''

# 二分搜索模板，记住下面的几个重点
from operator import le
from turtle import right

def binarysearch(lis, target):
    if len(lis) == 0:               # 1. 注意边界值处理
        return -1

    left, right = 0, len(lis)-1     
    while left + 1 < right:
    # while left <= right:            # 2. 注意左索引和右索引不要越界
        mid = (left + right) // 2
        if lis[mid] < target:
            left = mid + 1
        elif lis[mid] > target:
            right = mid - 1
        else:
            return mid
    
    if lis[left] == target:         # 3. 有可能中间值落在了对半分位置的左边一点或者右边一点
        return left
    if lis[right] == target:
        return right

    return -1




num_list = [2,3,5,7,8,9]
print(binarysearch(num_list, 7))  # 3
print(binarysearch(num_list, 4))  # -1

