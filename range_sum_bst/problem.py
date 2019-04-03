#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        self.total = 0
        self.L = L
        self.R = R
        self.get_total(root)
        return self.total

    def get_total(self, node):
        if not node:
            return None
        if node.val >= self.L and node.val <= self.R:
            self.total += node.val
        if node.left:    
            self.get_total(node.left)
        if node.right:
            self.get_total(node.right)
