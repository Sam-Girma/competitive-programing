class Solution:

    def maximalSquare(self, matrix: List[List[str]]) -> int:

        dp_grid = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        # print(dp_grid)
        maximum = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col]=="0":
                    dp_grid[row][col] = 0
                else:
                    if row==0 or col==0:
                        dp_grid[row][col] = 1
                    else:
                        dp_grid[row][col] = min(dp_grid[row-1][col], dp_grid[row] [col-1], dp_grid[row-1][col-1])+1
                maximum = max(maximum, dp_grid[row][col])
        

        return maximum**2
