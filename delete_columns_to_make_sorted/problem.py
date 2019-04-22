class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
       
        alphabets = {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6, 'i': 9, 'h': 8, 'k': 11, 'j': 10, 'm': 13, 'l': 12, 'o': 15, 'n': 14, 'q': 17, 'p': 16, 's': 19, 'r': 18, 'u': 21, 't': 20, 'w': 23, 'v': 22, 'y': 25, 'x': 24, 'z': 26}
        B = []
        for i in range(len(A)):
            temp = []
            for j in range(len(A[0])):
                temp.append(alphabets[A[i][j]])
            B.append(temp)
        cnt = 0
        for i in range(len(B[0])):
            temp = []
            for j in range(len(B)):
                temp.append(B[j][i])
            maxi = float('-inf')
            for i in temp:
                if i >= maxi:
                    maxi = i
                    #print maxi
                else:
                    #print maxi
                    cnt += 1
                    break
            
        return cnt
