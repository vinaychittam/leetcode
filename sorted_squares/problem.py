class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        last_index = len(A) - 1
        first_index = 0
        for i in range(len(A)):
            if A[first_index] * A[first_index] >= A[last_index] * A[last_index]:
                f_i = first_index + 1
                for q in range(f_i, last_index):
                    if A[q] * A[q] >= A[last_index] * A[last_index]:
                        A[q], A[last_index] = A[last_index], A[q]
                       
                A[first_index], A[last_index] = A[last_index], A[first_index]
            else:
                f_i = first_index + 1
                for k in range(f_i, last_index):
                    if A[k] * A[k] >= A[last_index] * A[last_index]:
                        A[k], A[last_index] = A[last_index], A[k]
                        break
                    
                
            last_index -= 1
        for i, j in enumerate(A):
            A[i] = j * j
        return A
                
# Note inplace memory
