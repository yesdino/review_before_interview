'''
- 题：
给你一个数组，你需要在数组中找到一个子数组，使其乘积为最大

- 思路：

'''


# 解：
def maxProduct(nums):
    if len(nums) == 0:
        return 0
    maxinum = mininum = result = nums[0]    # init
    for i in range(1, len(nums)):           # i: 1, 2, 3, ..., len(nums)-1
        num1 = maxinum * nums[i]
        num2 = mininum * nums[i]
        maxinum, mininum = max(num1, num2, nums[i]), min(num1, num2, nums[i])
        result = max(result, maxinum)
    return result

# nums = [2,3,-2,4]
# ret = maxProduct(nums)
# print(ret)