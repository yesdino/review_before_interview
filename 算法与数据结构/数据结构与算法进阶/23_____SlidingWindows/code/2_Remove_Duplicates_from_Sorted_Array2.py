'''



'''

def removeDuplicates2(nums):
    if not nums:
        return 0
    
    i = 0
    for j in range(len(nums)):
        if nums[i-2] != nums[j] or (i < 2):
            print("swap: i:{},j:{}, num[{}]<->num[{}]:{}<->{}".format(i,j,i,j,nums[i],nums[j]))
            nums[i] = nums[j]
            i += 1
    return i


nums = [1,1,2,2,2,2,3,3,3,3,4,4]
print(removeDuplicates2(nums))