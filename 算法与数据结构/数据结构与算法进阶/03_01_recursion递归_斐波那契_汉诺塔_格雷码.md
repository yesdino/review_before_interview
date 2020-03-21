[toc]

---


# Recursion

By the end of this chapter, you should be able to answer these questions.

- How does Python determine the meaning of an identifier in a program?
- What happens to the run-time stack when a function is called?
- What happens to the run-time stack when a function returns from a call?
- What are the two important parts to a recursive function and which part comes first?
- Exactly what happens when a return statement is executed?
- Why should we write recursive functions?
- What are the computational complexities of various recursive functions?

<a href='#Ex1'>Ex.1 求和</a>

<a href='#Ex2'>Ex.2 阶乘</a>

<a href='#Ex3'>Ex.3 斐波那契数列</a>

<a href='#Ex4'>Ex.4 打印尺子</a>

<a href='#Ex5'>Ex.5 数学表达式</a>

<a href='#Ex6'>Ex.6 汉诺塔</a>

<a href='#Ex7'>Ex.7 格雷码</a>

### <a id='Ex1'>Ex.1 Simple Example 求和 </a>


```python
n = 10
result = sum(range(n+1))
result
```

- **循环**
```python
def mysum(n):
    result = 0
    for i in range(n+1):
        result += i
    return result
```


- **递归**
```python
def mysum_recursive(n):
    if n == 0:
        return 0
    return n + mysum_recursive(n-1)

    
print(mysum_recursive(1500))
# RecursionError
```





注意：

在 python 中会限制递归的上限，即 **最大深度** ,大概为 1000 左右

当超过最大深度时会报错：

**RecursionError: maximum recursion depth exceeded in comparison**

当你的代码逻辑不对，程序找不到递归出口时，也容易报这个错误。

### <a id='Ex2'>Ex.2 阶乘 </a>

- **循环**
```python
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


factorial(5)
```


- **递归**
```python
def factorial_recursive(n):
    if n == 1:
        return 1
    return n * factorial_recursive(n - 1)


factorial_recursive(5)
# 120
```




<img src="../images/ch02/factorial.jpg" width="450"/>

递归缺点：吃内存
<img src="../images/ch03/use_space.png" width="350"/>

### <a id='Ex3'>Ex.3 斐波那契数列 </a>

1 1 2 3 5 8 13 21 ...

f(n) = f(n-1) + f(n-2)


- **错误写法**
```python
# 错误写法
def fibonacci1(n):
    assert(n>=0)
    if (n <= 2): 
        return 1
    return fibonacci1(n-1) + fibonacci1(n-2)    # O(2^n)指数增长



time fibonacci1(30)
# CPU times: user 274 ms, sys: 0 ns, total: 274 ms
# Wall time: 279 ms

# 832040
```




- **循环写法** O(n)
```python
# 斐波那契数列 循环写法 O(n)
def fibonacci2(n):
    assert(n>=0)
    a, b = 0, 1
    for i in range(1, n+1):
        a, b = b, a + b
    return a    


time fibonacci2(40)
# CPU times: user 7 µs, sys: 1e+03 ns, total: 8 µs
# Wall time: 11.7 µs

# 102334155
```



- **递归写法** O(n)
```python
# 斐波那契数列 递归写法 O()
def fibonacci3(n):
    assert(n>=0)
    if (n <= 1): 
        return (n,0)
    (a, b) = fibonacci3(n-1)
    return (a+b, a)    # 得到一个 pair 需要选择一个数


time fibonacci3(40)
# CPU times: user 23 µs, sys: 3 µs, total: 26 µs
# Wall time: 29.8 µs

# (102334155, 63245986)
```



**Why Fibonacci?**  为什么要使用斐波那契数列？


```python
def fibonaccis(n):
    assert(n>=0)
    result = [0, 1]
    for i in range(2, n+1):
        result.append(result[-2] + result[-1])
    return result
```


```python
# 计算斐波那契数列百分比 即用当前数减去前面一个数 得到数字基本固定为 1.618 黄金比例
fibos = fibonaccis(30)
r = []
for i in range(2, len(fibos)):
    r.append(fibos[i] / fibos[i-1])
r
# [1.0,
# 2.0,
# 1.5,
# 1.6666666666666667,
# 1.6,
# 1.625,
# 1.6153846153846154,
# 1.619047619047619,
# 1.6176470588235294,
# 1.6181818181818182,
# 1.6179775280898876,
# 1.6180555555555556,
# 1.6180257510729614,
# 1.6180371352785146,
# 1.618032786885246,
# 1.618034447821682,
# 1.6180338134001253,
# 1.618034055727554,
# 1.6180339631667064,
# 1.6180339985218033,
# 1.618033985017358,
# 1.6180339901755971,
# 1.618033988205325,
# 1.618033988957902,
# 1.6180339886704431,
# 1.6180339887802426,
# 1.618033988738303,
# 1.6180339887543225,
# 1.6180339887482036]
```







**黄金比例：** 肚脐到脚的距离／身高＝0.618
<img src="../images/ch03/beauty.png" width="200"/>

Fibonacci square 
<img src="../images/ch03/fibosquare.png" width="250"/>
<img src="../images/ch03/shell.jpg" width="250"/>
<img src="../images/ch03/fibo2.png" width="500"/>

### <a id='Ex4'>Ex.4 打印尺子 </a>

1

1 2 1

1 2 1 3 1 2 1

1 2 1 3 1 2 1 4 1 2 1 3 1 2 1


规律：

**f(n) = f(n-1) + n + f(n-1)**


```python
# O(2^n) 指数增长
def ruler_bad(n):    # bad code
    assert(n>=0)
    if (n==1):
        return "1"
    return ruler(n-1) + " " + str(n) + " " + ruler(n-1)
```

```python
# O(n)
def ruler(n):
    assert(n>=0)
    if (n==1):
        return "1"
    t = ruler(n-1)    # 把结果暂存起来 不重复计算
    return t + " " + str(n) + " " + t

# 循环写法
def ruler2(n):
    result = ""
    for i in range(1, n+1):
        result = result + str(i) + " " + result
    return result
```


```python
ruler_bad(3)
```


```python
ruler(3)
```


```python
ruler2(3)
```

**打印尺子**


```python
def draw_line(tick_length, tick_label=''):
    line = '-' * tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)

def draw_interval(center_length):nnn
    if center_length > 0:
        draw_interval(center_length - 1)
        draw_line(center_length)
        draw_interval(center_length - 1)
        
def draw_rule(num_inches, major_length):
    draw_line(major_length, '0')
    for j in range(1, 1 + num_inches):
        draw_interval(major_length - 1)
        draw_line(major_length, str(j))
```


```python
draw_interval(3)   # 只打印尺标

-
--
-
---
-
--
-
```



```python
draw_rule(5,3)   # 打印尺标、数字
--- 0
-
--
-
--- 1
-
--
-
--- 2
-
--
-
--- 3
-
--
-
--- 4
-
--
-
--- 5
```




### <a id='Ex5'>Ex.5 数学表达式  </a>

Given two integers a ≤ b, write a program  that transforms a into b by a minimum sequence of increment (add 1) and unfolding (multiply by 2) operations.

提供两个整形 a, b (a ≤ b)。 对 a 进行**最少**的运算得到 b: 只有两种运算方式：**a \* 2** 或者 **a + 1**


For example, 	

23 = ((5 * 2 + 1) * 2 + 1) 

113 = ((((11 + 1) + 1) + 1) * 2 * 2 * 2 + 1)




```python
def intSeq(a, b):
    if (a == b):      # 递归出口
        return str(a)
    
    # b 是奇数
    if (b % 2 == 1):
        return "(" + intSeq(a, b-1) + " + 1)"
    
    # b 是偶数
    if (b < a * 2):                 # b 小于 2a
        return "(" + intSeq(a, b-1) + " + 1)"
    return intSeq(a, b/2) + " * 2"; # b 大于 2a : 直接除以 2 然后进行下一轮递归
```


```python
a = 5
b = 101
print(str(b) + " = " + intSeq(a, b))
# 101 = (((5 + 1) * 2 * 2 + 1) * 2 * 2 + 1)
```




### <a id='Ex6'>Ex.6 汉诺塔  </a>

<img src="../images/ch02/hanoi.jpg" width="350"/>


```python
def hanoi(n, start, end, by):
    if (n==1):
        print("Move from " + start + " to " + end)
    else:
        hanoi(n-1, start, by, end)
        hanoi(1, start, end, by)
        hanoi(n-1, by, end, start)
```


```python
n = 3
hanoi(n, "START", "END", "BY")
```

    Move from START to END
    Move from START to BY
    Move from END to BY
    Move from START to END
    Move from BY to START
    Move from BY to END
    Move from START to END


### <a id='Ex7'>Ex.7 格雷码  </a>
<img src="../images/ch03/grey.jpg" width="350"/>


```python
def moves(n):    # 只打印 move 不打印 enter exit
    if n == 0:
        return
    moves(n-1)
    print(n)
    moves(n-1)


moves(3)
# 1
# 2
# 1
# 3
# 1
# 2
# 1
```



```python
def moves_ins(n, forward):
    if n == 0: 
        return
    moves_ins(n-1, True)
    print("enter ", n) if forward else print("exit  ", n)
    moves_ins(n-1, False)  


moves_ins(3, True)
# enter  1
# enter  2
# exit   1
# enter  3
# enter  1
# exit   2
# exit   1
```




**Why Grey Code?**

格雷码应用：

与非门：异或<img src="../images/ch03/grey1.jpg" width="250"/>
<img src="../images/ch03/grey2.png" width="380"/>


```python

```


```python

```
