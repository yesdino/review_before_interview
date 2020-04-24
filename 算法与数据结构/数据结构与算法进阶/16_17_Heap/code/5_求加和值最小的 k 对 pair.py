'''
给出两个排好序的 list。
限制每对 pair 需要从 list1,list 分别取一个数，
求加和值最小的 k 对 pair

例如：
list1 = [1,7,11]  list2 = [2,4,6]  k=3 
return: [1,2] [1,4] [1,6]

list1 = [1,1,2]  list2 = [1,2,3]  k=2 
return: [1,1] [1,1]
'''

# 时间复杂度：k*lg(k)

import heapq

def kSmallestPairs(num1, num2, k):
    heap = []
    def push(idx1, idx2):
        if idx1 < len(num1) and idx2 < len(num2):
            item = (num1[idx1] + num2[idx2], idx1, idx2)    # 注意元祖item 以第一个元素比较大小(这里用加和值比较大小)
            heapq.heappush(heap, item)
    push(0, 0)
    pair = []
    while heap and len(pair) < k:
        _, i, j = heapq.heappop(heap)
        pair.append((num1[i], num2[j]))
        push(i, j+1)
        if j == 0:
            push(i+1, j)
    return pair


# -----------------------------------------
num1 = [1,7,11]
num2 = [2,4,6]
k = 20
ret = kSmallestPairs(num1, num2, k)
print(ret)