'''
题目：
给你一个不含重复元素的集合 nums，要求返回所有可能的子集。
'''

# -------------------
# 迭代解法
def subsets(nums):
    result = [[]]
    for item in nums:
        for sub_lis in result[:]:  # 1. 注意这里为什么要用切片 切片其实是复制了一个copy
            result.append(sub_lis+[item])   # 2. 注意每一轮的 item, result 都发生了改变
    return result

# -------------------
# 递归解法
def subsets_recursive(nums):
    lis = []
    result = []
    subset_recursive_helper(result, lis, nums, 0)
    return result

def subset_recursive_helper(result, lis, nums, start_idx):
    """
    result   : 结果集
    lis      : 所有可能出现的子集都暂存在 lis 中
    nums     : input 的源集
    start_idx: 控制遍历源集 nums 时的位置索引，避免访问已经访问过的元素
    """
    result.append(lis[:])           # 2. 每一层递归最重要的就是这一步：把新的子集 lis 加入结果集中
    for i in range(start_idx, len(nums)):    # start_idx ~ len(nums)-1 从 start_idx 已经访问过的元素不再重新访问
        sub_lis = lis + [nums[i]]   # 1. sub_lis 构成所有可能出现的子集，在下一层递归中加入到结果集中
        subset_recursive_helper(result, sub_lis, nums, i+1) # 3. 下一层递归所以从当前 i 的下一个索引开始，访问过的索引不再访问


# -------
# 测试
nums = [0, 1, 2]
ret = subsets_recursive(nums)
print(ret)
ret.sort()

correct_ret = [[], [0], [0, 1], [0, 1, 2], [0, 2], [1], [1, 2], [2]]
correct_ret.sort()
print(ret == correct_ret)