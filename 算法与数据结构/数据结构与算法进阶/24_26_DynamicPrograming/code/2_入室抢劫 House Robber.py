def rob(nums):
    n = len(nums)
    dp = [ [0] * 2 for _ in range(n + 1)]       # [[0, 0], [0, 0], [0, 0], ...]
    for i in range(1, n + 1):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1])  # 0：不抢 = 不抢上一个房子的情况 + 这个房子抢到的钱
        dp[i][1] = nums[i-1] + dp[i-1][0]       # 1：抢 = ( 不抢上一个房子 or 抢上一个房子的情况 ) 哪个大选哪个
    return max(dp[n][0], dp[n][1])


def rob2(nums):         # 改进
    yes, no = 0, 0
    for i in nums: 
        no, yes = max(no, yes), i + no
    return max(no, yes)


if __name__ == "__main__":
    nums = [2, 7, 9, 3, 1]
    print(rob(nums))
    # print(rob2(nums))
