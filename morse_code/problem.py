class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        import string
        b = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        c = {}
        cnt = 0
        for i in string.ascii_lowercase:
            c[i] = b[cnt]
            cnt += 1

        seen = set()
        for word in words:
            res = ''
            for char in word:
                res += c[char]
            seen.add(res)


        return len(seen)


words = ["gin", "zen", "gig", "msg"]
obj = Solution()
print obj.uniqueMorseRepresentations(words)
                
