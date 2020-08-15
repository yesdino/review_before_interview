"""
求乘积小于 k 的子数组的个数

:param nums : 给定的数组
:param k    : 需要你去找的子串
:return     : 子串在字符串的位置索引
"""
def bruteforce(nums, k):
    count = 0
    for i in range(len(nums)):
        product = 1
        for j in range(i, len(nums)):
            product *= nums[j]
            if (product >= k):
                break
            count += 1
    return count

nums = [10, 5, 2, 6]
k = 100
ret = bruteforce(nums, k)
print(ret)