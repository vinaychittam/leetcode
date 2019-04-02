class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for i, j  in enumerate(A):
            temp = []
            for k in range(len(j)-1, -1, -1):
                temp.append(j[k])
            #print temp
            for ind, val in enumerate(temp):
                if val == 1:
                    temp[ind] = 0
                else:
                    temp[ind] = 1
            A[i] = temp
            #print A

        return A
A = [[1,1,0],[1,0,1],[0,0,0]]

obj = Solution()
assert [[1,0,0],[0,1,0],[1,1,1]] == obj.flipAndInvertImage(A)
