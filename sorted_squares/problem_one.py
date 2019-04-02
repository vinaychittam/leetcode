class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        for i, j  in enumerate(A):
            A[i] = j * j
        A.sort()
        return A
