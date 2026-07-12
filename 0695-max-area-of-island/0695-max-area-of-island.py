DIRS = [[-1, 0], [1, 0], [0, -1], [0, 1]]

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        area = 0

        def dfs(x, y):
            nonlocal area
            if not(0 <= x < m and 0 <= y < n) or grid[x][y] != 1:
                return

            grid[x][y] = 0
            area += 1
            for dx, dy in DIRS:
                dfs(x + dx, y + dy)
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = 0
                    dfs(i, j)
                    ans = max(ans, area)

        return ans