"""
实现 python 中的 strStr()
找到子串所在的开头索引

:param string   : 给定的字符串
:param substr   : 需要你去找的子串
:return         : 子串在字符串的位置索引
"""
def strStr(string, substr):
    if len(string) < len(substr):
        return None
    
    len1 = len(string)
    len2 = len(substr)
    # i: 子串的头指针
    # j: 当匹配到前面的字符之后子串的头指针偏移数
    for i in range((len1 - len2) + 1):  # i 只需要走 len1,len2 的距离差再加 1
        j = 0                           # j 实际上是偏移数
        while j < len2 and substr[j] == string[i+j]:
            j += 1
        if j == len2:
            return i
    return -1



string = '123lkoiu12'
substr = 'iuw1111111111'
ret = strStr(string, substr)
print(ret)






    

