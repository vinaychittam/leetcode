class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """

        row = len(matrix) - 2
        col = 1
 
        while row >= 0:
            temp = []
            t_r = 0
            t_c = -(col)
            for i in range(col + 1):
                
                temp.append(matrix[row + t_r][col + t_c ])
                t_r += 1
                t_c += 1


            base = temp[0]
            for i in temp:
                if i != base:
                    return False
            print temp
            row  -= 1
            col += 1


        
        
        return True


obj = Solution()

matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
obj.isToeplitzMatrix(matrix)
                

        
        
