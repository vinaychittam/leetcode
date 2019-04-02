class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        for ind, val in enumerate(A):
            #is_even = len(i) % 2 == 0
            #mid = len() // 2
            last = -1
            temp = []
            
            for ind1, val1 in enumerate(val):
                A[ind][ind1], A[ind][last] = A[ind][last], A[ind][ind1]
                last = last - 1
        print (A)
        for ind, val in enumerate(A):
            for c,j in enumerate(val):
                if j == 0:
                    A[ind][c] = 1
                else:
                    A[ind][c] = 0
        return A
                    
                
                
        
