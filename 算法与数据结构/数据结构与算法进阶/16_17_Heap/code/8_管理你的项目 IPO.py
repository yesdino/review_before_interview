'''
题：
你有很多个项目，每个项目的盈利为 Profits, 需要的启动资金为 Capital。
现在你有总资产 W, 允许你做 k 个项目，每做完一个项目都可以讲盈利添加到 W 中。
求做完 k 个项目之后的最大总盈利？
'''
# 解：
import heapq

# k: 可以做的项目数
# W: 动态总资产
# Profits: 每个项目的盈利
# Capital: 每个项目所需的启动资金
def findMaximizedCapital2(k, W, Profits, Capital):
    heap = []
    pairs = sorted(zip(Capital, Profits))[::-1]    # [(1, 3), (1, 2), (0, 1)] 按照每个项目的启动资金 Capital 从大到小排序
    print("pairs: ", pairs)
    for _ in range(k):
        while pairs and pairs[-1][0] <= W:          # 将所有启动资金小于 W 的项目的盈利 Profits 都 push 进 heap 中
            heapq.heappush(heap, -pairs.pop()[1])   # python 的 heap 是最小堆，可用负数实现最大堆
        if heap:
            W += (-heapq.heappop(heap))             # 由于 pop 出来的是负数，所以用减号
    return W

# ------------------------------------------------
k = 2
W = 0
Profits = [1,2,3]   # 盈利
Capital = [0,1,1]   # 启动资金
ret = findMaximizedCapital2(k, W, Profits, Capital)
print(ret)
