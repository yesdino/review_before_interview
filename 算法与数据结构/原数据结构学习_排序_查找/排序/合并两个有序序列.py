# 合并两个有序序列
#   有两个有序序列分别为 seq1, seq2。 给一个空序列 ret_seq 放最后排序好的结果
#   seq1, seq2 索引分别为 i, j, 索引值初始化为 0
#   思路：循环 索引推移
#       1. seq1[i] 与 seq2[j] 比较，小的那个值放入 ret_seq, 索引+1向后推移
#       2. 重复 1 步骤，直到 seq1, seq2 其中一个序列的索引走到最后
#       3. 索引没有走到最后的另一序列直接加到 ret_seq 后面 (已经排序好了的可以直接加)

# 实现
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

# 测试
a = [1, 2, 5]
b = [0, 6, 7, 2, 3, 9]
# 注意给的参数序列要有序
print(merge_sorted_list(sorted(a), sorted(b)))

