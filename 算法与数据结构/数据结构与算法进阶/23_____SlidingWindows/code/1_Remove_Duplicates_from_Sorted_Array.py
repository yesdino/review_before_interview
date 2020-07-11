'''
题： 23-01 00:05:38~00:08:26

给定一个 排序 数组，删除重复出现的元素（只保留此元素的一个），
这样新的数组中每个元素只出现一次，并返回这个新数组的长度


'''

def removeDuplicates(lis):
    if not lis:
        return 0
    
    i = 0
    for j in range(1, len(lis)):
        if lis[j] != lis[i]:
            i += 1
            lis[i] = lis[j]
    return i+1