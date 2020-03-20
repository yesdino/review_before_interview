# 树节点
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
"""
【 层序遍历 二叉树 】 实现
    思路: 
    需要有两个列表，list1 放当前层的节点，list2 放接下来要继续访问的下一层节点
    直到下一层没有节点之后停止
"""
class Solution:
    def leverOrder(self, root):
        res = []
        if root:    # 注意 root 可能为空
            cur_nodes = [root]
            next_nodes = []
            res.append([i.val for i in cur_nodes])  # 先把第一层加进去
            while cur_nodes or next_nodes:
                for node in cur_nodes:
                    if node.left:
                        next_nodes.append(node.left)
                    if node.right:
                        next_nodes.append(node.right)
                if next_nodes:
                    res.append([i.val for i in cur_nodes])  # 把每一层加进去
                
                # 初始化下一次循环
                cur_nodes = next_nodes
                next_nodes = []
        return res