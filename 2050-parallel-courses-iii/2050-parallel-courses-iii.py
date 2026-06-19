from collections import deque
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:

        adj = [[] for _ in range(n)]
        indegrees = [0] * n
        for r in relations:
            prev = r[0] - 1
            nxt = r[1] - 1
            adj[prev].append(nxt)
            indegrees[nxt] += 1

        q = deque()
        finish = [0] * n
        for i in range(n):
            if indegrees[i] == 0:
                finish[i] = time[i]
                q.append(i)

        while q:
            idx = q.popleft()
            for nxt in adj[idx]:
                finish[nxt] = max(finish[nxt], finish[idx] + time[nxt])
                indegrees[nxt] -= 1
                if indegrees[nxt] == 0:
                    q.append(nxt)

        return max(finish)
