from queue import PriorityQueue
from clas.LinkedList import LinkedList
from clas.LinkedList import Node

def mergeKLists(lists):
    dummy = Node()  # 哨兵结点: 记录合并以后的链表的头，完成之后直接返回
    cur = dummy
    q = PriorityQueue()
    # 先把每个链表的第一个结点先放进去
    for node in lists:
        if node is not None:
            q.put((node.value, node))
    while q.qsize() > 0:
        min_node = q.get()[1]
        cur.next = min_node
        cur = cur.next
        if cur.next:
            q.put((cur.next.value, cur.next))
    return dummy.next       # 注意：返回的时候不能返回哨兵节点，而是哨兵的next 头结点

# ------------------------------------------
lst1 = LinkedList()
lst1.add_last(1)
lst1.add_last(4)
lst1.add_last(5)

lst2 = LinkedList()
lst2.add_last(1)
lst2.add_last(3)
lst2.add_last(4)

lst3 = LinkedList()
lst3.add_last(2)
lst3.add_last(6)

# -------------------------
lists = [
    lst1.head.next, 
    lst2.head.next, 
    lst3.head.next
]
node = mergeKLists(lists)   # <----
result = LinkedList()

result.head.next = node
result.printlist()