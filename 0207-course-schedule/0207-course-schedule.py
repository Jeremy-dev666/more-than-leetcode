from collections import deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses
        for pre in prerequisites:
            indegrees[pre[0]] += 1
            adj[pre[1]].append(pre[0])

        q = deque()
        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)
        
        cnt = numCourses
        while q:
            cur_course = q.popleft()
            cnt -= 1
            for nxt_course in adj[cur_course]:
                indegrees[nxt_course] -= 1
                if indegrees[nxt_course] == 0:
                    q.append(nxt_course)

        return cnt == 0