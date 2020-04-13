'''
题：
一段包含着 A-Z 的短信用以下方式进行编码：
'A' -> 1 
'B' -> 2 
... 
'Z' -> 26 

要求：给定一段编码的短信，求编码的方式有几种：
Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
'''

# 解
def numDecodings(string):
    if string == '' or string[0] == '0':
        return 0
    dp = [1, 1]                             # 前面的不用算，从 2 才开始算
    for i in range(2, len(string)+1):       # i: 2, 3, 4, ..., len(string)
        # if it is 0, then dp[i]=0
        result = 0
        if 10 <= int(string[i-2: i]) <= 26: # 任何两个相邻数字的值在 [10,26] 范围内
            result = dp[i - 2]
        if string[i - 1] != '0':
            result += dp[i - 1]             # 任何一个数字的值不等于 0
        dp.append(result)
    return dp[len(string)]

# -----------------------------------
# if __name__ == "__main__":
#     ret = numDecodings("226")
#     print(ret)
            
