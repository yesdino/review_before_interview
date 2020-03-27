"""
12-2　dict.update 方法会忽略AnswerDict.__getitem__ 方法
"""

class AnswerDict(dict):
    def __getitem__(self, key): # ➊ 不管传入什么键，AnswerDict.__getitem__ 方法始终返回42。
        return 42


ad = AnswerDict(a='foo')# ➋ ad 是AnswerDict 的实例，以('a', 'foo') 键值对初始化。
tmp = ad['a']           # ➌ ad['a'] 返回42，这与预期相符。
print(tmp)
# 42

d = {}
d.update(ad)            # ➍ d 是dict 的实例，使用 ad 中的值更新d。
tmp = d['a']            # ➎ dict.update 方法忽略了 AnswerDict.__getitem__ 方法。
print(tmp)
# 'foo'

tmp = d
print(tmp)
# {'a': 'foo'}