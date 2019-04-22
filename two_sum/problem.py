class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i, j in enumerate(nums):
            
            if target - j in seen:
                return [i, seen[target-j]]
            seen[j] = i
                
        
