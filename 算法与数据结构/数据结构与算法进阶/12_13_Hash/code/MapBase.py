class MapBase():
    
    class _Item:
        __slots__ = '_key' , '_value'   # 实例化之后，外界只能操作 _key, _value 这两个属性
        
        def __init__ (self, k, v):
            self._key = k
            self._value = v
            
        def __eq__ (self, other):
            return self._key == other._key
        
        def __ne__ (self, other):
            return not (self == other)
        
        def __lt__ (self, other):
            return self._key < other._key
        
        def __print__ (self):
            print(str(self._key) + ":" + str(self._value),  end = ", ")