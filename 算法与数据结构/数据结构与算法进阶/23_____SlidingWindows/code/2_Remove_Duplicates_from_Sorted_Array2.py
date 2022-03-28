'''
题：
上一题的基础上，允许最后返回的数组中重复数最多出现两次

思路：

1. 双指针： 
    i: 前面的位置表示已经置换好了的子数组
    j: 指向的位置是预备比较的位子。

2. 最多出现两次，那就 i-2 往前两位的位置去跟 j 相比


# 答案
def removeDuplicates2(nums):
    if not nums:
        return 0
    
    i = 0
    for j in range(len(nums)):
        if nums[i-2] != nums[j] or (i < 2):
            nums[i] = nums[j]
            i += 1
    return i


nums = [1,1,2,2,2,2,3,3,3,3,4,4]
print(removeDuplicates2(nums))
'''

def removeDuplicates2(nums):                    # 注意点：
    if not nums:                                # 1. 边界值
        return 0
    
    i = 0
    for j in range(len(nums)):
        if nums[i-2] != nums[j] or (i < 2):     # 2. (i < 2): 此时 i, j 指向同一个位置，都需要往前走
            nums[i] = nums[j]
            i += 1
    return i


nums = [1,1,2,2,2,2,3,3,3,3,4,4]
print(removeDuplicates2(nums))

