'''
【 找到插入位置 】
(若找不到 target，返回 target 应该在有序数组中插入的位置索引)

题目：
提供一个有序数组 lis 和一个 target 目标值，需要找到并返回 target 在数组中的索引。
若找不到，返回 target 应该在有序数组中插入的位置索引
'''



def search_insert_position(lis, target):
    if len(lis) == 0:
        return 0

    left, right = 0, len(lis) - 1
    while left + 1 < right:
        mid = left + (right - left) // 2

        if lis[mid] == target:
            return mid
        
        if lis[mid] < target:
            left = mid
        else:
            right = mid
        
    if lis[left] >= target:
        return left
    if lis[right] >= target:
        return right
        
    return right + 1


num_list = [2,3,5,7,8,9]
# print(search_insert_position(num_list, 7))  # 3
# print(search_insert_position(num_list, 4))  # 2

search_insert_position(num_list, 4)


