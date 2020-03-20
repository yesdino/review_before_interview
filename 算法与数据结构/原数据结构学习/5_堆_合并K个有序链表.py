# 链表节点
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

"""
【 合并K个有序链表 】
"""
from heapq import heapify, heappop
class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]     # 输入: 嵌套列表
        :rtype: ListNode                # 输出: 链表
        """
        h = []  # 读取所有节点值
        for node in lists:
            while node:
                h.append(node.val)
                node = node.next
        
        if not h:
            return None
        # 构造最小堆
        heapify(h)          # heapify: 将列表转化为最小堆

        # 构造链表
        root = ListNode(heappop(h)) # 最小堆堆顶元素构成节点
        curnode = root
        while h:
            nextnode = ListNode(heappop(h))
            # 下一次循环初始化
            curnode.next = nextnode
            curnode = nextnode
        return root


