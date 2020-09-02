"""
思路：
每一轮都依次选择相邻两个元素，不符合排序顺序就交换。
接着进行下一轮
"""
# 冒泡排序
def bubbleSort(lis):
    for i in range(len(lis)-1):         # 要进行多少轮
        for j in range(len(lis)-i-1):   # 每一轮的比较范围 len(lis)—i-1:后面的黑色的已经排序好的不再继续比较
            if lis[j] > lis[j+1]:       # 比较范围内两两比较
                lis[j], lis[j+1] = lis[j+1], lis[j]
    return lis


# ----------------------------------------------
# 测试用例
def testSort():
    import random
    test_seq = list(range(10))
    random.shuffle(test_seq)    # 打乱顺序
    # print(test_seq)
    # print(bubbleSort(test_seq))
    assert bubbleSort(test_seq) == sorted(test_seq)  # 没报错就没错

# 运行测试用例
testSort()




