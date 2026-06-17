from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for cur, prev in prerequisites:
            graph[prev].append(cur)
            indegree[cur] += 1

        ans = []
        q = deque(c for c in range(numCourses) if indegree[c] == 0)
        while q:
            cur = q.popleft()
            ans.append(cur)
            for nxt in graph[cur]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)

        return ans if len(ans) == numCourses else []