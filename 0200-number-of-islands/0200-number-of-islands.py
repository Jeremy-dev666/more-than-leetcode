dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(x, y):
            if not(0 <= x < m and 0 <= y < n) or grid[x][y] != "1":
                return
            
            grid[x][y] = "0"
            for d in dirs:
                nx, ny = d[0] + x, d[1] + y
                dfs(nx, ny)

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    ans += 1

        return ans
                
