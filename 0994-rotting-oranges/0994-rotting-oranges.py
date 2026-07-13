from collections import deque

DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        ans = 0
        while q:
            sz = len(q)
            rotted_this_turn = False

            for _ in range(sz):
                x, y = q.popleft()
                for dx, dy in DIRS:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        rotted_this_turn = True
                        q.append((nx, ny))
            if rotted_this_turn:
                ans += 1

        return ans if fresh == 0 else -1



                