cafe = bytes('café', encoding='utf_8') # ➊ bytes 对象可以通过 str 对象使用给定的编码构建
print(cafe)
# b'caf\xc3\xa9'
print(cafe[0])              # ➋ bytes 对象中的各个元素是 0~256 内的整数。
# 99
print(cafe[:1])             # ➌ bytes 对象的切片还是 bytes 对象，即使是只有一个字节的切片。
# b'c'

# ---------------------------------------------------------------------------------------------------------
cafe_arr = bytearray(cafe)
print(cafe_arr)             # ➍ bytearray 对象没有字面量句法，而是以 bytearray() 和字节序列字面量参数的形式显示。
# bytearray(b'caf\xc3\xa9')

print(cafe_arr[-1:])        # ➎ bytearray 对象的切片还是bytearray 对象。
# bytearray(b'\xa9')