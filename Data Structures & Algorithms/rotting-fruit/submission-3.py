class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        minutes = 0
        fresh = 0
        que = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    que.append((r,c))
                    
        while fresh > 0 and que:
            for _ in range(len(que)):
                x, y = que.popleft()
                for dx, dy in directions:
                    nx, ny = dx + x, dy + y
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -=1
                        que.append((nx,ny))
            minutes += 1
        return minutes if fresh == 0 else -1