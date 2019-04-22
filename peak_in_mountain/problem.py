class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        maxi = float('-inf')
        res = 0
        for i , j in enumerate(A):
            if j > maxi:
                maxi = j
                res = i
                
        return res
