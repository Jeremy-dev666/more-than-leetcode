from collections import deque

INF = 2147483647
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return

        m, n = len(rooms), len(rooms[0])
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        q = deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i, j))

        while q:
            x, y = q.popleft()
            for dx, dy in DIRS:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and rooms[nx][ny] == INF:
                    rooms[nx][ny] = rooms[x][y] + 1
                    q.append((nx, ny))