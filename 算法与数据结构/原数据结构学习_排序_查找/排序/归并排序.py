# 归并排序
#   思路：分治法 三步走
#   1. 分       : 以一个数作为基准 (这里用中间值)，将原序列分开为 两个子序列
#   2. 排(递归) : 对两个子序列一直重复步骤 1, 直到每个
#   3. 合并     :

# 合并两个有序序列 实现
def merge_sorted_list(seq1, seq2):
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


# 【 归并排序 】 实现
def merge_sort(seq):
    if len(seq) <= 1:
        return seq              # 递归出口
    else:
        mid = int(len(seq)/2)   # 中间的数作为基准数 mid: 基准数索引
        left_half = merge_sort(seq[:mid])
        print('left_half :{}'.format(left_half))
        right_half = merge_sort(seq[mid:])
        print('rght_half :{}'.format(right_half))
        # 到这里时 left_half, right_half 分别都是有序序列
        return merge_sorted_list(left_half, right_half)

# 归并排序 测试用例
def test_merge_sort():
    import random
    test_seq = list(range(10))
    random.shuffle(test_seq)    # 打乱顺序
    # print(test_seq)
    assert merge_sort(test_seq) == sorted(test_seq)  # 没报错就没错
    # print(merge_sort(test_seq))

if __name__ == '__main__':
    test_merge_sort()