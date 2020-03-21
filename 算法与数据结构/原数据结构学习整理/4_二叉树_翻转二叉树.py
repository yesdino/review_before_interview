# 树节点
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
"""
【 翻转二叉树 】 实现
    思路: 
    1. 每个节点左右节点对调
    2. 左右节点继续递归步骤 1, 递归出口: 没有子节点了就出来
"""
class Solution:
    def invertTree(self, root):
        if root:    # 递归出口
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root