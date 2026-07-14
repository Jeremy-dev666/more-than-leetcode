class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = []
        indegrees = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        for to, fr in prerequisites:
            indegrees[to] += 1
            adj[fr].append(to)

        q = deque()
        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)
        while q:
            cur = q.popleft()
            ans.append(cur)
            for nxt in adj[cur]:
                indegrees[nxt] -= 1
                if indegrees[nxt] == 0:
                    q.append(nxt)
        
        return ans if len(ans) == numCourses else []
