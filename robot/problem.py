class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        a = {"U": 0, "D": 0, "L":0, "R": 0}
        
        for i in moves:
            if i in a:
                a[i] += 1
            else:
                a[i] = 1
        return (a["U"] == a["D"] and a["L"] == a["R"])

obj = Solution()

moves = "UUDD"
assert True == obj.judgeCircle(moves) 
