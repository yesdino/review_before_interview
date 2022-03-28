'''
题： 23-01 00:05:38~00:08:26
给定一个 排序 数组，删除重复出现的元素（只保留此元素的一个），
这样新的数组中每个元素只出现一次，并返回这个新数组的长度

注意点：
双指针：
    i: 前面的位置表示已经置换好了的子数组
    j: 指向的位置是预备比较的位子。

标签：
滑动窗口 双指针
'''

'''
def removeDuplicates(lis):          # 注意点
    if not lis:                     # 1. 边界
        return 0
    
    i = 0
    for j in range(1, len(lis)):    # 2. j 从第二位开始，因为第一位 i 会指向它
        if lis[j] != lis[i]:
            i += 1
            lis[i] = lis[j]
    return i+1
'''


def remove_duplicates(lis):
    if not len(lis):
        return 0
    
    i = 0           
    for j in range(1, len(lis)):
        if lis[j] != lis[i]:    
            i += 1
            lis[i] = lis[j]
    return i+1

lis = [1,1,2]
ret = remove_duplicates(lis)
print(ret)