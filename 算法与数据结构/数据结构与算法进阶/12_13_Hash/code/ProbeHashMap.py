from HashMapBase import HashMapBase
from SimpleUnsortedTableMap import UnsortedTableMap

class ProbeHashMap(HashMapBase):
    """
    Hash map implemented with linear probing for collision resolution.
    Hash 表使用 线性探索法 解决冲突
    """
    _AVAIL = object()       # sentinal marks locations of previous deletions

    def _is_available(self, j):
        """Return True if index j is available in table. 课上说的 delete flag"""
        return self._table[j] is None or self._table[j] is ProbeHashMap._AVAIL

    def _find_slot(self, j, k):
        """
        找 [格子]，即参数对应的那个位置
        Search for key k in bucket at index j.
        Return (success, index) tuple, described as follows:
        If match was found, success is True and index denotes its location.
        If no match found, success is False and index denotes first available slot.
        """
        firstAvail = None
        while True:                             # 一直找到一个空位置为止
            if self._is_available(j):
                if firstAvail is None:          # 没有放过元素在这个位置
                    firstAvail = j              # mark this as first avail
                if self._table[j] is None:
                    return (False, firstAvail)  # search has [failed]
            elif k == self._table[j]._key:
                return (True, j)                # found a match [success]
            j = (j + 1) % len(self._table)      # keep looking (cyclically)

    def _bucket_getitem(self, j, k):
        """ 在内部 hash 数组中 self._table 中获取 """
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error: ' + repr(k))     # no match found
        return self._table[s]._value

    def _bucket_setitem(self, j, k, v):
        """ 在内部 hash 数组中 self._table 中设置值 """
        found, s = self._find_slot(j, k)
        if not found:
            self._table[s] = self._Item(k,v)               # insert new item
            self._n += 1                                   # size has increased
        else:
            self._table[s]._value = v                      # overwrite existing

    def _bucket_delitem(self, j, k):
        print(j, k)
        found, s = self._find_slot(j, k)
        print(found, s)
        if not found:
            raise KeyError('Key Error: ' + repr(k))        # no match found
        self._table[s] = ProbeHashMap._AVAIL             # mark as vacated

    def __iter__(self):
        for j in range(len(self._table)):                # scan entire table
            if not self._is_available(j):
                yield self._table[j]._key
                
    def _print_ (self):
        for bucket in self._table:
            if bucket is not None: # a nonempty slot
                bucket.__print__()
                