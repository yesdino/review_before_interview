# 题：
# 给你一种 2*1 尺寸的瓷砖，要求你铺一块宽为 2，长为 n 的区域，求有几种铺法？

# 此题也没讲，需要自己写一下

def tails(n):
    dp = [1, 1]
    for i in range(2, n+1):
        dp.append(dp[i-1] + dp[i-2])
    return dp

# -----------------------------
# print(tails(6))