'''
题：
给你一个有 n 个正整数的数组。一个 m
找到一个连续的子数组，使得连续子数组之和尽可能大，但不能大于 m
'''


from itertools import accumulate  # since Python 3.2:

# print(list(accumulate([1,2,3,4,5])))        # 查看 accumulate 用法



# TODO 理解题解

def max_subarray(numbers, ceiling):
    cum_sum = [0]
    cum_sum = cum_sum + numbers
    cum_sum = list(accumulate(cum_sum))

    left  = 0
    right = 1           # 双指针：从第 1 2 位开始
    maximum = 0
    while left < len(cum_sum):
        while right < len(cum_sum) and cum_sum[right] - cum_sum[left] <= ceiling:
            right += 1
        if cum_sum[right - 1] - cum_sum[left] > maximum: # since cum_sum[0] = 0, thus right always > 0.
            maximum = cum_sum[right - 1] - cum_sum[left]
            pos = (left, right - 2)
        left += 1
    return pos

# --------
a = [4, 7, 12, 1, 2, 3, 6]
m = 15
result = max_subarray(a, m)
result