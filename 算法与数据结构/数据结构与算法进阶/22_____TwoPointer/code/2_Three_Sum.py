"""
题目：
在一个有 n 个整数的数组 S 中，要求找出三个数 (a,b,c) 相加等于 0 的组合，
并且结果中不能包含重复的组合。


"""


def three_sum(nums):                            # 注意点
    res = []
    nums.sort()                                 # 1. 数组先排序。时间复杂度 O(nlgn) 
    for i in range(len(nums) - 2):              # 2. i 少两位，因为还有左右两指针各占一个位置
        if i>=1 and nums[i-1] == nums[i]:       # 3: 注意这里一定要用 i-1, 跳过的是后面重复的那个数，如果 i+1 就直接把前面的跳过去了
            continue                            # 4. 注意排完序之后会出现重复元素，要跳过，指针要 + 1 
        
        left = i + 1
        right = len(nums) - 1                   # 5. 头指针从第二位开始，尾指针最后一位开始
        while left < right:
            cur_sum = nums[i] + nums[left] + nums[right]
            if cur_sum < 0:
                left +=1 
            elif cur_sum > 0:
                right -= 1
            else:                               # nums[i] + nums[left] + nums[right] == 0
                res.append((nums[i], nums[left], nums[right]))
                if left < right and nums[left] == nums[left+1]:  # 6. 排完序之后会出现重复元素，要跳过，指针要 + 1
                    left += 1
                if left < right and nums[right] == nums[right-1]:# 7. 注意 right 指针要 -1 向前移动
                    right -= 1
                left += 1
                right -= 1
    return res

# ------
nums = [-1,0,1,2,-1,-4]
print(three_sum(nums))
nums = []
print(three_sum(nums))
nums = [0]
print(three_sum(nums))
nums = [0,0,0]
print(three_sum(nums))
