



def removeElement(nums, val):
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i

nums = [3, 2, 2, 3]
val = 3
print(removeElement(nums, val))