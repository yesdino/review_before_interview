'''
【 简单的二分搜索 】 

在有序列表 lis 中查找 target 目标值，并返回目标值的索引，若目标值不存在，返回 -1
'''

def bi_search_iter(lis, target):
    left, right = 0, len(lis)-1     # 维护两个值：左索引、右索引
    while left <= right:
        mid = (left + right) // 2
        if lis[mid] < target:
            left = mid + 1
        elif lis[mid] > target:
            right = mid -1
        else:
            return mid
    return -1



num_list = [1,2,3,5,7,8,9]
print(bi_search_iter(num_list, 7))  # 4
print(bi_search_iter(num_list, 4))  # 7