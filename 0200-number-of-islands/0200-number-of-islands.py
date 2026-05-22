class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.m, self.n = len(grid), len(grid[0])
        ans = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    ans += 1
        
        return ans

    def dfs(self, grid, i, j) -> None:
        if i < 0 or i >= self.m or j < 0 or j >= self.n:
            return
        if grid[i][j] != "1":
            return
        
        grid[i][j] = "-1"
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j - 1)
        self.dfs(grid, i, j + 1)
    