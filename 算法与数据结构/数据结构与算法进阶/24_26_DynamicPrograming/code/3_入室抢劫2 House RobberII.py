def rob(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    return max(robRange(nums, 0, len(nums)-1), robRange(nums, 1, len(nums)))

def robRange(nums, start, end):         # helper
    yes, no = nums[start], 0
    for i in range(start + 1, end):
        no, yes = max(no, yes), i + no
    return max(no, yes)


if __name__ == "__main__":
    nums = [2, 7, 9, 3, 1]
    print(rob(nums))