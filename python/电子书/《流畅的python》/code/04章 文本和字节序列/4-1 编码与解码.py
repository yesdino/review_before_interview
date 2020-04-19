s = 'café'
tmp = len(s)            # 'café'拥有4个Unicode字符
print(tmp)              
# 4

# encode: 编码
b = s.encode('utf8')    # 利用 UTF-8 编码将 str 编码为 bytes（bytes 字面量以 b 开头
print(b)                
# b'caf\xc3\xa9'
tmp = len(b)
print(tmp)              # 字节序列 b 有5 个字节（在 UTF-8 中，é 的码位编码成两个字节）。
# 5

# decode: 解码
tmp = b.decode('utf8')  # 使用 UTF-8 编码把 bytes 对象解码成 str 对象
print(tmp)
# café
