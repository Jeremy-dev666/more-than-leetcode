class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        while left < right:
            mid = left + (right - left) // 2
            if self.canFinish(mid, weights, days):
                right = mid
            else:
                left = mid + 1
        return left

    def canFinish(self, capacity, weights, days):
        ans = 1
        cur_load = 0
        for w in weights:
            if cur_load + w > capacity:
                ans += 1
                cur_load = 0
            cur_load += w
        return ans <= days
        