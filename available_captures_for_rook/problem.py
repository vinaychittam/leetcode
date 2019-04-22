class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        # find the index for the rook
        
        index = None
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "R":
                    index = (i,j)
        count  = 0
        #print index
        row = index[0]
        col = index[-1]
        
        for i in range(col, len(board[0])):
            if board[row][i] == 'B':
                break
            elif board[row][i] == 'p':
                count += 1
                break
        for i in range(col, 0, -1):
            if board[row][i] == 'B':
                break
            elif board[row][i] == 'p':
                count += 1
                break
                
        for i in range(row, len(board)):
            if board[i][col] == 'B':
                break
            elif board[i][col] == 'p':
                count += 1
                break
                
        for i in range(row, 0, -1):
            if board[i][col] == 'B':
                break
            elif board[i][col] == 'p':
                count += 1
                break
                
                
                
        return count
