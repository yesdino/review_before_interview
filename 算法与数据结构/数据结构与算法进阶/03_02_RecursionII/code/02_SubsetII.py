'''
题目：
给你一个不含重复元素的集合 nums, 要求返回所有可能的子集。
nums 的集合中可能会包含重复的元素，返回的子集中去掉重复的元素
'''

# -------------------
# 迭代解法
def subsets2(nums):
    res = [[]]
    for num in nums: 
        res += [ i + [num] for i in res if i + [num] not in res]
    return res

# -------------------
# 递归解法
def subsets_recursive2(nums):
    sub_lis = []
    result = []
    nums.sort()                 # 1. 先排序
    subsets2_recursive_helper(result, sub_lis, nums, 0)
    return result

def subsets2_recursive_helper(result, sub_lis, nums, start_idx):
    result.append(sub_lis)
    for i in range(start_idx, len(nums)):
        if (i != start_idx and nums[i] == nums[i-1]):  # 2. 与前面一个数相同时，跳过不要
            continue
        next_sub_lis = sub_lis + [nums[i]]      # 3. 下一层的 sub_lis = 这一层的 sub_lis + 索引元素
        subsets2_recursive_helper(result, next_sub_lis, nums, i+1)

# -------
# 测试
nums = [1,2,2]
ret = subsets_recursive2(nums)
print(ret)
ret.sort()

correct_ret = [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
correct_ret.sort()
print(ret == correct_ret)