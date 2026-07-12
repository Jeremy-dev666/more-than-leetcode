import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q = stones
        heapq.heapify_max(q)
        while len(q) > 1:
            x = heapq.heappop_max(q)
            y = heapq.heappop_max(q)
            if x > y:
                heapq.heappush_max(q, x - y)
        return q[0] if q else 0
        