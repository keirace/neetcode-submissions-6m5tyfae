class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[0] * 9 for _ in range(len(board))]
        cols = [[0] * 9 for _ in range(len(board[0]))]
        squares = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                num = int(board[i][j]) - 1
                if rows[num][i] or cols[num][j] or num in squares[(i//3, j//3)]:
                    return False
                rows[num][i] = 1
                cols[num][j] = 1
                squares[(i//3, j//3)].add(num)
        return True