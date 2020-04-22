# from util.Empty import Empty
# from util.Outbound import Outbound

# 链表节点类
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
    
# 链表类
class LinkedList:
    def __init__(self):
        self.head = Node()  # 哨兵结点
        self.length = 0     # 链表长度要有
    
    def peek(self):
        """找到头结点（因为第一个是哨兵结点）"""
        if not self.head.next:
            raise ValueError('LinkedList id empty')
        return self.head.next
    
    def add_first(self, value):
        """在最前面插入结点"""
        # 其实是在哨兵结点和头结点之间插入结点
        new_node = Node(value, None)
        new_node.next = self.head.next  
        self.head.next = new_node
        self.length += 1
    
    def add_last(self, value):
        new_node = Node(value, None)
        node = self.head
        while node.next != None:
            node = node.next
        node.next = new_node    # new_node 的 next 为空（尾结点）
        self.length += 1
    
    def add(self, index, value):
        if (index < 0 or index >= self.length):
            raise ValueError('index is out of bound')
        if not self.head.next:
            raise ValueError('LinkedList id empty')
        
        node = self.head
        for _ in range(index):
            node = node.next
        # 此时 node 为 index 索引上的结点
        new_node = Node(value, None)
        new_node.next = node.next
        node.next = new_node
        self.length += 1

    def get_first(self):
        """找到头结点 O(1)"""
        if not self.head.next:
            raise ValueError('LinkedList id empty')
        return self.head.next
    
    def get_last(self):
        """找到最后一个结点 O(n)"""
        if not self.head.next:
            raise ValueError('LinkedList id empty')
        node = self.head
        while node.next != None:
            node = node.next
        return node
    
    def get(self, index):
        """找到指定索引的结点"""
        if (index < 0 and  index >= self.length):
            raise ValueError('index is out of bound')
        if not self.head.next:
            raise ValueError('LinkedList id empty')

        node = self.head.next
        for _ in range(index):
            node = node.next
        return node

    def remove_first(self):
        """删除头结点"""
        if not self.head.next:
            raise ValueError('LinkedList id empty')
        re_node = self.head.next
        self.head.next = self.head.next.next
        self.length -= 1
        return re_node.value      # 返回被删除的头结点

    def remove_last(self):
        """删除最后一个结点"""
        if not self.head.next:
            raise ValueError('LinkedList id empty')
        node_pre = self.head
        node = self.head.next
        while node.next != None:
            node_pre = node
            node = node.next
        # 此时 node 为最后一个结点, node_pre 为最后一个结点的前一个结点
        node_pre.next = None
        return node.value

    def remove(self, index):
        """删除指定结点"""
        if (index < 0 or index >= self.length):
            raise ValueError('index is out of bound')
        if not self.head.next:
            raise ValueError('LinkedList id empty')
            
        node = self.head
        for _ in range(index):
            node = node.next
        # 此时 node 已经是 index 索引前面的一个结点（因为从哨兵结点开始）
        del_node = node.next
        node.next = node.next.next
        self.length -= 1
        return del_node
    
    def printlist(self):
        """打印链表"""
        node = self.head.next
        count = 0
        while node and count < 20:
            print(node.value, end=" ")
            node = node.next
            count += 1
        print('')
    
    def size(self):
        return self.length