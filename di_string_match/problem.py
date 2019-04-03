class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        maxi = len(S)
        mini = 0
        A = []
        for i in S:
            if i == "I":
                A.append(mini)
                mini += 1
            else:
                A.append(maxi)
                maxi -= 1
        if S[-1] == "I":
            A.append(A[-1] + 1)
        else:
            A.append(A[-1] - 1)
        return A


obj = Solution()
S = "IDID"
assert [0,4,1,3,2] == obj.diStringMatch(S)
