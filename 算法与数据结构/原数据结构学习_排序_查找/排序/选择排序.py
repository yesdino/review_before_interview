"""
思路：
第一趟：第 1 个数假设为最小值 剩下的数遍历一遍找到最小值与第 1 个数的位置交换
第二趟：第 2 个数假设为最小值 剩下的数遍历一遍找到最小值与第 2 个数的位置交换
...
第i趟 ：第 i 个数假设为最小值 剩下的数遍历一遍找到最小值与第 i 个数的位置交换
"""
# 选择排序
def select_sort(lis):
    for i in range(len(lis)-1): # 要进行多少轮
        min = i     # 记录当前正在进行比较的那个数的索引 假设为最小值
        for j in range(i+1, len(lis)): # 当前那个数 与 后面的数比较
            if lis[j] < lis[min]:
                min = j
        lis[i], lis[min] = lis[min], lis[i]
    return lis

# 测试用例
def testSort():
    import random
    test_seq = list(range(10))
    random.shuffle(test_seq)    # 打乱顺序
    # print(test_seq)
    # print(select_sort(test_seq))
    assert select_sort(test_seq) == sorted(test_seq)  # 没报错就没错

# 运行测试用例
testSort()




