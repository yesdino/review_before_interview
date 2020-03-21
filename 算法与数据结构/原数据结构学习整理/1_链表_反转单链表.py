# 链表节点
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
"""
【 反转单链表 】 实现
  思路: 
      重新构造一个新链表
      遍历方向与原链表不变 但是 next 指向下一节点的属性要相反
"""
def reverseList(self, head):
    """
    type head: ListNone
    rtype: ListNone
    """
    pre = None
    cur = head
    while cur:
        # 遍历方向与原链表不变 但是 next 指向下一节点的属性要相反
        nextnode = cur.next 
        cur.next = pre      
        # 继续按原链表 next 方向遍历
        pre = cur           
        cur = nextnode