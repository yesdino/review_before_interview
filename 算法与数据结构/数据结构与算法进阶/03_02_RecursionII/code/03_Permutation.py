








# -----------------------------
# 1、递归解法
def permute(nums):
    result = []
    sub_lis = []
    permute_helper(result, sub_lis, nums)
    return result

def permute_helper(result, sub_lis, nums):
    if len(nums) == 0:
        result.append(sub_lis)
    for i in range(len(nums)):                  # 1. 索引 i = 上一层下来的 nums
        next_sub_lis = sub_lis + [nums[i]]      # 2. 下一层的 sub_lis = 加上索引元素
        next_nums = nums[0:i] + nums[i+1:]      # 3. 下一层的 nums 剔除索引元素
        permute_helper(result, next_sub_lis, next_nums)
    
nums = [1, 2, 3]
ret = permute(nums)
print(ret)
# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]


















