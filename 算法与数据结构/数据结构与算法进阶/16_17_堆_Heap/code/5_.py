import heapq

# 时间复杂度： O(kLogk) 
def kSmallestPairs(nums1, nums2, k):
    queue = []
    def push(i, j):
        if i < len(nums1) and j < len(nums2):
            heapq.heappush(queue, [nums1[i]+nums2[j], i, j])    # 堆 queue 用第一个 item: nums1[i]+nums2[j] 加和值进行排序比较
    push(0, 0)
    pairs = []
    while queue and len(pairs) < k:
        _, i, j = heapq.heappop(queue)
        # print("i:{}, j:{}".format(i, j))
        pairs.append([nums1[i], nums2[j]])
        push(i, j + 1)
        if j == 0:
            push(i + 1, 0)
    return pairs

# -----------------------------------------
nums1 = [1,7,11]
nums2 = [2,4,6]
k = 20
ret = kSmallestPairs(nums1, nums2, k)
print(ret)