class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj = [[] for _ in range(n)]
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        q = deque()
        visited = set()
        cnt = 0
        q.append(0)
        visited.add(0)

        while q:
            cur = q.popleft()
            cnt += 1
            for nxt in adj[cur]:
                if nxt not in visited:
                    visited.add(nxt)
                    q.append(nxt)

        return cnt == n
