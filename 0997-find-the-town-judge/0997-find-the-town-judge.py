class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegrees = [0] * (n + 1)
        outdegrees = [0] * (n + 1)

        for t in trust:
            fr = t[0]
            to = t[1]
            indegrees[to] += 1
            outdegrees[fr] += 1

        for i in range(1, n + 1):
            if indegrees[i] == n - 1 and outdegrees[i] == 0:
                return i
        return -1

        
            
