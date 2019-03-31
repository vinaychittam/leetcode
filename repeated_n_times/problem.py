class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        seen = {}
        for i in A:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        for i, j in seen.items():
            if seen[i] == len(A) / 2:
                return i
        return False


A = [2,1,2,5,3,2]

obj = Solution()
assert 2 == obj.repeatedNTimes(A)
