class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        for col in range(n):
            if obstacleGrid[0][col] == 1:
                break
            dp[0][col] = 1
        for row in range(m):
            if obstacleGrid[row][0] == 1:
                break
            dp[row][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]