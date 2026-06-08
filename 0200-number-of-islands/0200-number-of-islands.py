class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        cnt = 0
        for i in range (n):
            for j in range (m):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    cnt += 1
        return cnt

    def dfs(self, grid: List[List[str]], i: int, j: int) -> None:
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return
        if grid[i][j] != "1":
            return
        grid[i][j] = "0"
        
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j - 1)
        self.dfs(grid, i, j + 1)