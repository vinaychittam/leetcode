# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        self.insert(root, val)
        return root
    def insert(self, node, val):
        if not node:
            return None
        if val > node.val:
            if node.right:
                self.insert(node.right, val)
            else:
                node.right = TreeNode(val)
        elif val < node.val:
            if node.left:
                self.insert(node.left, val)
            else:
                node.left = TreeNode(val)
        return node
        
        
