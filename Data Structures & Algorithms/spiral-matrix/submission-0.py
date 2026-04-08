class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        rows, cols = len(matrix), len(matrix[0])
        steps = [cols, rows-1] # starts at row 0, need to update rows-1 times

        direction = 0
        i, j = 0, -1
        while steps[direction & 1]:
            for _ in range(steps[direction & 1]):
                i += directions[direction][0]
                j += directions[direction][1]
                res.append(matrix[i][j])
            steps[direction & 1] -= 1
            direction += 1
            direction %= 4
        return res