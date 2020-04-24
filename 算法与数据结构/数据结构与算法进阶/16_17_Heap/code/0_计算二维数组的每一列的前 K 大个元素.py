'''
计算二维数组的每一列的前 K 大个元素

'''


import numpy as np
import heapq

x = np.array(
    [
        [1, 2, 3, 4, 5, 6],
        [2, 3, 5, 7, 8, 1], 
        [7, 9, 6, 6, 3, 2], 
        [8, 9, 0, 1, 4, 7]
    ], 
    np.int32
)


cols = x.shape[1]           # x.shape 返回 (行数，列数)
for col_idx in range(cols):
    col = x[:, col_idx]     # col: 每一列
    h = []
    for e in col:
        heapq.heappush(h, e)
        if len(h) > 2:
            heapq.heappop(h)# 把小的 pop 出去
    print(h)
ret = np.sort(x, axis=0)[-2:]
print(ret)