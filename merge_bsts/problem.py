# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None and t2 is None:
            return t1
        self.res = []
        t3 = TreeNode(None)
        c = 1
        res = self.helper(t1, t2, t3)
        #c = 1
        print self.res
        return t3
    def helper(self, t1, t2, t3):
        
        if not t1 and not t2:
            return None
        temp = []
        if t1:
            temp.append(t1.val)
        #else:
        #    temp.append(0)
            
        if t2:
            temp.append(t2.val)
        #else:
        #    temp.append(0)
        if sum(temp) != 0:
            self.res.append(sum(temp))
        #print "t3 val %d" % (sum(temp))
        
        t3.val = sum(temp)
        #else:
        #    t3 = TreeNode(sum(temp))
        #c += 1
        #t1.val = sum(temp)
        if t1 and t2:
            #t3.left = TreeNode(t1.val + t2.val)
            if t1.left is not None:
                t3.left = TreeNode(t1.left.val)
            elif t2.left is not None:
                t3.left = TreeNode(t2.left.val)
            #else:
                #t3.left = TreeNode(None)
            self.helper(t1.left, t2.left, t3.left)
        elif t1 and not t2:
            #t3.left = TreeNode(t1.val)
            if t1.left is not None:
                t3.left = TreeNode(t1.left.val)
            #else:
            #    t3.left = TreeNode(None)
            self.helper(t1.left, None, t3.left)
        elif t2 and not t1:
            #t3.left = TreeNode(t2.val)
            if t2.left is not None:
                
                t3.left = TreeNode(t2.left.val)
            #else:
            #    t3.left = TreeNode(None)
            self.helper(None, t2.left, t3.left)
        else:
            return None
            
        if t1 and t2:
            #t3.right = TreeNode(t1.val + t2.val)
            if t1.right is not None:
                t3.right = TreeNode(t1.right.val)
            elif t2.right is not None:
                t3.right = TreeNode(t2.right.val)
            #else:
            #    t3.right = TreeNode(None)
            #t3.right = TreeNode(0)
            self.helper(t1.right, t2.right, t3.right)
        elif t1 and not t2:
            #t3.right = TreeNode(t1.val)
            if t1.right is not None:
                t3.right = TreeNode(t1.right.val)
            #else:
            #    t3.right = TreeNode(None)
            #t3.right = TreeNode(0)
            self.helper(t1.right, None, t3.right)
        elif t2 and not t1:
            #t3.right = TreeNode(t2.val)
            if t2.right is not None:
                t3.right = TreeNode(t2.right.val)
            #else:
            #    t3.right = TreeNode(None)
            #t3.right = TreeNode(0)
            self.helper(None, t2.right, t3.right)
        else:
            return None
        
        return t3
            
                
        
