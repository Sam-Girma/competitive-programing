class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        """
        [1,2,3],
        [4,5,6],
        [7,8,9]]
        """
        def get(r, c):
            if r < 0 or r >= len(mat) or c < 0 or c >= len(mat[0]):
                return 0
            return mat[r][c]
        
        top_left = 0
        for i in range(k+1):
            for j in range(k+1):
                top_left += get(i, j)

        result = []
        for row_idx in range(len(mat)):
            result.append([])
            for col_idx in range(len(mat[0])):
                res = None
                if col_idx == 0:
                    if row_idx == 0:
                        res = top_left
                    else:
                        top_row = bottom_row = 0
                        for i in range(-k, k+1):
                            top_row += get(row_idx-1-k, col_idx+i)
                            bottom_row += get(row_idx+k, col_idx+i)
                        res = result[row_idx-1][col_idx] - top_row + bottom_row
                else:
                    left_col = right_col = 0
                    for i in range(-k, k+1):
                        left_col += get(row_idx + i, col_idx-1-k)
                        right_col += get(row_idx + i, col_idx+k)
                    res = result[row_idx][col_idx-1] - left_col + right_col
                    
                result[-1].append(res)
        return result
        


        
