class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # capacity: [maxW, totalW]
        l, r = max(weights), sum(weights)
        while l < r:
            mid = (l + r) // 2
            if self.canFinish(mid, weights, days):
                r = mid
            else:
                l = mid + 1
        return l

    def canFinish(self, capacity, weights, days):
        load = 0
        d = 1
        for w in weights:
            if load + w > capacity:
                d += 1
                load = 0
            load += w
        return d <= days
