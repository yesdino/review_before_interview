# 插入排序
def insertSort(lis):
    for cur_idx in range(1, len(lis)):  # 1,2,3..., n-1: 红色的那个数从第2个数到最后一个数
        for j in range(cur_idx):
            if lis[cur_idx] < lis[j]: # 红色的那个数 和 黑色的列表里面的数全部比一遍
                lis.insert(j, lis[cur_idx]) # lis[cur_idx] 插入到 j 的位置
                lis.pop(cur_idx + 1)        # 前面插入之后多了一个位置
                break
    return lis

# 测试用例
def test_insertSort():
    import random
    test_seq = list(range(10))
    random.shuffle(test_seq)    # 打乱顺序
    # print(test_seq)
    assert insertSort(test_seq) == sorted(test_seq)  # 没报错就没错

# 运行测试用例
test_insertSort()




