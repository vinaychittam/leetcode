class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        
        for i in range(len(matrix)):
            row = i
            col = 0
            for j in range(len(matrix[0])):
                print matrix[row][col]
                t_r = row
                t_c = col
                temp = matrix[row][col]
                while (t_r <= len(matrix) -1 ) and (t_c <= len(matrix[0]) -1):
                    if matrix[t_r][t_c] != temp:
                        return False
                    else:
                        t_r += 1
                        t_c += 1
                col += 1
        
        return True        
        

obj = Solution()

matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
matrix = [[11,74,0,93],[40,11,74,7]]
print obj.isToeplitzMatrix(matrix)
                

        
        
