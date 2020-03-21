[toc]

---

## defaultdict

value 有默认默认值的 dict, 不用进行“++如果 key not in dict, 设定 value 默认值++” 的这个动作
```py
# 复制到 vscode 看用法
from collections import defaultdict

s = [
    ('yellow', 1), 
    ('blue', 2), 
    ('yellow', 3), 
    ('blue', 4), 
    ('red', 1)
]

default_dic = defaultdict(list) # 字典 value 类型默认为 []
print(default_dic)

for k, v in s:
    default_dic[k].append(v)

print(default_dic)
# defaultdict(<class 'list'>, {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]})
```


## OrderedDict

有序字典
```py
# 复制到 vscode 看用法
from collections import OrderedDict

print("-"*90)
print ("Regular dictionary")
d={}
d['a']='A'
d['b']='B'
d['c']='C'
for k,v in d.items():
    print (k,v)

print ("\nOrder dictionary")
d1 = OrderedDict()
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'
d1['1'] = '1'
d1['2'] = '2'
for k,v in d1.items():
    print (k,v)

# -------------------------------------------------------
# 无序字典比较 只要比较 key value 是否成对相同就可
print("-"*30)
print ('Regular dictionary:')
d2={}
d2['a']='A'
d2['b']='B'
d2['c']='C'

d3={}
d3['c']='C'
d3['a']='A'
d3['b']='B'

print ("d2 == d3: ", d2 == d3)  # True

# 有序字典比较 还要比较顺序
print ('\nOrderedDict:')
d4=OrderedDict()
d4['a']='A'
d4['b']='B'
d4['c']='C'

d5=OrderedDict()
d5['c']='C'
d5['a']='A'
d5['b']='B'

print ( "d1==d2: ", d1==d2)     # False
print ( "\n")

# -------------------------------------------------------
# 排序
dd = {
    'banana': 3, 
    'apple':4, 
    'pear': 1, 
    'orange': 2
}
#按key排序
kd = OrderedDict(sorted(dd.items(), key=lambda t: t[0]))
print (kd)
#按照value排序
vd = OrderedDict(sorted(dd.items(),key=lambda t:t[1]))
print (vd)
```
