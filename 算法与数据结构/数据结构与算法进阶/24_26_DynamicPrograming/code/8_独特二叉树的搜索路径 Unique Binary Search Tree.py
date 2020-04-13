'''
题：
给定 n，用 1, 2..., n 来表达 Binary Search Tree，求有几种表达方式？

# TODO 补全思路
'''

def numTrees(n):
    if n <= 2:
        return n
    sol = [0] * (n+1)       # dp 数组
    sol[0] = sol[1] = 1
    for i in range(2, n+1):
        for left in range(0, i):
            sol[i] += (sol[left] * sol[i-1-left])
    return sol[n]

# ----------------------------------------
# if __name__ == "__main__":
#     ret = [numTrees(i) for i in range(1, 6)]
#     print(ret)