# 快速排序
# 思路：递归
#   1. 从 序列 seq 中选第一个参数作为基准数 base
#   2. 以 base 作为基准比较 seq, 比 base 小的 left_part 放 base 前面，比 base 大的 right_part 放 base 后面
#   3. left_part, right_part 分别重复 1.2 步骤

# 实现
def quicksort(seq):
    if len(seq) < 2:
        return seq    # 递归出口
    else:
        base_idx = 0
        base = seq[base_idx]
        left_part = [i for i in seq[base_idx+1:] if i<= base]
        right_part = [i for i in seq[base_idx+1:] if i > base]
    return quicksort(left_part) + [base] +quicksort(right_part)   # 递归 合并

# 测试用例
def test_quicksort():
    import random
    test_seq = list(range(10))
    random.shuffle(test_seq)    # 打乱顺序
    # print(test_seq)
    assert quicksort(test_seq) == sorted(test_seq)  # 没报错就没错

# 运行测试用例
test_quicksort()