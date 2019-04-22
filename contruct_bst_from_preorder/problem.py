# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        
        ind_item = set()
        node_dict = {}
        for ind, val in enumerate(preorder):
            #for every value find min and max
            # min is the very next item
            # max is the first val greater than the val
            
            # find min max only if the item is not last
            if ind == len(preorder) -1:
                node_dict[val] = [None, None]
            #if ind == len(preorder) - 2:
            #    node_dict[]
            else:
                # find min
                if val > preorder[ind+1]:
                    mini = preorder[ind+1]
                    # index for mini = ind + 1
                    ind_item.add((ind+1, mini))
                else:
                    # index for mini = No index
                    mini = None
                # find max
                flag = True
                for i in range(ind+1, len(preorder)):
                    maxi = None
                    if val  <= preorder[i]:
                        flag = False
                        maxi = preorder[i]
                        if (i,preorder[i]) in ind_item:
                            # if the ind and val is found in the set, right node will be none
                            maxi = None
                            node_dict[val] = [mini,maxi]
                        else:
                            # if the ind and val not found in set
                            maxi = preorder[i]
                            node_dict[val] = [mini, maxi]
                            ind_item.add((i, maxi))
                        break
                if flag is True:
                    node_dict[val] = [mini, maxi] 
                
                    
                
                    # update node_dict with max = None
                    # if min found set is updated for child
                    # dict needs to be updated yet for the case where max is not found
                        
                
        
        
        #print node_dict
        #print ind_item
        self.node_dict = node_dict
        root = TreeNode(preorder[0])
        self.helper(root)
        #for i in preorder:
        return root
            
    def helper(self, node):
        if node is None:
            return None
        #if node.val in self.node_dict:
        l_r = self.node_dict[node.val]
        if l_r[0] is not None:
            node.left = TreeNode(l_r[0])
            self.helper(node.left)
        if l_r[1] is not None:
            node.right = TreeNode(l_r[1])
            self.helper(node.right)
            
        return node
            
            
