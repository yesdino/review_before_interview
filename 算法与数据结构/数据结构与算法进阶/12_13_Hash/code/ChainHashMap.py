from HashMapBase import HashMapBase
from SimpleUnsortedTableMap import UnsortedTableMap

class ChainHashMap(HashMapBase):
    """
    Hash 表使用 开放链表法 解决冲突
    """
    def _bucket_getitem(self, j, k):
        bucket = self._table[j]     # bucket: self._table[j] 位置上再嵌套的一个数组
        if bucket is None:
            raise ValueError( 'Key Error: ' + repr(k)) # no match found
        return bucket[k] # may raise KeyError

    def _bucket_setitem(self, j, k, v):
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap( ) # bucket is new to the table
        oldsize = len(self._table[j])
        self._table[j][k] = v
        if len(self._table[j]) > oldsize: # key was new to the table
            self._n += 1 # increase overall map size

    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError( 'Key Error: ' + repr(k)) # no match found
        del bucket[k] # may raise KeyError

    def __iter__ (self):
        for bucket in self._table:
            if bucket is not None: # a nonempty slot
                for key in bucket:
                    yield key
                    
    def _print_ (self):
        for bucket in self._table:
            if bucket is not None: # a nonempty slot
                bucket.__print__()
 

 