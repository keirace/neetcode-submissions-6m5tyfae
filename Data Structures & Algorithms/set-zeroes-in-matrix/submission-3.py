class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        row_set = set()
        col_set = set()
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    row_set.add(i)
                    col_set.add(j)

        for i in row_set:
            for j in range(cols):
                matrix[i][j] = 0

        for i in col_set:
            for j in range(rows):
                matrix[j][i] = 0
