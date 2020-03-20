# 二分查找
#   思路：每次都找到中间所以的值比较目标值，并根据大小缩小一半的查找范伟

# 经常会让手写二分查找，要注意边界（其实 python 有个 bisect 模块 ）


# 【 二分查找 】 实现 (注意待查找序列要是有序序列)
def binary_serach(sorted_seq, val):
    if not sorted_seq:
        return -1
    
    begin = 0
    end = len(sorted_seq) - 1
    while begin <= end:
        mid = int((begin + end) / 2)    # int()屏蔽 2/3 差异
        if sorted_seq[mid] == val:
            return mid
        elif sorted_seq[mid] > val:
            end = mid - 1
        else:
            begin = mid + 1
    return -1

# 二分查找 测试用例
def test_binary_serach():
    import random
    test_seq = range(10)
    i = random.choice(test_seq)
    assert binary_serach(test_seq, i) == i

if __name__ == '__main__':
    test_binary_serach()