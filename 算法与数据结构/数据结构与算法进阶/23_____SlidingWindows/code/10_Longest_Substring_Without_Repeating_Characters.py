"""
从字符串中找到最长的子串，这个子串没有重复的字母，
要求你返回这个字符串的长度

:param string   : 给定的字符串
:return         : 符合条件的最长的子串
"""
def lengthOfLongestSubstring(string):
    i = 0   # 左指针 有效窗口的头指针
    j = 0   # 右指针 遍历字符的指针

    char_s = set()  # 检测重复
    max_len = 0
    n = len(string)
    while i < n and j < n:
        if string[j] in char_s:     # 遇到了重复的字符
            char_s.remove(string[i])
            i += 1
        else:                       # 没有重复
            char_s.add(string[j])
            j += 1
            # 更新最大子串长度
            cur_len = j - i
            max_len = max(max_len, cur_len)
    return max_len


assert(lengthOfLongestSubstring('abcabcbb') == 3)
assert(lengthOfLongestSubstring('bbbbb') == 1)
assert(lengthOfLongestSubstring('pwwkew') == 3)
assert(lengthOfLongestSubstring('wesdsfgh') == 5)



