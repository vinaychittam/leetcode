class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        res = ''
        for i in str:
            if ord(i) not in range(ord('a'), ord('z')) and ord(i) not in range(ord('A'), ord('Z')):
                res += i
                continue
            
            if ord(i) < 97:
                res += chr(ord(i) + 32)
            else:
                res += i
        return res
        
a = "Vinay"

obj = Solution()
assert "vinay" == obj.toLowerCase(a)
