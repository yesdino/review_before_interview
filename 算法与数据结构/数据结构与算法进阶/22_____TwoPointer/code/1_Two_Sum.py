# 解法 1: 使用字典成对
def two_sum(nums, target):
    dic = {}
    for idx, num in enumerate(nums):
        if num in dic:                  # 2. 遇到了【与它成对的数 (key)】, 返回上一个索引与当前索引
            print(dic)
            return [dic[num], idx]
        else:
            dic[target - num] = idx     # 1. 遇到了一个数，把【与它成对的数】作为 key, 数的索引作为 val 存入字段


# 解法 2: 双指针
def two_sum2(nums, target):
    index = []
    sorted_nums = nums[:]; 
    sorted_nums.sort()        # 先排序，时间复杂度 O(nlgn)
    
    i = 0;                  # 头尾双指针
    j = len(sorted_nums) - 1
    while i < j:
        if sorted_nums[i] + sorted_nums[j] == target:
            for k in range(0, len(nums)):            # 要找到左右指针指向的值在 排序之前的 nums 中的位置
                if nums[k] == sorted_nums[i]:
                    index.append(k)                 
                    break
            for k in range(len(nums)-1, -1, -1):     # 从后边开始往前迭代
                if nums[k] == sorted_nums[j]:
                    index.append(k)
                    break
            index.sort()
            break
        elif sorted_nums[i] + sorted_nums[j] < target:
            i = i + 1                                   # 小了，移动头指针
        elif sorted_nums[i] + sorted_nums[j] > target:
            j = j - 1                                   # 大了，移动尾指针

    return (index[0]+1, index[1]+1)


nums = [2,4,5,6,7,3]
target = 11
print(twoSum(nums, target))