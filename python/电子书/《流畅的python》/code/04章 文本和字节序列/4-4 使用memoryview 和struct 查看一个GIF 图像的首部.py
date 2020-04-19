'''
用 struct 模块处理 byte 对象
'''
import struct

img_path = u'E:\\code\\GitHub\\review_before_interview\\python\\电子书\\《流畅的python》\\code\\04章 文本和字节序列\\2020-04-18093851.png'
with open(img_path, 'rb') as fp:
    img = memoryview(fp.read())     # ➋ 使用内存中的文件内容创建一个 memoryview 对象
header = img[:10]                   # ➌ 然后使用它的切片再创建一个memoryview 对象；这里不会复制字节序列
print(bytes(header))                # ➍ 转换成字节序列，这只是为了显示；这里复制了 10 字节
# b'\x89PNG\r\n\x1a\n\x00\x00'

fmt = '<3s3sHH'                     # ➊ 设置结构体的格式：< 是小字节序，3s3s 是两个 3 字节序列，HH 是两个 16 位二进制整数
print(struct.unpack(fmt, header))   # ➎ 拆包 memoryview 对象，得到一个元组，包含类型、版本、宽度和高度
# (b'\x89PN', b'G\r\n', 2586, 0)

del header                          # ➏ 删除引用，释放 memoryview 实例所占的内存
del img