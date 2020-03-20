## python中时间 time 模块

## 时间日期格式化
### 1. strftime() 时间元祖 → 时间字符串
- 格式
```py
# 接收以时间元组，并返回以可读字符串表示的当地时间，格式由fmt决定。
time.strftime(fmt[,tupletime])
```
- 实例
```py
import time

print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# 2016-04-07 11:18:05
```

### 2. strptime() 时间字符串 → 时间元祖
- 格式
```py
# 根据fmt的格式把一个时间字符串解析为时间元组。
time.strptime(str,fmt='%a %b %d %H:%M:%S %Y')
```
- 实例
```py
import time

struct_time = time.strptime("30 Nov 00", "%d %b %y")
print ("返回元组: ", struct_time)
# 返回元组:  time.struct_time(tm_year=2000, tm_mon=11, tm_mday=30, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=335, tm_isdst=-1)
```

### 格式化形式 汇总
```py
    %y 两位数的年份表示（00-99）
    %Y 四位数的年份表示（000-9999）
    %m 月份（01-12）
    %d 月内中的一天（0-31）
    %H 24小时制小时数（0-23）
    %I 12小时制小时数（01-12）
    %M 分钟数（00=59）
    %S 秒（00-59）
    %a 本地简化星期名称
    %A 本地完整星期名称
    %b 本地简化的月份名称
    %B 本地完整的月份名称
    %c 本地相应的日期表示和时间表示
    %j 年内的一天（001-366）
    %p 本地A.M.或P.M.的等价符
    %U 一年中的星期数（00-53）星期天为星期的开始
    %w 星期（0-6），星期天为星期的开始
    %W 一年中的星期数（00-53）星期一为星期的开始
    %x 本地相应的日期表示
    %X 本地相应的时间表示
    %Z 当前时区的名称  # 乱码
    %% %号本身

    时间元组（年、月、日、时、分、秒、一周的第几日、一年的第几日、夏令时）
        一周的第几日: 0-6
        一年的第几日: 1-366
        夏令时: -1, 0, 1
```

## 时间格式转换函数

```py
#!/usr/bin/python

import time
import calendar
```

### 1. time() 当前时间戳
```py
time.time()
# 1538271871.226226
```

### 2. localtime() 时间戳 → 时间元组，默认为当前时间

```py
time.localtime()
time.localtime(1538271871.226226)
# time.struct_time(tm_year=2018, tm_mon=9, tm_mday=3, tm_hour=9, tm_min=4, tm_sec=1, tm_wday=6, tm_yday=246, tm_isdst=0)
```

### 3. ctime() 时间戳 → 可视化时间
```py
time.ctime(1538271871.226226)
# time.ctime(时间戳)，默认为当前时间
```

### 4. mktime() 时间元组 → 时间戳
```py
time.mktime((2018, 9, 30, 9, 44, 31, 6, 273, 0))
# 1538271871
```

### 5. asctime() 时间元组 → 可视化时间
```py
time.asctime()
time.asctime((2018, 9, 30, 9, 44, 31, 6, 273, 0))
time.asctime(time.localtime(1538271871.226226))
# time.asctime(时间元组)，默认为当前时间
```

### 6. strftime() 时间元组 → 可视化时间（定制）
```py
# time.strftime(要转换成的格式，时间元组)
time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
```

### 7. strptime() 可视化时间（定制） → 时间元祖
```py
# time.strptime(时间字符串，时间格式)
print(time.strptime('2018-9-30 11:32:23', '%Y-%m-%d %H:%M:%S'))
```

### 8. clock() 浮点数秒数，用于衡量不同程序的耗时，前后两次调用的时间差
```py
time.clock()
```