# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # check for every node if the left and right values are 1 or 0
        # if the left and right are both 0 return None 
        # Even if one of them has a 1, create a node 
    
        root.left = self.helps(root.left)
        root.right = self.helps(root.right)
        return root
    def helps(self, node):
        if node is None:
            return None
        # check for 
        #flag = True
        node.left = self.helps(node.left)
        node.right = self.helps(node.right)
        if node.left is None and node.right is None and node.val == 0:
            return None
        else:
            return node
        
    
