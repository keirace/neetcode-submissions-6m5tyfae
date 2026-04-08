class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        def bfs(r, c):
            que = deque([(r, c)])
            visited = set()
            distance = 0
            while que:
                distance += 1
                for _ in range(len(que)):
                    x, y = que.popleft()
                    for dx , dy in directions:
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != -1 and grid[nx][ny] != 0 and (nx, ny) not in visited:
                            grid[nx][ny] = min(distance, grid[nx][ny])
                            visited.add((nx, ny))
                            que.append((nx, ny))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    bfs(r, c)