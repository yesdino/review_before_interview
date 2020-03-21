# 链表节点
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

"""
【 删除链表节点 】
    思路：被删除节点后面的节点全部前移
"""
def deleteNone(self, node):
    next_node = node.next               # 下一个节点
    after_next_node = node.next.next    # 下下个节点

    node.val = next_node.val            # 要删除节点的位置 替换为 下一个节点
    node.next = after_next_node         # 要删除节点的下一个节点的指针 指向 下下个节点

