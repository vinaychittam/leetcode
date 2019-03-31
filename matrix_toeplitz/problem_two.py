class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        
        if len(matrix[0]) == 1:
            return True
        for k in range(len(matrix[0])):
            for i in range(len(matrix[0])):
                temp = []
                col = i
                row = k
                base = min(len(matrix), len(matrix[0]) - col)
                #for i in range(base):
                while (row <= len(matrix) -1 ) and (col <= len(matrix[0]) -1):
                    temp.append(matrix[row][col])
                    row += 1
                    col += 1
                com = temp[0]
                for i in temp: 
                    if com != i:
                        return False
                print temp
        return True

        """
        row = 1
        col = 0
        for i in range(len(matrix) -1):
            temp = []
            row += i
            #col = i
	    #base = min(len(matrix)-1, (len(matrix)-1) - col)
            #base = (len(matrix) - 1 ) - i
            #for i in range(base):
            while row < len(matrix):

                temp.append(matrix[row][col])
                 
                row += 1
                col += 1

            col = 0
            #row += 1
            row = 1
            com = temp[0]
            for i in temp:
                if com != i:
                    return False
            print temp
            
        return True"""


obj = Solution()

matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
obj.isToeplitzMatrix(matrix)
                

        
        
