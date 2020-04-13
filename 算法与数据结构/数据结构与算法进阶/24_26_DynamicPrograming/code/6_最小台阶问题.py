'''
题目：
有一个楼梯，需要你从最底下到最上面，你可以一次走一步或者一次走两步
限制：每一层楼梯都要交费，每层收费不同 (给一个数组 cost_lis 告诉每层收费)
求：如何走才话费最少？

思路：
这题原理与入室抢劫的原理是一样的，都是边走边算，
只不过公式不同

公式：
dp(i) = min( dp[i-2]+cost_lis[i-2], dp[i-1]+cost_lis[i-1] )
当第 i 层台阶的花费 = min( 跨了 1 个台阶上来的的花费, 垮了 2 个台阶上来的花费 ) 哪个花费小选哪个

其中：
跨了 1 台阶上来的的花费 = cost_lis[i-1] + dp[i-1] ：( 前面那个台阶的花费+到前面那个台阶之前的花费总和 )
垮了 2 个台阶上来的花费 = cost_lis[i-2] + dp[i-2] ：( 前面那个台阶的花费+到前面那个台阶之前的花费总和 )
'''

# 解
# 时间复杂度：O(n), 空间复杂度：O(n)
def minCostClimbingStairs(cost_lis):
    n = len(cost_lis) + 1
    dp = [0] * n            # dp 数组: 到达第 i 个台阶所需要的花费
    for i in range(2, n):   # i = 2,3,4,...,n-1
        dp[i] = min(dp[i-2] + cost_lis[i-2], dp[i-1] + cost_lis[i-1])   # dp[i] : 到达第 i 个台阶所需要的花费
    return dp[-1]


# 解 2
# 时间复杂度：O(n), 空间复杂度：O(1)
def minCostClimbingStairs2(cost_lis):
    dp0, dp1, dp2 = 0, 0, 0
    for i in range(2, len(cost_lis)+1):   # i = 2,3,4,...,n-1
        dp2 = min(dp0 + cost_lis[i-2], dp1 + cost_lis[i-1])
        dp0, dp1 = dp1, dp2     # 为下一轮更新前两级台阶的花费
    return dp2



# ------------------------------------------------------------
if __name__ == "__main__":
    cost_lis = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    ret = minCostClimbingStairs2(cost_lis)
    print(ret)