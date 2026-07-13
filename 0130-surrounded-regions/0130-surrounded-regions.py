DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        def dfs(x, y):
            if not (0 <= x < m and 0 <= y < n):
                return
            if board[x][y] == "X" or board[x][y] == "$":
                return
                
            board[x][y] = "$"
            for dx, dy in DIRS:
                nx, ny = dx + x, dy + y
                dfs(nx, ny)

        # 从四条边切为"O"进入DFS
        for i in range(m):
            for j in range(n):
                is_edge = (i == 0 or i == m - 1 or j == 0 or j == n - 1)
                if is_edge and board[i][j] == "O":
                    dfs(i, j)

        # 恢复现场，淹没陆地
        for i in range(m):
            for j in range(n):
                if board[i][j] == "$":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"

        


