
# 【 二叉树节点 】定义
class BinTreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# 二叉树
#   思路: 
#       前中后 序遍历其实就是打印节点的值而已，只不过依靠 left, right 来定位
#       看递归中做的操作，其实就只有一句 就是 print(node.data)    

# 【 二叉树 类 】
class BinTree(object):
    def __init__(self, root=None):
        self.root = root
    
    def pre_order_trav(self, subtree):
        ''' 先(根)序遍历 '''
        if subtree is not None:
            # 每层递归做的处理
            print(subtree.data)     # 打印节点值 

            self.pre_order_trav(subtree.left)   # 递归处理左子树
            self.pre_order_trav(subtree.right)  # 递归处理右子树 
        # else:pass    # 递归出口
    
    def in_order_trav(self, subtree):
        ''' 中序遍历 '''
        if subtree is not None:
            self.pre_order_trav(subtree.left)   
            print(subtree.data)
            self.pre_order_trav(subtree.right)
    
    def af_order_trav(self, subtree):
        ''' 后序遍历 '''
        if subtree is not None:
            self.pre_order_trav(subtree.left)   
            self.pre_order_trav(subtree.right)
            print(subtree.data)
        

