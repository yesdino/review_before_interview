
"""
每 k 个元素求一个平均值

:param nums : 给定的数组
:param k    : 给定的滑动窗口大小 k
:return     : 每k个元素求一个平均值，得到的列表
"""
def findMaxnumsverage(nums, k):
    moving_sum = 0.0
    # 1. 第一个 [1~k] 区间的值的总和
    for i in range(k):
        moving_sum += nums[i]
    
    # 2. 接下来，每向前移动一个值，就加上 nums[i]，减掉 nums[i-k]
    res = moving_sum
    for i in range(k, len(nums)):
        moving_sum += nums[i] - nums[i-k]
        res = max(res, moving_sum)  # 挑大的那个？？
    return (res / k)


nums = [1, 12, -5, -6, 50, 3]
ret = findMaxnumsverage(nums, 4)
print('ret:', ret)


    

