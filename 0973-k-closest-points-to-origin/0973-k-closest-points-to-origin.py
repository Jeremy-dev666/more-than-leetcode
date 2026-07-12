import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hq = [(self.square(points[i]), i) for i in range(k)]
        heapq.heapify_max(hq)
        for i in range(k, len(points)):
            dist = self.square(points[i])
            if dist < hq[0][0]:
                heapq.heappop_max(hq)
                heapq.heappush_max(hq, (dist, i))
        return [points[i] for (_, i) in hq]

    def square(self, point):
        return point[0] ** 2 + point[1] ** 2