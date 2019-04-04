#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        maxi = [float('-inf'),0]
        for i, j in enumerate(nums):
            if j > maxi[0]:
                maxi[0] = j
                maxi[-1] = i
        left_arr = nums[0:maxi[-1]]
        right_arr = nums[maxi[-1] + 1:]
        
        root = TreeNode(maxi[0])
        root.left = self.helper(left_arr, root)
        root.right = self.helper(right_arr, root)
        return root
    def helper(self, nums, node):
        if node is None:
            return None
        
        maxi = [float('-inf'),0]
        for i, j in enumerate(nums):
            if j > maxi[0]:
                maxi[0] = j
                maxi[-1] = i
        left_arr = nums[0:maxi[-1]]
        right_arr = nums[maxi[-1] + 1:]
        if maxi[0] == float('-inf'):
            node = None
            return None
        else:
            node = TreeNode(maxi[0])
        
        node.right = self.helper(right_arr, node)
        node.left = self.helper(left_arr, node)
        return node

obj = Solution()
nums = [3,2,1,6,0,5]
#assert [6,3,5,None,2,0,None,None,1] == obj.constructMaximumBinaryTree(nums)
obj.constructMaximumBinaryTree(nums)
