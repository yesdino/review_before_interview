import random
    






    

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



"""
【 冒泡排序 】
思路：
每一轮都依次选择相邻两个元素，不符合排序顺序就交换。
接着进行下一轮
"""
def bubbleSort(lis):
    pass

"""
【 插入排序 】
思路：
排麻将一样，每一轮里面依次挑一个数，到了合适的位置后面的位置都往后搓
"""
def insertSort(lis):
    pass
    

"""
【 快速排序 】
思路：递归
  1. 从 序列 seq 中选第一个参数作为基准数 base
  2. 以 base 作为基准比较 seq, 比 base 小的 left_part 放 base 前面，比 base 大的 right_part 放 base 后面
  3. left_part, right_part 分别重复 1.2 步骤
"""
def quickSort(seq):
    pass
    
    
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
    pass
    

"""
【 归并排序 】
    思路：分治法 三步走
        1. 分       : 以一个数作为基准 (这里用中间值)，将原序列分开为 两个子序列
        2. 排(递归) : 对两个子序列一直重复步骤 1, 直到每个
        3. 合并     :
"""
def mergeSort(seq):
    pass


# 运行测试用例
test_bubbleSort()       # 冒泡排序 测试
# test_quickSort()        # 快速排序 测试
# test_insertSort()       # 插入排序 测试
# test_merge2SortedList() # 合并两个有序序列 测试
# test_mergeSort()        # 归并排序 测试



