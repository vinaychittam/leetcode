
emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """

        seen = set()
        for email in emails:
            ln_dn = email.split('@')
            ln = ln_dn[0]
            dn = ln_dn[1]
            res = ''
            for char in ln:
                if char == "+":
                    break
                if char == '.':
                    continue
                res += char
            res = res + '@' + dn
            seen.add(res)
         
        return len(seen)    
       

obj = Solution()

print obj.numUniqueEmails(emails) 
