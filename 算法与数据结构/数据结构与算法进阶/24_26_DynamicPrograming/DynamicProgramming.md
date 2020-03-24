# 目录

[toc]

---


# 练习

## 1. 给定的数求和的不同方式。Number Problem

[程式：Ex.1 Number Problem](http://39.100.240.159:1234/notebooks/24-26_Dynamic_Programming/23_01_DynamicProgramming.ipynb#Ex1)

给一个 n, 求 1,3,4 相加得到 n 的所有相加方式

```python
def coin(n):
    dp = [0] * (n + 1)
    dp[0] = dp[1] = dp[2] = 1
    dp[3] = 2
    for i in range(4, n+1):
        # 由于是从下往上的原因，dp[i-1],dp[i-3],dp[i-4] 一定都是在上次循环中已经得到答案存入的 dp 数组的，所以计算速度会非常快
        dp[i] = dp[i-1] + dp[i-3] + dp[i-4]   # D(n) = D(n-1) + D(n-3) + D(n-4)
    return dp[n]


if __name__ == "__main__":
    print(coin(5))      # 6
    print(coin(10))     # 64
```
<br>




## 2. 入室抢劫。 House Robber
[程式：Ex.2 House Robber](http://39.100.240.159:1234/notebooks/24-26_Dynamic_Programming/23_01_DynamicProgramming.ipynb#Ex2)

**题：**
你是一个小偷，盯上一排房子，相邻的房子若都被抢将触动报警系统，每个房子里面有多少钱你都调查清楚了，
求不触动报警系统的情况下怎样才能入室抢劫抢到最多钱？

**思路：**
```
选择抢这个房子时 = 不抢上一个房子的情况 + 这个房子抢到的钱
选择不抢这个房子 = ( 不抢上一个房子 or 抢上一个房子的情况 ) 哪个大选哪个
```
|     公式 \ 数组                              |   8   |  3    |   5   |  7    |    6  |  9    |  2    |
| ----                              | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|  不抢：`No(i)  = max(Yes[i-1], No[i-1]` |   0   |   8   |  8    |  13    |  15    |  19    |   24   |
| 抢：`Yes(i) = No(i-1) + lis[i]`       |  8    |   3   |  13    |   15   |  19    |  24    |    21  |

<br>

**正解：**
```python
# 时间复杂度：O(n), 空间复杂度：O(n)
def rob(nums):
    n = len(nums)
    dp = [ [0] * 2 for _ in range(n + 1)]       # [[0, 0], [0, 0], [0, 0], ...]
    for i in range(1, n+1):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1])  # forget it
        dp[i][1] = nums[i-1] + dp[i-1][0]       # let's do it
    return max(dp[n][0], dp[n][1])


if __name__ == "__main__":
    nums = [2, 7, 9, 3, 1]
    print(rob(nums))
```


**改进：**
由于每一次我们都只需要上一次的而已，所以上上次、上上上次的都不要
```python
# 时间复杂度：O(n), 空间复杂度：O(1)
def rob(nums):
    yes, no = 0, 0
    for i in nums: 
        no, yes = max(no, yes), i + no
    return max(no, yes)


if __name__ == "__main__":
    nums = [2,7,9,3,1]
    print(rob(nums))
```

<br>




## 3. 入室抢劫（进阶）House Robber II

[程式：Ex.3 House Robber II](http://39.100.240.159:1234/notebooks/24-26_Dynamic_Programming/23_01_DynamicProgramming.ipynb#Ex3)


**题：**
你是一个小偷，盯上一 **<u>圆形</u>** 排列的街道房子，相邻的房子若都被抢将触动报警系统，每个房子里面有多少钱你都调查清楚了，
求不触动报警系统的情况下怎样才能入室抢劫抢到最多钱？
<u></u>

**思路：**
```
将圆拉开变成直线，变形成上面那道题。
不同点在于: 抢了第1个房子的话就不能抢最后一个(第n个)房子（圆形头尾相邻）
```



```python

```
<br>

<!-- ## 4. 组织聚会 Planning Party -->

<!-- [程式：Ex.4](http://39.100.240.159:1234/notebooks/24-26_Dynamic_Programming/23_01_DynamicProgramming.ipynb#Ex4) -->


```python

```
<br>

<!-- ## 5. 瓷砖问题 -->

<!-- [程式：Ex.5](http://39.100.240.159:1234/notebooks/24-26_Dynamic_Programming/23_01_DynamicProgramming.ipynb#Ex5) -->


```python

```
<br>

<!-- ## 6. 最小台阶问题 -->

<!-- [程式：Ex.6](http://39.100.240.159:1234/notebooks/24-26_Dynamic_Programming/23_01_DynamicProgramming.ipynb#Ex6) -->


```python

```
<br>

<!-- ## 7. 求编码方式 Decode Way -->

<!-- [程式：Ex.7](http://39.100.240.159:1234/notebooks/24-26_Dynamic_Programming/23_01_DynamicProgramming.ipynb#Ex7) -->


```python

```
<br>

<!-- ## 8. 独特二叉树的搜索路径 Unique Binary Search Tree -->

<!-- [程式：Ex.8](http://39.100.240.159:1234/notebooks/24-26_Dynamic_Programming/23_01_DynamicProgramming.ipynb#Ex8) -->


```python

```
<br>


<!-- ## 9. 最大子序列乘积 Maximum Product Subarray -->

<!-- [程式：Ex.9](http://39.100.240.159:1234/notebooks/24-26_Dynamic_Programming/23_01_DynamicProgramming.ipynb#Ex9) -->


```python

```






