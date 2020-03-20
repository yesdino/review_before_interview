
[toc]

---

# 回溯题型汇总

## 78. 子集


[leetcode](https://leetcode-cn.com/problems/subsets/submissions/)

给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。


```
示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
```

![image](http://39.100.240.159:1234/notebooks/images/ch03/Backtracking.jpg)

==这题非常的重要 是所有回溯变形的根源==
```py
class Solution(object):
    def subsets(self, nums):
        
        def subsets_help(tmp_lis, nums, result, position):
            result.append(tmp_lis[:])
            for i in range(position, len(nums)):
                # tmp_lis.append(nums[i])
                subsets_help(tmp_lis+[nums[i]], nums, result, i+1)
                # tmp_lis.pop()
    
        tmp_lis = []
        result = []
        position = 0
        subsets_help(tmp_lis, nums, result, position)
        return result
```

---

## 90. 子集 II

[leetcode](https://leetcode-cn.com/problems/subsets-ii/)

给定一个可能包含 **重复元素** 的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。


```
示例:
输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
```

```py
class Solution(object):
    def subsetsWithDup(self, nums):
        result = []
        tmp_lis = []
        nums.sort()
        self.subsetsWithDup_help(result, tmp_lis, nums, 0)
        return result
    
    def subsetsWithDup_help(self, result, tmp_lis, nums, position):
        result.append(tmp_lis[:])
        for i in range(position, len(nums)):
            if i != position and nums[i] == nums[i-1]:
                continue
            tmp_lis.append(nums[i])
            self.subsetsWithDup_help(result, tmp_lis, nums, i+1)
            tmp_lis.pop()
```

---

## 60. 第k个排列

[leetcode](https://leetcode-cn.com/problems/permutation-sequence/)

给出集合 `[1,2,3,…,n]`，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 `n = 3` 时, 所有排列如下：
```
"123"
"132"
"213"
"231"
"312"
"321"
```

给定 n 和 k，返回 **第 k 个** 排列。

说明：

给定 n 的范围是 [1, 9]。
给定 k 的范围是[1,  n!]。

```
示例 1:
输入: n = 3, k = 3
输出: "213"

示例 2:
输入: n = 4, k = 9
输出: "2314"
```

这题真的做不出来 打印就可以

---

## 46. 全排列

给定一个没有重复数字的序列，返回其所有可能的全排列。


```
示例:
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
```

```py
class Solution(object):
    def permute(self, nums):
        result = []
        tmp_lis = []
        self.permute_help(result, tmp_lis, nums)
        return result
    
    def permute_help(self, result, tmp_lis, nums):
        if len(nums) == 0:
            result.append(tmp_lis) 
            return
        for i in range(len(nums)):
            self.permute_help(result, tmp_lis+[nums[i]], nums[0:i]+nums[i+1:])
```

---

## 47. 全排列 II

[leetcode](https://leetcode-cn.com/problems/combination-sum/)

思路和上面的去重一样


---

## 39. 组合总和

[leetcode](https://leetcode-cn.com/problems/combination-sum/)

给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 


```
示例 1:
输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]

示例 2:
输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
```


```py
class Solution(object):
    def combinationSum(self, candidates, target):
        
        def combinationSumHelp(nums, remains, tmp_lis, result, start):
            if remains < 0:
                return 
            
            if remains == 0:
                result.append(tmp_lis[:])
                
            for i in range(start, len(nums)):
                tmp_lis.append(nums[i])
                combinationSumHelp(nums, remains-nums[i], tmp_lis, result, i)
                tmp_lis.pop()
        
        tmp_lis = []
        result = []
        combinationSumHelp(candidates, target, tmp_lis, result, 0)
        return result
```

---

## 40. 组合总和 II

[leetcode](https://leetcode-cn.com/problems/combination-sum-ii/)

给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 


```
示例 1:
输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

示例 2:
输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]
```

```py
class Solution(object):
    def combinationSum2(self, candidates, target):
        
        def combinationSum2Help(nums, remains, result, tmp_lis, start):
            if remains < 0:
                return 
            
            if remains == 0:
                result.append(tmp_lis[:])
                return
            
            for i in range(start, len(nums)):
                # if i!=0 and nums[i]==nums[i-1]:
                if i>start and nums[i]==nums[i-1]:
                    continue
                tmp_lis.append(nums[i])
                combinationSum2Help(nums, remains-nums[i], result, tmp_lis, i+1)
                tmp_lis.pop()
        
        candidates.sort()
        result = []
        combinationSum2Help(candidates, target, result, [], 0)
        return result
```


