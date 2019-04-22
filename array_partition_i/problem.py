class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        res = []
        #print nums
        for i in range(0, len(nums), 2):
            if i == len(nums) - 1:
                break
            res.append([nums[i], nums[i+1]])
        total = 0
        for i in res:
            total += min(i)
            
        return total
        
