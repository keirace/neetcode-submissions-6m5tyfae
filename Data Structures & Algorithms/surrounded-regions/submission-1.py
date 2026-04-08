class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # connected group
        rows, cols = len(board), len(board[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        que = deque()

        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows - 1 or 
                    c == 0 or c == cols - 1 and 
                    board[r][c] == "O"
                    ):
                    que.append((r, c))
        # turn all the O borders to T
        while que:
            x, y = que.popleft() # current = 'O'
            if board[x][y] == 'O':
                board[x][y] = 'T'
                for dx, dy in directions:
                    nx, ny = x+dx, y+dy
                    if (0<=nx<rows 
                    and 0<=ny<cols 
                    ):
                        que.append((nx,ny))
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"