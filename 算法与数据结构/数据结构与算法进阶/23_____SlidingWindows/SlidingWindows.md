# 目录

[toc]

------------------------------------------------------

# 滑动窗口 练习


## 1. 删除重复元素 | Remove Duplicates from Sorted Array
**题：** <sup style="color:#ccc">23-01 00:05:38~00:08:26</sup>

给定一个 **==排序==** 数组，<u>删除重复出现的元素</u>（只保留此元素的一个），
这样新的数组中每个元素只出现一次，并<u>返回这个新数组的长度</u>





**思路：** <sup style="color:#ccc">23-01 00:08:28~00:14:58</sup>

==这题实际上是双指针==

<img style="width:400px" src="../img/SlidingWindow/Remove_Duplicates_from_Sorted_Array_.png"></img>
自己画过程中的变化，这题很简单，
到最后 i 指针前面的都是不重复的，所以可以直接返回 i+1 为数组长度

**code：** <sup style="color:#ccc">23-02 00:00:08~00:01:34 Ex.1</sup>
[link](http://localhost:8888/notebooks/MyJupyterNote/old/23_____SlideWindows/22_01_.ipynb)
```python
def removeDuplicates(lis):
    if not lis:
        return 0
    
    i = 0
    for j in range(1, len(lis)):    # 时间复杂度 O(n), 只需要循环一遍就可以
        if lis[j] != lis[i]:        # 跟上一个元素比较
            i += 1
            lis[i] = lis[j]
    return i+1
```


------------------------------------------------------


## 2. 删除重复元素 2
**题：** <sup style="color:#ccc">23-02 00:02:07~00:03:01</sup>
上一题的基础上，允许最后返回的数组中重复数最多出现两次



**思路：** <sup style="color:#ccc">23-02 00:03:01~00:06:15</sup>
==**记住： 
`j`指向的位置是下一个要置换正确数的位置。
`i`前面的位置表示已经置换好了的子数组**==
<img src="../img/SlidingWindow/2_Remove_Duplicates_from_Sorted_ArrayII/00.gif"></img>

（如果动图思路跟不上可以自己去文件夹里面一张一张翻源图片）

**code：** <sup style="color:#ccc">23-02 00:06:15~00:07:16 Ex.2</sup>
[link](http://localhost:8888/notebooks/MyJupyterNote/old/23_____SlideWindows/22_01_.ipynb)

```python
def removeDuplicates2(nums):
    if not nums:
        return 0
    
    i = 0
    for j in range(len(nums)):
        if nums[i-2] != nums[j] or (i < 2):
            nums[i] = nums[j]
            i += 1
    return i
```


------------------------------------------------------


## 3. 删除元素 Remove Element
**题：** <sup style="color:#ccc">23-03 00:00:09~00:00:53</sup>

给定一个数组 **`nums`** 和一个值 **`val`**，
就地(**==in-place==**)删除这个 val 的所有实例，并返回新的数组的长度。
(注意没讲数组有没有排序)


**思路：** <sup style="color:#ccc">23-03 00:00:57~00:02:33</sup>

这个思路跟前面两题也是一样的，
==i 是下一个要置换的正确的数的位置==，
==i 前面的都是已经置换好的正确的子数组==。
那么你<u>只需要把不等于 val 的数都置换到 i 前面的子数组去就可以了</u>

**code：** <sup style="color:#ccc">23-03 00:02:35~ Ex.</sup>
[link]()

```python
def removeElement(nums, val):
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i
```


------------------------------------------------------


## 4. 每k个元素求一个平均值, 求最大的均值 | Maximum Average Subarray
**题：** <sup style="color:#ccc">23-04 00:00:08~00:06:27</sup>

给一个数组 nums, 一个窗口大小 k。
<u>要求你在 num 中每 k 个元素求一个平均值。</u>


（这题在银行中是比较常见的，他们需要知道到了月底手上还有多少现金流，根据手上的钱来做下一步决策。k 就相当于时间，多少个月。）

**思路：** <sup style="color:#ccc">23-04 00:09:12~00::</sup>

1. 第一个 [1~k] 区间的值的总和 
2. 接下来，每向前移动一个值，就加上 `nums[i]`，减掉 `nums[i-k]`

<img src="../img/SlidingWindow/4_Maximum_Average_Subarray.png" width=400></img>
[](../img/SlidingWindow/4_Maximum_Average_Subarray.png)


**code：** <sup style="color:#ccc"> Ex.</sup>
[link]()
```python
def findMaxnumsverage(nums, k):
    moving_sum = 0.0
    # 1. 第一个 [1~k] 区间的值的总和
    for i in range(k):
        moving_sum += nums[i]
    
    # 2. 接下来，每向前移动一个值，就加上 nums[i]，减掉 nums[i-k]
    res = moving_sum
    for i in range(k, len(nums)):
        moving_sum = moving_sum + nums[i] - nums[i-k]
        res = max(res, moving_sum)  # 挑大的那个？？
    return (res / k)


nums = [1, 12, -5, -6, 50, 3]
ret = findMaxnumsverage(nums, 4)
```


------------------------------------------------------


## 5. 最长的连续的、递增的子数组的长度 | Longest Continuous Increasing Subsequence
**题：** <sup style="color:#ccc"></sup>
给你一个没有排序的数组，
要求你在数组中找到最长的 **连续的**、**递增的** 子数组的<u>==**长度**==</u>。


**思路：** <sup style="color:#ccc">23-05 00:00:03~00::</sup>
1. maintain 一个 **`left`**，一个 **`right`**。
   **`left`**(`min`)到 **`right`**(`max`) 必须是递增的
2. ==下一个数一定要比 **`right`** 大才能继续构成连续==
   否则重新算，既这个数为新的 **`left`**

**code：** <sup style="color:#ccc"> Ex.</sup>
[link]()
```python
def findLengthOfLCIS(nums):
    count = 1       # 局部长度
    max_count = 1   # 全局最大长度
    for i in range(1, len(nums)):   # 从第 2 个开始比
        if nums[i] > nums[i-1]:
            count += 1
            max_count = max(count, max_count)
        else:
            count = 1
    return max_count

nums = [1, 3, 5, 4, 7]
ret = findLengthOfLCIS(nums)
```


------------------------------------------------------

## 6. 最短的连续子数组 | Minimum Size Subarray Sum（模板）
<!-- 6_Minimum_Size_Subarray_Sum -->

**题：** <sup style="color:#ccc"></sup>

给你一个正整数数组，一个整数 target,
要求找到一个 **长度最小的连续的子数组**，使得这个子数组的和大于 target
没有就返回 0。

Example：
Given the array `[2, 3, 1, 2, 4, 3]` and `s = 7`
the subarray `[4, 3]` has the minimal length under the problem constraint



**思路：** <sup style="color:#ccc">23-06 00:01:35</sup>

<br>

可能会问的点：<sup style="color:#ccc">23-06 00:05:41</sup>
1. 如何定义窗口。（什么是好窗口，坏窗口，什么时候打破窗口，恢复窗口
2. 什么时候移动左指针，什么时候移动右指针

**模板**：<sup style="color:#ccc">23-06 00:07:25</sup>
```py
# 两个 while 循环，
while j < len(nums):
    j += 1          # valid windows
    while ...:      # condition
        i += 1      # break windows

    ...
```
**时间复杂度：**<sup style="color:#ccc">23-06 00:08:56</sup>
注意，不是 `O(n^2)`, `i`, `j` 都各自只走了一遍数组长度，是 `O(n)`

**code：** <sup style="color:#ccc">23-06 00:09:36 Ex.</sup>
[link]()
```python
import sys

def minsubarray(lis, target):
    if not len(lis):
        return 0

    i = j = 0
    sums = 0
    min_len = sys.maxsize
    
    while j < len(lis):
        sums += lis[j]
        j += 1                      # 扩展窗口
        while sums >= target:       # 找到有效窗口了
            cur_len = j - i
            min_len = min(min_len, cur_len) # 更新全局的最小长度
            sums -= lis[i]
            i += 1                  # 打破窗口

    if min_len == sys.maxsize:
        min_len = 0
    return min_len

lis = [2, 3, 1, 2, 8]
target = 7
ret = minsubarray(lis, target)
```


------------------------------------------------------


## 7. 实现 strStr() 函数 | Implement strStr()

<!-- 7_Implement_strStr -->

`Return the index of the first occurrence of needle in haystack,`
`or -1 if needle is not part of the haystack`

找到子串所在的索引

**题：** <sup style="color:#ccc"></sup>





**思路：** <sup style="color:#ccc">23-07 00:08:40~</sup>


**code：** <sup style="color:#ccc">23-07 00:11:03~ Ex.</sup>
[link]()
```python
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
```
**时间复杂度：**<sup style="color:#ccc">23-07 00:13:08</sup>
这种算法如果遇到极端情况的话，时间复杂度会较高，`O(n*m)`。不过在大多数情况下，这种算法的效率还是比较高的


（还有一种解法没讲）




------------------------------------------------------


## 8. 子数组乘积小于 K | Subarray Product Less Than K
<!-- 8_Subarray_Product_Less_Than_K -->
**题：** <sup style="color:#ccc">23-08 00:00:11~</sup>

给你一个正整数数组 `nums`, 
要求你找到所有连续子数组，使得数组所有子元素的乘积小于 k
要求你返回符合条件的子数组的个数



**思路：** <sup style="color:#ccc">23-08 00:03:36~</sup>
小于 k 时，就是 valid windows，此时 `j++`
大于 k 时，就是 invalid windows，此时 `i++`


**code：** <sup style="color:#ccc">23-08 00:11:00~ Ex.8</sup>
[link]()
```python
# 暴力解 O(n)（虽然是暴力解但是还是很快的）
def bruteforce(nums, k):
    count = 0
    for i in range(len(nums)):
        product = 1
        for j in range(i, len(nums)):   # 从 i 开始，前面遍历过的 i 不再继续遍历
            product *= nums[j]
            if (product >= k):
                break
            else:
                count += 1 
    return count

# --------------------------
nums1 = [10, 5, 2, 6]
k = 100
print(bruteforce(nums1, k))
nums2 = [1, 5, 4, 3, 2, 7]
print(bruteforce(num, k))
```

------------------------------------------------------

# 练习 2

<!-- 10_Longest_Substring_Without_Repeating_Characters -->

## 1. 最小窗口子串 | Longest Substring Without Repeating Characters 
**题：** <sup style="color:#ccc">23-09 00:00:29</sup>
从字符串中找到**最长**的子串，这个子串没有重复的字母，
要求你返回这个字符串的长度
```py
例子:
Given 'abcabcbb', the answer is 'abc', which the length is 3.
Given 'bbbbb', the answer is 'b', which the length is 1.
Given 'pwwkew', the answer is 'wke', which the length is 3.
(Note that the answer must be a substring, 'pwke' is a subsequence and not a substring)
```


**思路：** <sup style="color:#ccc">23-09 00:04:47</sup>





**code：** <sup style="color:#ccc">23-10 00:00:08 Ex.1</sup>
[link]()
```python
def lengthOfLongestSubstring(string):
    i = 0   # 左指针 有效窗口的头指针
    j = 0   # 右指针 遍历字符的指针

    char_s = set()  # 检测重复
    max_len = 0
    n = len(string)
    while i < n and j < n:
        if string[j] in char_s:     
            char_s.remove(string[i])
            i += 1                  # 遇到了重复的字符，打破窗口，移动 i, j 不用重置
        else:                       
            char_s.add(string[j])
            j += 1                  # 没有重复, 扩大
            # 更新最大子串长度
            cur_len = j - i
            max_len = max(max_len, cur_len)
    return max_len
```


------------------------------------------------------


## 2. 
**题：** <sup style="color:#ccc"></sup>





**思路：** <sup style="color:#ccc"></sup>


**code：** <sup style="color:#ccc"> Ex.</sup>
[link]()
```python

```


------------------------------------------------------


## 3. 最小的窗口子串 II
**题：** <sup style="color:#ccc"></sup>
给你一个字符串 a，和一个字符串 b，
要求你在 a 中找到最小的子串，使得子串中包含 b 中的所有字母

**思路：** <sup style="color:#ccc"></sup>


**code：** <sup style="color:#ccc"> Ex.</sup>
[link]()
```python
import sys

def minWindow(s, t):
    if len(t) > len(s):
        return ""
    lt = len(t)
    count = lt
    ct = collections.Counter(t)
    left = 0
    right = 0
    minLength = sys.maxsize
    notfound = 1
    ansleft = 0
    ansright = 0
    print(ct)
    for i in range(len(s)):
        # found in t
        if ct[s[i]] > 0:
            count -= 1
        ct[s[i]] -= 1
        #print(s[i], ct)
        # found a window, containing all chars from t
        while count == 0:
            right = i
            notfound = 0
            if right - left < minLength:
                minLength = right-left
                ansleft = left
                ansright = right
            # when map[left] is 0, meaning the exit char is in t, then count++
            if ct[s[left]] == 0:
                count += 1
            ct[s[left]] += 1
            #print("left: ", s[left], ct)
            left += 1
    if notfound == 1:
        return ""
    return s[ansleft:ansright+1]

```


------------------------------------------------------


## . 
**题：** <sup style="color:#ccc"></sup>





**思路：** <sup style="color:#ccc"></sup>


**code：** <sup style="color:#ccc"> Ex.</sup>
[link]()
```python

```


------------------------------------------------------


## . 
**题：** <sup style="color:#ccc"></sup>





**思路：** <sup style="color:#ccc"></sup>


**code：** <sup style="color:#ccc"> Ex.</sup>
[link]()
```python

```


------------------------------------------------------


## . 
**题：** <sup style="color:#ccc"></sup>





**思路：** <sup style="color:#ccc"></sup>


**code：** <sup style="color:#ccc"> Ex.</sup>
[link]()
```python

```


------------------------------------------------------


## . 
**题：** <sup style="color:#ccc"></sup>





**思路：** <sup style="color:#ccc"></sup>


**code：** <sup style="color:#ccc"> Ex.</sup>
[link]()
```python

```


------------------------------------------------------


## . 
**题：** <sup style="color:#ccc"></sup>





**思路：** <sup style="color:#ccc"></sup>


**code：** <sup style="color:#ccc"> Ex.</sup>
[link]()
```python

```


------------------------------------------------------


## . 
**题：** <sup style="color:#ccc"></sup>





**思路：** <sup style="color:#ccc"></sup>


**code：** <sup style="color:#ccc"> Ex.</sup>
[link]()
```python

```


------------------------------------------------------


## . 
**题：** <sup style="color:#ccc"></sup>





**思路：** <sup style="color:#ccc"></sup>


**code：** <sup style="color:#ccc"> Ex.</sup>
[link]()
```python

```


------------------------------------------------------


## . 
**题：** <sup style="color:#ccc"></sup>





**思路：** <sup style="color:#ccc"></sup>


**code：** <sup style="color:#ccc"> Ex.</sup>
[link]()
```python

```


------------------------------------------------------