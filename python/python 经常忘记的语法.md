#### python经常忘记的语法: 
<br>
先复制再添加

------------------------------------------------------------
#### 
```python


```

------------------------------------------------------------
#### 
不支持原地修改的類型有: **字符串** **元祖**

------------------------------------------------------------
#### 可迭代 Iterable 对象 ： 可以用 for ... in ... 循环的对象

```python
# 判断是否为可迭代 Iterable 对象
from collections import Iterable
print(isinstance([], Iterable))
```
------------------------------------------------------------
#### 排序函数 sort() sorted()
<b>sort():  应用在 list 上的方法</b>
```python


```
<b>sorted(): 可以对所有可迭代的对象进行排序操作</b>
语法： sorted( iterable[ , cmp[, key[, reverse]] ] )
- iterable -- 可迭代对象。
- cmp -- 比较的函数，这个具有两个参数，参数的值都是从可迭代对象中取出，此函数必须遵守的规则为，大于则返回1，小于则返回-1，等于则返回0。
- key -- 用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
- reverse -- 排序规则，reverse = True 降序有小到大 ， reverse = False 升序由大到小（默认）。
```python
>>> L=[('b',2), ('a',1), ('c',3), ('d',4)]

>>> sorted(L, cmp=lambda x,y:cmp(x[1],y[1]))   # 利用cmp函数 这个: x,y 均表示循环遍历的列表 L 中的每一个元素,只是用不同的变量名表示对应不同的操作而已
# [('a', 1), ('b', 2), ('c', 3), ('d', 4)]

>>> sorted(L, key=lambda x:x[1])               # 利用key
# [('a', 1), ('b', 2), ('c', 3), ('d', 4)]

students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
>>> sorted(students, key=lambda s: s[2], reverse=True)       # 按每个元素中的第三个元素降序排序
# [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
```

------------------------------------------------------------
#### lambda 表达式 : lambda [arg1 [,arg2,.....argn]]:expression
使用 lambda 来创建 <b>匿名函数</b>
- lambda 只是一个表达式，函数体比def简单很多。
- lambda 的主体是一个表达式，而不是一个代码块。仅仅能在 lambda 表达式中封装有限的逻辑进去。
- lambda 函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。
- 虽然 lambda 函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率
```python
# 注意声明时函数名称后面不带 (), 调用时才带
sum = lambda arg1, arg2: arg1 + arg2

# 调用sum函数
print "相加后的值为 : ", sum( 10, 20 )
print "相加后的值为 : ", sum( 20, 20 )
```

------------------------------------------------------------
#### 列表推导式：x for x in a
```python
print [ x*2 for x in list_a ]   # 循环列表计算输出 x
```

------------------------------------------------------------
#### 栈 : 先入先出 两边开口
```python
# 用列表表示
stack = []
# 把栈元素推出栈 用删除列表元素的pop()方法 还会返回删除的元素 即推出去的那个栈元素
top_element = stack.pop()   # top_element：被推出去的栈顶元素
# 把元素推入栈 尾部追加的方式
stack.append(element)
```

------------------------------------------------------------
#### 节点
```python
# 树状结构
# max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1

```
------------------------------------------------------------
#### join(): 拼接生成字符串
格式：连接符.join(要连接的元组、列表、字典、字符串)
```python
list=['1','2','3','4','5']
print(''.join(list))
# 结果：12345

dict = {'hello':'nihao','good':2,'boy':3,'doiido':4}
print('-'.join(dict))        # 字典只对键进行连接
# 结果：hello-good-boy-doiido
```

------------------------------------------------------------
#### 遍历
```python
# ① 遍历列表，字典，集合
for item in list/dict/set:
    # item为里面的每一个元素
    
# ② 遍历字符串
for i in range( len(str) ):
    # str[i]为字符串str的每一个字符
```

------------------------------------------------------------
## 字符串
<u>在Python中，字符串属于不可变对象，不支持原地修改</u>

##### 字符串运算
```python
    a = 'hello'
    b = 'python'
    
>>> a + b   # hellopython
>>> a * 2   # hellohello
```
##### Unicode 字符串
引号前小写的 "u" 表示这里创建的是一个 Unicode 字符串
```python
>>> u'Hello World !'
# u'Hello World !'
```

---------------------------------------------------------
#### ASCII操作

```python
# 字符 -> ASCII码值
ord('a')    
# ASCII码值 -> 字符
chr(101)     
    
# 字符串中大写字母转换为小写字母
string = ''     # 字符串是不可变的 所以只能新建 原字符串不能改变
for i in range(len(str)):
    s = str[i]
    # 注意python 不能像C语言一样那字符直接加ASCII码值 一定要先转换
    if ord(s)>=65 and ord(s)<=90:
        tmp = chr(ord(s)+32)
        string += tmp
    else:
        string += s
return string
```

---
#### 刪除列表 pop,remove
```python
list[]
# ① 索引刪除
list.pop(index)
del list[index]
# ② 值刪除
list.remove(value)
```

---
#### 添加列表元素 append
```python
list[]
list.append(value)
```

---
#### 追加列表 extend
相当于合并列表，在一个列表后面加另一个列表
```python
total_list = []
add_list = []
total_list.extend(add_list)
```

---
#### 添加集合 set (不重复)
```python
tmp_set = set()     # 声明 set
set.add(value)
```

---
#### range( len(S) )
```python
# 遍历字符串
    S = "aAAbbbb"
    for i in range(len(S)):
        per_string = S[i]   # per_string 是字符串 S 中的每一个字符
```

---
#### if ... in ... 
#### if ... not in ...
检测是否为 list/dict/set 中的元素
```python
mapping = {")": "(", "}": "{", "]": "["}
if char in mapping:
    ...
```

#### while ... in ... 
当是 list/dict/set 中的元素时
```python
# 查找指定字符串并執行特定動作
ops = []
while 'C' in ops:
...
```
---
#### sum
```python
# 直接計算list總和，元素需為整數
sum(ops)
```

---
#### isinstance
```python
# 判斷類型
isinstance(a,int)   # 判斷變量a是否為int
# 輸出 True/False
```

---
#### type
```python
# 輸出類型
type(a)
```

---
#### int()
```python
# int()會報異常 只是系統放過了這個異常沒去處理而已，但是如果你去捕捉就能捕捉得到
try:
    int(a)
except:
    pass
```












