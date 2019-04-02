class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        start = 0
        last = len(A) -1
        a = [0] * len(A)
        for i, j in enumerate(A):
            if j % 2 == 0:
                a[start] = j
                start += 1
            else:
                a[last] = j
                last -= 1
        return a
obj = Solution()
A = [3,1,2,4]
assert [2,4,1,3] == obj.sortArrayByParity(A) 
