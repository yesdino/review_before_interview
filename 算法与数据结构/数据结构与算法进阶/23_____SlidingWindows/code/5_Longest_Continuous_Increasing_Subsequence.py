"""
给你一个没有排序的数组，
要求你在数组中找到最长的 连续的、递增的 子数组的长度。

:param nums : 给定的数组
:return     : 最长的 连续的、递增的 子数组的长度
"""
def findLengthOfLCIS(nums):
    count = 1
    max_count = 1
    for i in range(1, len(nums)):   # 从第 2 个开始比
        if nums[i] > nums[i-1]:
            count += 1
            max_count = max(count, max_count)
        else:
            count = 1
    return max_count

nums = [1, 3, 5, 4, 7]
ret = findLengthOfLCIS(nums)
print("ret: ", ret)

