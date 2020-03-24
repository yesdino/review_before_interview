# 题：
# Given n, find the number of different ways to write n as the sum of 1, 3, 4.
# 给一个 n, 求 1,3,4 相加得到 n 的所有相加方式

# 公式： D(n) = D(n-1) + D(n-3) + D(n-4)

def coin(n):
    dp = [0] * (n + 1)
    dp[0] = dp[1] = dp[2] = 1
    dp[3] = 2
    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 3] + dp[i - 4]   # D(n) = D(n-1) + D(n-3) + D(n-4)
    return dp[n]


if __name__ == "__main__":
    print(coin(5))      # 6
    print(coin(10))     # 64