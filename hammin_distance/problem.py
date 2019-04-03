class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x = self.get_binary(x)
        y = self.get_binary(y)
        count = 0
        for i, j in enumerate(y):
            if x[i] != j:
                count += 1
        return count
                
        
    
    def get_binary(self,x):
        base = [0] * 32
        two_base = [0] * 32
        last = 31
        for i in range(32):
            two_base[last] = 2**i
            last -= 1
        
        last = 31
        temp = 0
      
        for i , j in enumerate(two_base):
            if j <= x:
                base[i] = 1
                x = x -j
        return base


obj = Solution()
assert 2 == obj.hammingDistance(1,4)
