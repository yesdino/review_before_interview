import heapq

def findKthLargest(nums, k):
    heap = []
    for i in nums:
        heapq.heappush(heap, i,)
        if len(heap) > k:
            heapq.heappop(heap)
    return heapq.heappop(heap)

# --------------------------------
nums = [5,11,3,6,12,9,8,10,14,1,4,2,7,15]
k = 5
ret = findKthLargest(nums, k)
print(ret)
