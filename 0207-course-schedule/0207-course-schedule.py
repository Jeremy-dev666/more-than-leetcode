from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses
        for to, fr in prerequisites:
            adj[fr].append(to)
            indegrees[to] += 1

        q = deque()
        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)

        cnt = numCourses
        while q:
            cur = q.popleft()
            cnt -= 1
            for nxt in adj[cur]:
                indegrees[nxt] -= 1
                if indegrees[nxt] == 0:
                    q.append(nxt)

        return cnt == 0
