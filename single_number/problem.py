class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = {}
        for i in nums:
            if i not in seen:
                seen[i] = 1
            else:
                seen[i] += 1
                
        for i, j in seen.items():
            if j == 1:
                return i
                

obj = Solution()
nums = [2,2,1]
assert 1 == obj.singleNumber(nums)
