class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_row = []
        for i, j  in enumerate(grid):
            max_row.append(max(j))
        max_col = []
        total = 0
        for i in range(len(grid[0])):
            maxi = -1000000
            for j in range(len(grid)):
                if grid[j][i] > maxi:
                    maxi = grid[j][i]
            max_col.append(maxi)
        
        for ind_x, x in enumerate(grid):
            for ind_y, y in enumerate(x):
                row_max = max_row[ind_x]
                col_max = max_col[ind_y]
                base = min(row_max, col_max)
                
                res = base - grid[ind_x][ind_y]
                grid[ind_x][ind_y] += res
                total += res
                
        return total

grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]

obj = Solution()

assert 35 == obj.maxIncreaseKeepingSkyline(grid)
