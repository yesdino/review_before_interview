
```
a bytes-like object is required, not 'str'
```
bytes-like object 是 encode 的编码 就是机器编码 要用`.encode()` 转化成 bytes-like object。即 `b'字符串'` 的形式

注意 `open(path, 'rb')`用 rb 二进制形式打开的文件 操作的时候都要用机器编码 
即所有的字符串要加上 `.encode()` 转化成 bytes-like object