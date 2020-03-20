import random
"""
【 冒泡排序 】
思路：
每一轮都依次选择相邻两个元素，不符合排序顺序就交换。
接着进行下一轮
"""
def bubbleSort(lis):
    for i in range(len(lis)-1):         # 要进行多少轮
        for j in range(len(lis)-i-1):   # 每一轮的比较范围 len(lis)—i-1:后面的黑色的已经排序好的不再继续比较
            if lis[j] > lis[j+1]:       # 比较范围内两两比较
                lis[j], lis[j+1] = lis[j+1], lis[j]
    return lis

"""
【 插入排序 】
思路：
排麻将一样，每一轮里面依次挑一个数，到了合适的位置后面的位置都往后搓
"""
def insertSort(lis):
    for cur_idx in range(1, len(lis)):      # 1,2,3..., n-1: 红色的那个数从第2个数到最后一个数
        for j in range(cur_idx):
            if lis[cur_idx] < lis[j]:       # 红色的那个数 和 黑色的列表里面的数全部比一遍
                lis.insert(j, lis[cur_idx]) # lis[cur_idx] 插入到 j 的位置
                lis.pop(cur_idx + 1)        # 前面插入之后多了一个位置
                break
    return lis

"""
【 快速排序 】
思路：递归
  1. 从 序列 seq 中选第一个参数作为基准数 base
  2. 以 base 作为基准比较 seq, 比 base 小的 left_part 放 base 前面，比 base 大的 right_part 放 base 后面
  3. left_part, right_part 分别重复 1.2 步骤
"""
def quickSort(seq):
    if len(seq) < 2:
        return seq    # 递归出口
    else:
        base_idx = 0
        base = seq[base_idx]
        left_part = [i for i in seq[base_idx+1:] if i<= base]
        right_part = [i for i in seq[base_idx+1:] if i > base]
    return quickSort(left_part) + [base] +quickSort(right_part)   # 递归 合并
    
"""
【 合并两个有序序列 】
  有两个有序序列分别为 seq1, seq2。 给一个空序列 ret_seq 放最后排序好的结果
  seq1, seq2 索引分别为 i, j, 索引值初始化为 0
  
  思路：循环 索引推移
      1. seq1[i] 与 seq2[j] 比较，小的那个值放入 ret_seq, 索引+1向后推移
      2. 重复 1 步骤，直到 seq1, seq2 其中一个序列的索引走到最后
      3. 索引没有走到最后的另一序列直接加到 ret_seq 后面 (已经排序好了的可以直接加)
"""
def merge2SortedList(seq1, seq2):
    len1, len2 = len(seq1), len(seq2)
    i = j = 0   # 分别做为 seq1, seq2 的索引
    ret_seq = []
    
    while i < len1 and j < len2:    # 步骤 1, 2
        if seq1[i] < seq2[j]:
            ret_seq.append(seq1[i]) # 注意没有从原序列剔除元素，只是复制到 ret_seq
            i += 1
        else:
            ret_seq.append(seq2[j])
            j += 1
    
    if i < len1:                    # 步骤 3
        ret_seq.extend(seq1[i:])
    else:
        ret_seq.extend(seq2[j:])
    
    return ret_seq

"""
【 归并排序 】
    思路：分治法 三步走
        1. 分       : 以一个数作为基准 (这里用中间值)，将原序列分开为 两个子序列
        2. 排(递归) : 对两个子序列一直重复步骤 1, 直到每个
        3. 合并     :
"""
def mergeSort(seq):
    if len(seq) <= 1:
        return seq              # 递归出口
    else:
        mid = int(len(seq)/2)   # 中间的数作为基准数 mid: 基准数索引
        left_half = mergeSort(seq[:mid])
        # print('left_half :{}'.format(left_half))
        right_half = mergeSort(seq[mid:])
        # print('rght_half :{}'.format(right_half))

        # 到这里时 left_half, right_half 分别都是有序序列
        return merge2SortedList(left_half, right_half)

# ------------------------- 测试用例 ---------------------------------------------------------------
test_seq = list(range(10))

def test_merge2SortedList():
    """ 合并两个有序序列 测试用例 """
    assert merge2SortedList(sorted(test_seq), sorted(test_seq)) == sorted(test_seq+test_seq)

def test_mergeSort():
    """ 归并排序 测试用例 """
    random.shuffle(test_seq)    # 打乱顺序
    assert mergeSort(test_seq) == sorted(test_seq)  # 没报错就没错

def test_quickSort():
    """ 快速排序 测试用例 """
    random.shuffle(test_seq)    # 打乱顺序
    # print(test_seq)
    # print(bubbleSort(test_seq))
    assert quickSort(test_seq) == sorted(test_seq)  # 没报错就没错

def test_insertSort():
    """ 插入排序 测试用例 """
    random.shuffle(test_seq)    # 打乱顺序
    # print(test_seq)
    # print(bubbleSort(test_seq))
    assert insertSort(test_seq) == sorted(test_seq)  # 没报错就没错

def test_bubbleSort():
    """ 冒泡排序 测试用例 """
    random.shuffle(test_seq)    # 打乱顺序
    # print(test_seq)
    # print(bubbleSort(test_seq))
    assert bubbleSort(test_seq) == sorted(test_seq)  # 没报错就没错

# 运行测试用例
test_bubbleSort()       # 冒泡排序 测试
test_quickSort()        # 快速排序 测试
test_insertSort()       # 插入排序 测试
test_merge2SortedList() # 合并两个有序序列 测试
test_mergeSort()        # 归并排序 测试



