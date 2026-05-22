from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        freshCnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    freshCnt += 1
                elif grid[i][j] == 2:
                    q.append((i, j))

        if freshCnt == 0:
            return 0

        ans = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            sz = len(q)
            has_rotten = False
            for i in range(sz):
                x, y = q.popleft()
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= m or ny < 0 or ny >= n or grid[nx][ny] != 1:
                        continue
                    grid[nx][ny] = 2
                    has_rotten = True
                    freshCnt -= 1
                    q.append((nx, ny))
            if has_rotten:
                ans += 1

        return ans if freshCnt == 0 else -1
