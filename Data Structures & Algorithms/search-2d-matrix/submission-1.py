class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix)-1, len(matrix[0])-1
        row_l, row_h = 0, rows
        col_l, col_h = 0, cols
        while row_l <= row_h and col_l <= col_h:
            row_m = (row_l+row_h)//2
            col_m = (col_l+col_h)//2
            if target > matrix[row_m][col_m]:
                col_l = col_m + 1
                if col_l > cols:
                    row_l += 1
                    col_l = 0
                    col_h = cols
            elif target < matrix[row_m][col_m]:
                col_h = col_m - 1
                if col_h < 0:
                    row_h -= 1
                    col_l = 0
                    col_h = cols
            else: # match
                return True
        return False