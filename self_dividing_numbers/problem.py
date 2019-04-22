class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        self.res = []
        for i in range(left, right +1):
            if i == 10:
                continue
            if i > 10:
                #print i
                ans = self.helper(i)
                if ans is not True:
                    continue
            else:
                self.res.append(i)
        return self.res
            
        
    def helper(self, num):
        self.base = num
        
        while num != 0:
            temp = num % 10
            if temp == 0:
                return False
            if self.base % temp == 0:
                #print self.base%temp
                num = num // 10
            else:
                return False
        self.res.append(self.base)
        return True
                
