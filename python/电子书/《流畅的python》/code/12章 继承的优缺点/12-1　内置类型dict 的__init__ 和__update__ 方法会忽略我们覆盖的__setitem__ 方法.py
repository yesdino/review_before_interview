

class DoppelDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2) # ➊ DoppelDict.__setitem__ 方法会重复存入的值（只是为了提供易于观察的效果）。它把职责委托给超类。
   

dd = DoppelDict(one=1)      # ➋ 继承自dict 的__init__ 方法显然忽略了我们覆盖的__setitem__ 方法：'one' 的值没有重复。
print(dd)                   # {'one': 1}

dd['two'] = 2               # ➌ [] 运算符会调用我们覆盖的__setitem__ 方法，按预期那样工作：'two' 对应的是两个重复的值，即[2, 2]。
print(dd)                   # {'one': 1, 'two': [2, 2]}

dd['two'] = 3
print(dd)                   # {'one': 1, 'two': [3, 3]}

dd.update(three=3)          # ➍ 继承自 dict 的update 方法也不使用我们覆盖的__setitem__ 方法：'three' 的值没有重复。
print(dd)                   # {'three': 3, 'one': 1, 'two': [3, 3]}