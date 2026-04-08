class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        maxarea = 0
        def bfs(r, c):
            nonlocal maxarea
            que = deque([(r, c)])
            grid[r][c] = 0
            area = 1
            while que:
                x, y = que.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        area += 1
                        que.append((nx, ny))
                        grid[nx][ny] = 0
            return area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxarea = max(bfs(r, c), maxarea)

        return maxarea
            